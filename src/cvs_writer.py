import csv
from utils import serialize_entities, extract_urls_from_serialized_entities
import os
from pathlib import Path


def write_csv(csv_file, messages):
    """
    Writes a list of Telegram messages to a CSV file.

    Args:
        csv_file (str): The file path for the CSV file.
        messages (list): A list of Telegram messages to be written.

    Returns:
        None
    """

    output_dir = Path(os.path.dirname(csv_file))
    output_dir.mkdir(parents=True, exist_ok=True)

    headers = ["CPC Дерево", "Ключевые слова", "Краткое описание идеи/продукта",
               "Длинное описание идеи/продукта", "Компания", "Личности (если есть)",
               "Какой потенциал проекта? Для чего он может быть применим? в чем польза?",
               "Тип источника", "Ссылки", "Дата поста", "Текст сообщения", "Ссылка на сообщение"]

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for message in messages:
            message_content = message.message  # Telethon uses `message` for text/caption
            serialized_entities = serialize_entities(message.entities)
            urls = extract_urls_from_serialized_entities(serialized_entities)
            message_link = f"https://t.me/{message.chat.username}/{message.id}"

            # Write the message data to the CSV file
            writer.writerow([
                "",  # Placeholder for CPC Дерево
                "",  # Placeholder for Ключевые слова
                "",  # Placeholder for Краткое описание идеи/продукта
                "",  # Placeholder for Длинное описание идеи/продукта
                "",  # Placeholder for Компания
                "",  # Placeholder for Личности (если есть)
                "",  # Placeholder for Какой потенциал проекта
                "TG",  # Тип источника
                ', '.join(urls),  # Links found in message entities
                # Date without timezone info
                message.date.replace(tzinfo=None),
                message_content,  # Message text/caption
                message_link  # Message link
            ])
