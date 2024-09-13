from telethon.sync import TelegramClient
from telethon.tl.types import DocumentAttributeFilename
from dotenv import load_dotenv
import os
from pathlib import Path
from telethon import types
# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")


def get_telegram_messages(channel_name: str, limit: int, last_scraped_id: int = None,
                          photo_scrape: bool = False, video_scrape: bool = False, pdf_scrape: bool = False):
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
        last_scraped_id = last_scraped_id or 0
        messages = list(client.iter_messages(
            channel, limit=limit, min_id=last_scraped_id))

        if photo_scrape or video_scrape or pdf_scrape:
            for message in messages:
                if message.media:
                    file_path = None

                    if photo_scrape and message.photo:
                        file_path = save_media(
                            client, message.photo, 'photos', message.id)
                    elif video_scrape and message.video:
                        file_path = save_media(
                            client, message.video, 'videos', message.id)
                    elif pdf_scrape and isinstance(message.media, types.MessageMediaDocument):
                        if message.document.mime_type == 'application/pdf':
                            print(
                                f"Parsing PDF from message {message.id} with filename: {message.document.attributes[0].file_name}")
                            file_path = save_media(
                                client, message.document, 'pdfs', message.id)

                    if file_path:
                        # Add file path information to message (if necessary)
                        message.file_path = file_path

        return messages


def save_media(client: TelegramClient, media, folder: str, message_id: int):
    """
    Saves media files to a specified folder.

    Args:
        client (TelegramClient): The Telegram client instance.
        media (Media): The media object to be saved.
        folder (str): The folder where media will be saved.
        message_id (int): The ID of the message containing the media.

    Returns:
        str: The relative path of the saved media file.
    """
    folder_path = Path(f'data/{folder}')
    folder_path.mkdir(parents=True, exist_ok=True)

    # Determine file name based on media type
    if isinstance(media, types.Photo):
        print('is determining fotos')
        file_name = f'{message_id}.jpg'
    elif isinstance(media, types.Document):
        print('is determining pdfs')
        file_name = next(
            (attr.file_name for attr in media.attributes if isinstance(
                attr, types.DocumentAttributeFilename)),
            f'{message_id}.jpg'
        )
    else:
        file_name = f'{message_id}.jpg'

    # Save media
    file_path = folder_path / file_name
    client.download_media(media, file_path)

    return str(file_path.relative_to(Path('data')))
