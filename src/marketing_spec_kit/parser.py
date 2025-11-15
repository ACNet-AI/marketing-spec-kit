"""Parser for Marketing Operations Specification (YAML/JSON)

Supports:
- YAML files (.yaml, .yml)
- JSON files (.json)
- Python dictionaries
- String content (YAML/JSON)

v2.0.0 Changes:
- Automatically parses 'plans' field (MarketingPlan entities)
- Automatically parses 'analytics' field (Analytics reports)
- Campaign.plan_id is now REQUIRED (BREAKING CHANGE from v1.x)

Performance Target: Parse <100ms for typical specs (<1000 lines)
"""

import json
from pathlib import Path
from typing import Union

import yaml
from pydantic import ValidationError as PydanticValidationError

from marketing_spec_kit.exceptions import ParseError, ValidationError
from marketing_spec_kit.models import MarketingSpec


class MarketingSpecParser:
    """Parser for converting YAML/JSON to MarketingSpec objects
    
    Example:
        >>> parser = MarketingSpecParser()
        >>> spec = parser.parse("my-spec.yaml")  # From file
        >>> spec = parser.parse(yaml_string, format="yaml")  # From string
        >>> spec = parser.parse({"project": {...}}, format="dict")  # From dict
    """

    def parse(
        self,
        source: Union[str, Path, dict],
        format: str = "auto",
    ) -> MarketingSpec:
        """Parse marketing specification from various sources
        
        Args:
            source: File path (str/Path), string content, or dict
            format: "auto" (detect), "yaml", "json", or "dict"
        
        Returns:
            MarketingSpec object with validated entities
        
        Raises:
            ParseError: If YAML/JSON parsing fails (MKT-VAL-001)
            ValidationError: If Pydantic validation fails (MKT-VAL-002, MKT-VAL-003)
        
        Performance:
            - Typical spec (<1000 lines): <100ms
            - Uses yaml.CSafeLoader when available (10x faster)
        """
        try:
            # Step 1: Load data from source → dict
            data = self._load_data(source, format)
            
            # Step 2: Validate and parse dict → MarketingSpec (Pydantic validation)
            spec = self._parse_spec(data)
            
            return spec
            
        except ParseError:
            raise  # Re-raise our custom errors
        except ValidationError:
            raise
        except Exception as e:
            raise ParseError(
                code="MKT-VAL-001",
                message=f"Unexpected parsing error: {e}",
                fix="Check file format and syntax",
            ) from e
    
    def _load_data(
        self,
        source: Union[str, Path, dict],
        format: str,
    ) -> dict:
        """Load data from source into dictionary
        
        Args:
            source: File path, string content, or dict
            format: Format hint ("auto", "yaml", "json", "dict")
        
        Returns:
            dict: Parsed data
        
        Raises:
            ParseError: If loading fails
        """
        # If already dict, return directly
        if isinstance(source, dict):
            return source
        
        # Detect format from file extension
        if format == "auto":
            if isinstance(source, (str, Path)):
                path = Path(source)
                if path.exists() and path.is_file():
                    suffix = path.suffix.lower()
                    if suffix in [".yaml", ".yml"]:
                        format = "yaml"
                    elif suffix == ".json":
                        format = "json"
                    else:
                        # Default to YAML for unknown extensions
                        format = "yaml"
                else:
                    # Assume string content is YAML
                    format = "yaml"
            else:
                format = "yaml"
        
        # Load based on format
        if format == "yaml":
            return self._load_yaml(source)
        elif format == "json":
            return self._load_json(source)
        else:
            raise ParseError(
                code="MKT-VAL-001",
                message=f"Unsupported format: {format}",
                fix="Use 'yaml', 'json', or 'dict' format",
            )
    
    def _load_yaml(self, source: Union[str, Path]) -> dict:
        """Load YAML from file or string
        
        Args:
            source: File path or YAML string
        
        Returns:
            dict: Parsed YAML
        
        Raises:
            ParseError: If YAML parsing fails (MKT-VAL-001)
        """
        try:
            # Check if source is a file path
            path = Path(source)
            if path.exists() and path.is_file():
                with open(path, "r", encoding="utf-8") as f:
                    # Use CSafeLoader if available (C implementation, 10x faster)
                    Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
                    data = yaml.load(f, Loader=Loader)
            else:
                # Treat as YAML string
                Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
                data = yaml.load(str(source), Loader=Loader)
            
            if not isinstance(data, dict):
                raise ParseError(
                    code="MKT-VAL-001",
                    message=f"Expected dict, got {type(data).__name__}",
                    fix="Ensure YAML root is a mapping (key-value pairs)",
                )
            
            return data
            
        except yaml.YAMLError as e:
            error_msg = str(e)
            line = None
            if hasattr(e, "problem_mark"):
                line = e.problem_mark.line + 1
                error_msg = f"Line {line}: {e.problem}"
            
            raise ParseError(
                code="MKT-VAL-001",
                message=f"Invalid YAML syntax: {error_msg}",
                fix="Check YAML syntax, ensure proper indentation and no tabs",
                line=line,
            ) from e
    
    def _load_json(self, source: Union[str, Path]) -> dict:
        """Load JSON from file or string
        
        Args:
            source: File path or JSON string
        
        Returns:
            dict: Parsed JSON
        
        Raises:
            ParseError: If JSON parsing fails (MKT-VAL-001)
        """
        try:
            # Check if source is a file path
            path = Path(source)
            if path.exists() and path.is_file():
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                # Treat as JSON string
                data = json.loads(str(source))
            
            if not isinstance(data, dict):
                raise ParseError(
                    code="MKT-VAL-001",
                    message=f"Expected dict, got {type(data).__name__}",
                    fix="Ensure JSON root is an object {{...}}",
                )
            
            return data
            
        except json.JSONDecodeError as e:
            raise ParseError(
                code="MKT-VAL-001",
                message=f"Invalid JSON syntax: {e.msg} at line {e.lineno}, column {e.colno}",
                fix="Check JSON syntax, ensure proper quoting and commas",
                line=e.lineno,
            ) from e
    
    def _parse_spec(self, data: dict) -> MarketingSpec:
        """Parse dict into MarketingSpec using Pydantic validation
        
        Args:
            data: Parsed YAML/JSON data
        
        Returns:
            MarketingSpec: Validated specification object
        
        Raises:
            ValidationError: If Pydantic validation fails (MKT-VAL-002, MKT-VAL-003)
        """
        try:
            spec = MarketingSpec(**data)
            return spec
            
        except PydanticValidationError as e:
            # Extract first error for clear messaging
            errors = e.errors()
            first_error = errors[0]
            
            # Determine error code and create helpful message
            error_type = first_error["type"]
            field_path = ".".join(str(loc) for loc in first_error["loc"])
            error_msg = first_error["msg"]
            
            if error_type == "missing":
                code = "MKT-VAL-002"
                message = f"Missing required field: '{field_path}'"
                fix = f"Add '{field_path}' field to your specification"
            else:
                code = "MKT-VAL-003"
                message = f"Invalid value for '{field_path}': {error_msg}"
                fix = f"Check the value and type for '{field_path}'"
            
            # Extract entity name if possible
            entity = ""
            if first_error["loc"]:
                entity = str(first_error["loc"][0])
            
            raise ValidationError(
                code=code,
                message=message,
                entity=entity,
                field=field_path,
                value=first_error.get("input"),
                fix=fix,
            ) from e

