from typing import Dict, List, Union, Any
from services.slack_service import slack_service
from core.handlers import resource_response
from fastmcp import FastMCP

def register_slack_resources(mcp: FastMCP):
    """Register all Slack resources with MCP app."""

    # --- Channels ---
    @mcp.resource(uri="https://slack.api/channels")
    def get_slack_channels() -> Any:
        """Get available Slack channels."""
        success, result = slack_service.list_channels()
        return resource_response(success, result)

    # --- Users ---
    @mcp.resource(uri="https://slack.api/user/{user_id}")
    def get_slack_user(user_id: str) -> Any:
        """Get user profile data."""
        success, result = slack_service.get_user(user_id=user_id)
        return resource_response(success, result)

    @mcp.resource(uri="https://slack.api/user/{user_id}/details")
    def get_slack_user_details(user_id: str) -> Any:
        """Get structured user profile."""
        success, result = slack_service.get_user(user_id=user_id)
        return resource_response(success, result)