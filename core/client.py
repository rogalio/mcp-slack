from typing import Optional
from slack_sdk import WebClient
from core.config import get_settings

class ApiClient:
    """Base manager for API clients."""
    pass

class SlackClient(ApiClient):
    """Slack API client provider."""

    @staticmethod
    def create() -> Optional[WebClient]:
        """Create client from environment settings."""
        settings = get_settings()
        if settings.slack_user_token:
            return WebClient(token=settings.slack_user_token)
        return None

    @staticmethod
    def get_default() -> WebClient:
        """Get default client or raise error if unavailable."""
        client = SlackClient.create()
        if not client:
            raise ValueError("Slack client initialization failed - token missing")
        return client