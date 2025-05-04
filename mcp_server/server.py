from fastmcp import FastMCP
from mcp_server.tools.message_tools import register_message_tools
from mcp_server.resources.slack_resources import register_slack_resources
# Import other tool/resource registration functions as needed

def create_app() -> FastMCP:
    #--- Initialize FastMCP with proper configuration ---
    mcp = FastMCP(
        name="Slack Connector MCP 🚀",
        description="MCP server for connecting to Slack APIs",
        transport="sse",  # Default to SSE transport
    )

    # Register tools and resources
    register_message_tools(mcp)
    register_slack_resources(mcp)

    return mcp

#--- Initialize the application ---
mcp_app = create_app()
