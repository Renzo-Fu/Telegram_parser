from telegram_client import get_telegram_messages
from cvs_writer import write_csv
from utils import measure_time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


@measure_time
def main():
    channel_name = os.getenv("TELEGRAM_CHANNEL")
    limit = 1500

    csv_file = "data/collected_data.csv"

    messages = get_telegram_messages(channel_name, limit)

    write_csv(csv_file, messages)


if __name__ == "__main__":
    main()
