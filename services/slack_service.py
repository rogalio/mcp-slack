from typing import List, Dict, Optional
from slack_sdk import WebClient
from core.decorators import api_call_handler
from core.client import SlackClient

class SlackService:
    """Service for Slack API operations."""

    def __init__(self, client: Optional[WebClient] = None):
        """Initialize with client or default."""
        self.client = client or SlackClient.get_default()

    api_call = api_call_handler(lambda self: self.client)

    # --- Messages ---
    @api_call
    def send_dm(self, user_id: str, text: str) -> str:
        """Send DM to user."""
        response_conv = self.client.conversations_open(users=user_id)
        channel_id = response_conv["channel"]["id"]
        response_chat = self.client.chat_postMessage(channel=channel_id, text=text)
        return response_chat["ts"]

    @api_call
    def send_message(self, channel_id: str, text: str) -> str:
        """Send message to channel."""
        response = self.client.chat_postMessage(channel=channel_id, text=text)
        return response["ts"]

    # --- Users ---
    @api_call
    def get_user(self, user_id: str) -> dict:
        """Get user profile."""
        response = self.client.users_info(user=user_id)
        return response["user"]

    @api_call
    def list_users(self) -> List[Dict]:
        """List all users in the workspace."""
        response = self.client.users_list()
        return response["members"]

    # --- Channels ---
    @api_call
    def list_channels(self) -> List[Dict]:
        """List all channels."""
        response = self.client.conversations_list(types="public_channel,private_channel")
        return response["channels"]

# Default instance
slack_service = SlackService()