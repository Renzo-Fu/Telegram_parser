# **Telegram Parser**

This is a test parser for extracting Telegram messages and saving them to a CSV file using the library **Telethon**.

## **Features**
- **Multi-Channel Support**:  
  You can specify multiple Telegram channels in the `.env` file, and the parser will scrape messages from all the channels.

- **Periodic Dataset Updates**:  
  The script stores the ID of the last scraped message for each channel, so subsequent scrapes will only retrieve new messages.

- **Custom CSV Output**:  
  The data is exported into a CSV file with specific columns, including the name of the channel (`Название источника`) and the message link (`Источник`).

## **Setup**

### **Requirements**
- `Telethon`
- `python-dotenv`

### **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/telegram-parser.git
    cd telegram-parser
    ```

2. **Install Poetry**:
    ```bash
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    poetry --version
    ```

3. **Install Project Dependencies**:
    ```bash
    poetry install
    ```

4. **Set Up Environment Variables**:
    The project uses environment variables to store sensitive information like your Telegram API credentials. You need to create a `.env` file at the root of the project directory.

    - **4.1. Create a `.env` file**:
        ```bash
        touch .env
        ```

    - **4.2. Add your Telegram API credentials and channel names to the `.env` file**:
        ```plaintext
        TELEGRAM_API_ID=your_telegram_api_id
        TELEGRAM_API_HASH=your_telegram_api_hash
        TELEGRAM_CHANNELS=channel_1,channel_2,channel_3
        PHOTO=true
        VIDEO=true
        PDF=true
        ```

    Replace with your actual Telegram credentials and channel names.
    Adjust PHOTO, VIDEO, and PDF as needed.

    - **To obtain your API ID and Hash**, visit [my.telegram.org](https://my.telegram.org) and create an application.

6. **Running the Code**:

    - **5.1. Activate the virtual environment created by Poetry**:
        ```bash
        poetry shell
        ```

    - **5.2. Run the script to start fetching messages from Telegram**:
        ```bash
        poetry run python src/parser.py
        ```
    - **5.3 During execution, you will be prompted to enter your phone number (or bot token):**:
        ```bash
        Scraping messages for Channel_1...
        Please enter your phone (or bot token):
        ```
        Enter your phone number or bot token as instructed.
      
    - **5.3 After entering your phone number or bot token**
            You will receive a code sent to Telegram. Enter this code when prompted to continue the execution.
      
      
7. **Output**:
    - **6.1 Example output**:
        ```bash
        Scraping messages for channel_1...
        Scraping messages for channel_2...
        ```
    After running the script, the extracted messages will be saved in a CSV file located at `data/collected_data.csv`. The file will include details like message text, URLs, message date, and message links.
    - **6.1 Example output**:
        All scraped media data will be stored in the data folder. Each type of data (videos, PDFs, photos) will be saved in its respective folder within data.
