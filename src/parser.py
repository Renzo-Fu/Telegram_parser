from telegram_client import get_telegram_messages
from cvs_writer import write_csv
from utils import measure_time, load_last_scraped_ids, save_last_scraped_ids
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


@measure_time
def main():
    """
    Main function to scrape messages from multiple Telegram channels.
    Scrapes only new messages since the last scrape for each channel.
    """
    channels = os.getenv("TELEGRAM_CHANNEL")
    limit = 1500
    csv_file = "data/collected_data.csv"

    # Load last scraped message IDs for all channels
    last_scraped_ids = load_last_scraped_ids()

    for channel in channels:
        print(f"Scraping messages for {channel.strip()}...")

        # Fetch new messages from the channel
        messages = get_telegram_messages(
            channel.strip(), limit, last_scraped_ids.get(channel.strip()))

        if messages:
            # Update the last scraped message ID for this channel
            last_scraped_ids[channel.strip()] = messages[0].id

            # Write messages to CSV and include the channel name
            write_csv(csv_file, messages, channel.strip())

    # Save the last scraped message IDs
    save_last_scraped_ids(last_scraped_ids)


if __name__ == "__main__":
    main()
