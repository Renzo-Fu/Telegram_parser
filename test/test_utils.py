from types import SimpleNamespace
from src.utils import serialize_entities

# In process


def test_serialize_entities():
    entity = SimpleNamespace(type="url", offset=0,
                             length=10, url="https://example.com")
    entities = [entity]

    result = serialize_entities(entities)
    expected_result = '[{"type": "SimpleNamespace", "offset": 0, "length": 10, "url": "https://example.com"}]'
    assert result == expected_result
