"""
CLI for marketing_spec_kit - Marketing Operations Specification Toolkit

Commands:
- init: Create a new specification from template
- validate: Validate an existing specification
- info: Show toolkit information
"""

import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax

from marketing_spec_kit import __version__
from marketing_spec_kit.parser import MarketingSpecParser
from marketing_spec_kit.validator import MarketingSpecValidator
from marketing_spec_kit.exceptions import MarketingSpecError, ParseError, ValidationError

app = typer.Typer(
    name="marketing_spec_kit",
    help="Marketing Operations Specification Toolkit",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


@app.command()
def info():
    """Show toolkit information"""
    console.print(Panel.fit(
        f"[bold cyan]marketing-spec-kit[/bold cyan] [dim]v{__version__}[/dim]\n\n"
        "[yellow]Marketing Operations Specification Toolkit[/yellow]\n\n"
        "Domain: [green]Marketing Operations[/green]\n"
        "Entities: [green]7[/green] (Project, Product, Campaign, Channel, Tool, Template, Milestone)\n"
        "Validation Rules: [green]42[/green]\n"
        "Commands: [green]init, validate, info[/green]",
        title="📦 Toolkit Info",
        border_style="cyan",
    ))
    
    console.print("\n[bold]Available Commands:[/bold]")
    console.print("  [cyan]init[/cyan] <filename>      Create a new specification from template")
    console.print("  [cyan]validate[/cyan] <filename>  Validate an existing specification")
    console.print("  [cyan]info[/cyan]                 Show this information")


@app.command()
def init(
    filename: str = typer.Argument(..., help="Output filename (e.g., my-spec.yaml)"),
    template: str = typer.Option(
        "default",
        "--template",
        "-t",
        help="Template to use: minimal, default, or full",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite existing file",
    ),
):
    """Create a new marketing specification from template
    
    Templates:
    - minimal: Project only with required fields
    - default: Complete example (Project + Products + Campaign + Channels)
    - full: All entities with all optional fields
    
    Example:
        marketing_spec_kit init my-spec.yaml
        marketing_spec_kit init my-spec.yaml --template=full
    """
    try:
        # Check if file exists
        output_path = Path(filename)
        if output_path.exists() and not force:
            console.print(f"[red]✗[/red] File '{filename}' already exists")
            console.print("  Use --force to overwrite")
            raise typer.Exit(1)
        
        # Load template
        template_dir = Path(__file__).parent.parent.parent / "templates" / "entity_templates"
        template_file = template_dir / f"{template}.yaml"
        
        if not template_file.exists():
            console.print(f"[red]✗[/red] Template '{template}' not found")
            console.print(f"  Available templates: minimal, default, full")
            raise typer.Exit(1)
        
        # Copy template to output
        content = template_file.read_text()
        output_path.write_text(content)
        
        # Success message
        console.print(f"[green]✓[/green] Created '{filename}' from '{template}' template")
        console.print(f"\n[bold]Next steps:[/bold]")
        console.print(f"  1. Edit '{filename}' and fill in your project details")
        console.print(f"  2. Run: [cyan]marketing_spec_kit validate {filename}[/cyan]")
        
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to create specification: {e}")
        raise typer.Exit(1)


@app.command()
def validate(
    filename: str = typer.Argument(..., help="Specification file to validate (YAML or JSON)"),
    strict: bool = typer.Option(
        False,
        "--strict",
        "-s",
        help="Fail on warnings (treat warnings as errors)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show detailed validation info",
    ),
):
    """Validate a marketing specification
    
    Checks:
    - YAML/JSON syntax
    - Required fields
    - 42 validation rules (VR-P01 to VR-M05)
    - Reference integrity (product_ids, channel_ids, etc.)
    
    Example:
        marketing_spec_kit validate my-spec.yaml
        marketing_spec_kit validate my-spec.yaml --strict
    """
    try:
        # Check if file exists
        spec_path = Path(filename)
        if not spec_path.exists():
            console.print(f"[red]✗[/red] File '{filename}' not found")
            raise typer.Exit(1)
        
        # Parse specification
        console.print(f"[cyan]→[/cyan] Parsing '{filename}'...")
        parser = MarketingSpecParser()
        
        try:
            spec = parser.parse(spec_path)
            console.print(f"[green]✓[/green] Parsing successful")
        except (ParseError, ValidationError) as e:
            console.print(f"[red]✗[/red] Parsing failed: [{e.code}] {e.message}")
            if hasattr(e, 'fix') and e.fix:
                console.print(f"  [yellow]Fix:[/yellow] {e.fix}")
            if hasattr(e, 'line') and e.line:
                console.print(f"  [dim]Line {e.line}[/dim]")
            raise typer.Exit(1)
        
        # Validate specification
        console.print(f"[cyan]→[/cyan] Validating specification...")
        validator = MarketingSpecValidator()
        result = validator.validate(spec)
        
        # Display results
        console.print()
        _display_validation_result(result, verbose)
        
        # Exit code
        if not result.valid:
            raise typer.Exit(1)
        elif strict and result.warning_count > 0:
            console.print(f"\n[yellow]⚠[/yellow] Warnings present (strict mode enabled)")
            raise typer.Exit(1)
        else:
            console.print(f"\n[green bold]✓ Validation successful![/green bold]")
            raise typer.Exit(0)
        
    except MarketingSpecError:
        # Already handled above
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]✗[/red] Unexpected error: {e}")
        if verbose:
            import traceback
            console.print(traceback.format_exc())
        raise typer.Exit(1)


