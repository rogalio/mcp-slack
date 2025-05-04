# core/config.py
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Settings:
    """Application configuration loaded from environment variables."""
    slack_token: Optional[str] = None
    slack_user_token: Optional[str] = None

    def __init__(self):
        self.slack_user_token = os.getenv("SLACK_USER_TOKEN")

        if not self.slack_user_token:
            print("Warning: SLACK_USER_TOKEN environment variable not set.")

        # Keep this in case it's still used elsewhere
        if not self.slack_token:
            print("Warning: SLACK_BOT_TOKEN environment variable not set.")

# Singleton instance
_settings = None

def get_settings() -> Settings:
    """Get the application settings singleton."""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings