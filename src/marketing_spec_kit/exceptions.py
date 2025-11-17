"""Exception classes for marketing-spec-kit

Error Codes (from domain specification):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MKT-VAL-001: Invalid YAML/JSON syntax
MKT-VAL-002: Missing required field
MKT-VAL-003: Invalid field value
MKT-REF-001: Reference integrity violation (entity not found)
MKT-REF-002: Circular dependency detected
"""

from typing import Any, Optional


class MarketingSpecError(Exception):
    """Base exception for all marketing-spec-kit errors"""

    def __init__(self, code: str, message: str, fix: str = ""):
        self.code = code
        self.message = message
        self.fix = fix
        super().__init__(f"[{code}] {message}")


class ParseError(MarketingSpecError):
    """Error during specification parsing (YAML/JSON → dict)
    
    Error codes: MKT-VAL-001, MKT-VAL-002
    """

    def __init__(self, code: str, message: str, fix: str = "", line: Optional[int] = None):
        self.line = line
        super().__init__(code, message, fix)


class ValidationError(MarketingSpecError):
    """Error during specification validation (dict → MarketingSpec)
    
    Error codes: MKT-VAL-003, MKT-REF-001, MKT-REF-002
    """

    def __init__(
        self,
        code: str,
        message: str,
        entity: str = "",
        field: str = "",
        value: Any = None,
        fix: str = "",
    ):
        self.entity = entity
        self.field = field
        self.value = value
        super().__init__(code, message, fix)