def _display_validation_result(result, verbose: bool = False):
    """Display validation results with rich formatting"""
    
    # Summary panel
    summary_lines = [
        f"Rules Checked: [cyan]{result.rules_checked}[/cyan]",
        f"Rules Passed: [green]{result.rules_passed}[/green]",
        f"Success Rate: [{'green' if result.success_rate >= 90 else 'yellow'}]{result.success_rate:.1f}%[/]",
    ]
    
    if result.error_count > 0:
        summary_lines.append(f"Errors: [red]{result.error_count}[/red]")
    if result.warning_count > 0:
        summary_lines.append(f"Warnings: [yellow]{result.warning_count}[/yellow]")
    if verbose and len(result.info) > 0:
        summary_lines.append(f"Info: [blue]{len(result.info)}[/blue]")
    
    console.print(Panel(
        "\n".join(summary_lines),
        title="📊 Validation Summary",
        border_style="cyan" if result.valid else "red",
    ))
    
    # Errors table
    if result.error_count > 0:
        console.print()
        errors_table = Table(title="❌ Errors", border_style="red", show_lines=True)
        errors_table.add_column("Code", style="red bold")
        errors_table.add_column("Entity", style="cyan")
        errors_table.add_column("Field", style="yellow")
        errors_table.add_column("Message", style="white")
        errors_table.add_column("Fix", style="green")
        
        for err in result.errors:
            errors_table.add_row(
                err.code,
                f"{err.entity_type}\n[dim]{err.entity_id}[/dim]" if err.entity_id else err.entity_type,
                err.field,
                err.message,
                err.fix,
            )
        
        console.print(errors_table)
    
    # Warnings table
    if result.warning_count > 0:
        console.print()
        warnings_table = Table(title="⚠️  Warnings", border_style="yellow")
        warnings_table.add_column("Code", style="yellow bold")
        warnings_table.add_column("Entity", style="cyan")
        warnings_table.add_column("Message", style="white")
        warnings_table.add_column("Suggestion", style="green dim")
        
        for warn in result.warnings:
            warnings_table.add_row(
                warn.code,
                f"{warn.entity_type}\n[dim]{warn.entity_id}[/dim]" if warn.entity_id else warn.entity_type,
                warn.message,
                warn.fix,
            )
        
        console.print(warnings_table)
    
    # Info (verbose only)
    if verbose and len(result.info) > 0:
        console.print()
        info_table = Table(title="ℹ️  Info", border_style="blue")
        info_table.add_column("Code", style="blue bold")
        info_table.add_column("Entity", style="cyan")
        info_table.add_column("Message", style="white")
        
        for info in result.info:
            info_table.add_row(
                info.code,
                f"{info.entity_type}\n[dim]{info.entity_id}[/dim]" if info.entity_id else info.entity_type,
                info.message,
            )
        
        console.print(info_table)


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
