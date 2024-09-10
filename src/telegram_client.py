from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")


def get_telegram_messages(channel_name, limit):
    """
    Fetches messages from a given Telegram channel.

    Args:
        channel_name (str): The username or ID of the Telegram channel.
        limit (int): The maximum number of messages to retrieve.

    Returns:
        list: A list of Telegram messages.
    """
    with TelegramClient("my_account", api_id, api_hash) as client:
        channel = client.get_entity(channel_name)
        history = list(client.iter_messages(channel, limit=limit))
        return history
