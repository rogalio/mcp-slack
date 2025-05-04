# Main entry point for the Slack MCP server
from .app import mcp_app
from core.config import get_settings

def run_server():
    """Configures and runs the FastMCP server with SSE transport."""
    print("Starting Slack MCP Server...")

    # Check if essential config is loaded before starting
    settings = get_settings()
    if not settings.slack_token:
        print("Warning: SLACK_BOT_TOKEN is not configured. Some features may not work properly.")
        print("Please set the SLACK_BOT_TOKEN environment variable in .env file.")

    # Run the server using FastMCP's built-in SSE transport
    print("Starting FastMCP server with SSE transport on http://127.0.0.1:8000")
    try:
        # Use FastMCP's built-in run method with SSE transport (not HTTP directly)
        mcp_app.run(transport="sse", port=8000)
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    run_server()