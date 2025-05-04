from services.slack_service import slack_service
from core.types import ToolResult
from core.handlers import tool_response

def register_message_tools(mcp):
    """Register Slack messaging tools."""

    # --- Direct Messages ---
    @mcp.tool()
    def send_slack_direct_message(user_id: str, message_text: str) -> ToolResult:
        """Send DM to Slack user."""
        success, result = slack_service.send_dm(user_id=user_id, text=message_text)
        return tool_response(success, result if success else None, result if not success else None)

    # --- Channel Messages ---
    @mcp.tool()
    def send_slack_channel_message(channel_id: str, message_text: str) -> ToolResult:
        """Send message to Slack channel."""
        success, result = slack_service.send_message(channel_id=channel_id, text=message_text)
        return tool_response(success, result if success else None, result if not success else None)

    # --- Channel Listing ---
    @mcp.tool()
    def list_slack_channels() -> ToolResult:
        """List available Slack channels."""
        success, channels = slack_service.list_channels()
        return tool_response(success, channels if success else None, channels if not success else None)

    # --- User Listing ---
    @mcp.tool()
    def list_slack_users(random_string: str = "") -> ToolResult:
        """List all Slack users in the workspace."""
        success, users = slack_service.list_users()
        return tool_response(success, users if success else None, users if not success else None)

