"""
Generator for creating marketing project structures from templates.

This module implements the core generation logic that creates
complete marketing project directories with specifications,
constitutions, and necessary configuration files.

Following MetaSpec's Generator Pattern:
- Creates PROJECT FILES (directories, specs, constitution)
- NOT domain content (social posts, articles, campaigns)
"""

import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from jinja2 import (
    BaseLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
)

from marketing_spec_kit.exceptions import MarketingSpecError


class ProjectGenerationError(MarketingSpecError):
    """Raised when project generation fails."""
    pass


class TemplateRenderError(ProjectGenerationError):
    """Raised when template rendering fails."""
    pass


class MarketingProjectGenerator:
    """
    Generate complete marketing project structures from templates.

    The generation process:
    1. Validate output directory
    2. Select templates
    3. Create template context
    4. Render all templates
    5. Build project structure
    6. Write to disk (atomic)
    """

    def __init__(self, custom_template_dir: Path | None = None):
        """
        Initialize generator with Jinja2 environment.

        Args:
            custom_template_dir: Optional path to custom templates
        """
        # Initialize Jinja2 environment
        loader: BaseLoader
        if custom_template_dir:
            loader = FileSystemLoader(str(custom_template_dir))
        else:
            # Use packaged templates
            loader = PackageLoader("marketing_spec_kit", "project_templates")

        self.env = Environment(
            loader=loader,
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

    def generate_project(
        self,
        project_name: str,
        output_dir: Path,
        template: str = "default",
        force: bool = False,
        dry_run: bool = False,
    ) -> dict[str, Any]:
        """
        Generate a complete marketing project from template.

        Args:
            project_name: Name of the new project
            output_dir: Output directory path
            template: Template type (minimal, default, full)
            force: If True, overwrite existing directory
            dry_run: If True, only return structure without writing

        Returns:
            Dictionary with project structure and metadata

        Raises:
            FileExistsError: If output_dir exists and force=False
            TemplateRenderError: If template rendering fails
        """
        # Step 1: Validate output directory
        if not dry_run and output_dir.exists() and not force:
            raise FileExistsError(
                f"Output directory already exists: {output_dir}\n"
                "Use --force flag to overwrite."
            )

        # Step 2: Create template context
        context = self._create_context(project_name, template)

        # Step 3: Select files based on template type
        files_to_generate = self._select_files(template)

        # Step 4: Render templates
        rendered_files = {}
        for rel_path, template_name in files_to_generate.items():
            try:
                rendered_files[rel_path] = self._render_template(
                    template_name, context
                )
            except Exception as e:
                raise TemplateRenderError(
                    f"Failed to render {template_name}: {e}"
                ) from e

        # Step 5: Determine which commands would be deployed
        commands_source = Path(__file__).parent.parent.parent / "templates" / "sdm" / "commands"
        command_files = list(commands_source.glob("*.md")) if commands_source.exists() else []
        
        # Step 6: Deploy slash commands (unless dry_run)
        if not dry_run:
            self._deploy_slash_commands(output_dir)
        
        # Step 7: Write files (unless dry_run)
        if not dry_run:
            self._write_files(output_dir, rendered_files, force)

        # Combine rendered files and command files for reporting
        all_files = (
            list(rendered_files.keys()) + 
            [f".marketingspeckit/commands/{cmd.name}" for cmd in command_files]
        )
        
        return {
            "project_name": project_name,
            "output_dir": str(output_dir),
            "template": template,
            "files": all_files,
            "file_count": len(all_files),
        }

    def _create_context(self, project_name: str, template: str) -> dict[str, Any]:
        """
        Create Jinja2 template context.

        Args:
            project_name: Name of the project
            template: Template type

        Returns:
            Template context dictionary
        """
        return {
            "project_name": project_name,
            "template_type": template,
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "toolkit_name": "marketing-spec-kit",
            "toolkit_version": "0.3.0",
        }

    def _select_files(self, template: str) -> dict[str, str]:
        """
        Select infrastructure files to generate (MetaSpec-aligned structure).

        New architecture (v0.4.0):
        - specs/ - Marketing strategy specifications (Markdown)
        - config/ - Campaign configurations (YAML) - created by /marketspec.implement
        - templates/ - Content templates - created by /marketspec.implement
        - data/ - Collected metrics (JSON) - created by code execution
        - src/ - Executable code (TypeScript) - created by /marketspec.implement
        
        Per "Generator vs AI Commands: Role Separation":
        - Generator creates project infrastructure only (memory/, specs/, README)
        - config/, templates/, data/, src/ created by /marketspec.implement
        - Like MetaSpec: Generator doesn't pre-create src/, implement does
        
        Architectural consistency (MetaSpec pattern):
        - specs/README.md exists (workflow guidance for creating specs)
        - config/, templates/, data/, src/ have NO README (generated artifacts)

        Args:
            template: Template type (minimal, default)

        Returns:
            Dictionary mapping output paths to template names
        """
        # Infrastructure files (MetaSpec-aligned structure)
        files = {
            "memory/constitution.md": "constitution.md.j2",
            "specs/README.md": "specs-readme.md.j2",  # Specification workflow
            # Note: config/, templates/, data/, src/ NOT pre-created by generator
            # Like src/ in MetaSpec, these are created by /marketspec.implement
            # when executing tasks and generating code + configurations
            "README.md": "readme.md.j2",
            ".gitignore": "gitignore.j2",
        }

        # Note: template parameter kept for future extensibility
        # Currently both minimal and default generate the same infrastructure

        return files

    def _render_template(self, template_name: str, context: dict[str, Any]) -> str:
        """
        Render a single template.

        Args:
            template_name: Name of the template file
            context: Template context

        Returns:
            Rendered template content

        Raises:
            TemplateNotFound: If template doesn't exist
        """
        template = self.env.get_template(template_name)
        return template.render(**context)

    def _deploy_slash_commands(self, output_dir: Path) -> list[Path]:
        """
        Deploy toolkit's slash commands to user project.
        
        Copies all command files from toolkit's templates to 
        `.marketingspeckit/commands/` so AI assistants can read them.
        
        Args:
            output_dir: Output directory for the project
            
        Returns:
            List of deployed command file paths
        """
        # Get toolkit's command directory
        commands_source = Path(__file__).parent.parent.parent / "templates" / "sdm" / "commands"
        
        if not commands_source.exists():
            return []  # No commands to deploy
        
        # Create target directory
        commands_target = output_dir / ".marketingspeckit" / "commands"
        commands_target.mkdir(parents=True, exist_ok=True)
        
        # Copy all command files
        deployed = []
        for cmd_file in commands_source.glob("*.md"):
            target_file = commands_target / cmd_file.name
            shutil.copy2(cmd_file, target_file)
            deployed.append(cmd_file)
        
        return deployed
    
    def _write_files(
        self,
        output_dir: Path,
        files: dict[str, str],
        force: bool,
    ) -> None:
        """
        Write rendered files to disk.

        Args:
            output_dir: Output directory
            files: Dictionary of relative_path -> content
            force: If True, overwrite existing files
        """
        # Create output directory if needed
        # Note: Directory might already exist if _deploy_slash_commands() ran first
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
        elif not force:
            # Directory exists and force=False, check if it was created by us
            # (has .marketingspeckit but no other files)
            existing_files = [f for f in output_dir.rglob("*") if f.is_file()]
            non_command_files = [
                f for f in existing_files 
                if not str(f.relative_to(output_dir)).startswith(".marketingspeckit/commands/")
            ]
            if non_command_files:
                raise FileExistsError(
                    f"Output directory already exists with files: {output_dir}\n"
                    "Use --force flag to overwrite."
                )

        # Write all files
        for rel_path, content in files.items():
            file_path = output_dir / rel_path
            file_path.parent.mkdir(parents=True, exist_ok=True)

            file_path.write_text(content, encoding="utf-8")

