# Telegram Parser

This is a test parser for extracting Telegram messages and saving them to a CSV file using the library Telethon.
## Update
- The `save_media` function now identifies and processes different media types, for now just works with photos and pdfs:
     - **Photos**: Files are saved with a `.jpg` extension.
     - **Documents**: Files are saved with the extension specified in the document’s attributes. If the file name is not available, it defaults to `.jpg`.
## Features
- Fetch messages from a Telegram channel.
- Extract URLs from message entities.
- Save extracted data to a CSV file with organized columns.

## Setup

### Requirements
- Telethon
- python-dotenv

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/telegram-parser.git
cd telegram-parser
```
2. Install Poetry:
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
poetry --version
```
3. Install Project Dependencies:
```bash
poetry install
```

4. Set Up Environment Variables:
The project uses environment variables to store sensitive information like your Telegram API credentials. You need to create a \`.env\` file at the root of the project directory.

4.1. Create a \`.env\` file:

```bash
touch .env
```

4.2. Add your Telegram API credentials and channel name to the \`.env\` file:

```
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
TELEGRAM_CHANNEL=your_telegram_channel_name
```

Replace \`your_telegram_api_id\`, \`your_telegram_api_hash\`, and \`your_telegram_channel_name\` with your actual Telegram credentials and channel name.

- **To obtain your API ID and Hash**, visit [my.telegram.org](https://my.telegram.org) and create an application.

5. Running the Code:

5.1. Activate the virtual environment created by Poetry:

```bash
poetry shell
```

5.2. Run the script to start fetching messages from Telegram:

```bash
poetry run python src/parser.py
```

6. Output:
After running the script, the extracted messages will be saved in a CSV file located at \`data/collected_data.csv\`. The file will include details like message text, URLs, message date, and message links.
