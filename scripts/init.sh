#!/bin/bash
# Initialization script for marketing_spec_kit

set -e

echo "Initializing marketing_spec_kit..."

# Check if uv is installed
if command -v uv &> /dev/null; then
    echo "Using uv for faster installation..."
    uv sync
else
    echo "uv not found, falling back to pip..."
    echo "Tip: Install uv for faster dependency management: curl -LsSf https://astral.sh/uv/install.sh | sh"
    pip install -e .
fi

echo "✓ marketing_spec_kit initialized successfully!"
echo ""
echo "Next steps:"
echo "  - Run 'marketing_spec_kit --help' to see available commands"
echo "  - Check README.md for usage instructions"
echo "  - Read AGENTS.md for AI-assisted development guide"
