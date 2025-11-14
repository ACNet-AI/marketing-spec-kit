"""
CLI for marketing_spec_kit.
"""

import typer
from rich.console import Console

app = typer.Typer(
    name="marketing_spec_kit",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()

@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    """
    marketing_spec_kit - Specification toolkit

    Use --help with commands for more information.
    """
    # If no subcommand is provided, show help
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())

@app.command()
def info():
    """Show speckit information"""
    console.print("[cyan]Speckit:[/cyan] marketing_spec_kit")
    console.print("[yellow]No functionality implemented yet.[/yellow]")
    console.print("\nNext steps:")
    console.print("  1. Use /metaspec.specify to define your specification")
    console.print("  2. Use /metaspec.implement to add CLI commands")
    console.print("  3. See AGENTS.md for AI-assisted development guide")

def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
