import json
import time
import os


def serialize_entities(entities):
    """
    Serializes message entities into a JSON format.

    Args:
        entities (list): List of message entities.

    Returns:
        str: A JSON string of serialized entities.
    """
    if not entities:
        return ""
    serializable_entities = []
    for entity in entities:
        entity_dict = {
            "type": str(entity.__class__.__name__),
            "offset": entity.offset,
            "length": entity.length,
            "url": entity.url if hasattr(entity, 'url') else None
        }
        serializable_entities.append(entity_dict)
    return json.dumps(serializable_entities, ensure_ascii=False)


def extract_urls_from_serialized_entities(serialized_entities):
    """
    Extracts URLs from serialized message entities.

    Args:
        serialized_entities (str): A JSON string of serialized entities.

    Returns:
        list: A list of URLs found in the entities.
    """
    urls = []
    if serialized_entities:
        entities = json.loads(serialized_entities)
        urls = [entity["url"] for entity in entities if entity.get("url")]
    return urls


def measure_time(func):
    """
    Decorator to measure the execution time of functions.

    Args:
        func (function): The function to be measured.

    Returns:
        function: The wrapped function with timing.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper


def load_last_scraped_ids():
    """
    Loads the last scraped message IDs for each channel from a JSON file.

    Returns:
        dict: A dictionary mapping channel names to their last scraped message ID.
    """
    if os.path.exists('data/last_scraped_ids.json'):
        with open('data/last_scraped_ids.json', 'r') as file:
            return json.load(file)
    return {}


def save_last_scraped_ids(last_scraped_ids):
    """
    Saves the last scraped message IDs for each channel to a JSON file.

    Args:
        last_scraped_ids (dict): A dictionary mapping channel names to their last scraped message ID.
    """
    with open('data/last_scraped_ids.json', 'w') as file:
        json.dump(last_scraped_ids, file)
