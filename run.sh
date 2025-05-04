#!/bin/bash
# Enhanced script to run the Slack MCP server with proper environment setup



# Check and activate virtual environment if it exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source ".venv/bin/activate"
else
    echo "Warning: No virtual environment found at .venv/"
    echo "Using system Python installation..."
fi

# Check for required Python packages and install if missing
echo "Checking required packages..."
python3 -m pip install -r requirements.txt

# Run the specified command
if [ $# -eq 0 ]; then
    echo "Starting MCP server..."
    python3 -m main
else
    echo "Running command: python3 $@"
    python3 "$@"
fi