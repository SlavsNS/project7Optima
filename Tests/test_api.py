import pytest
from Infra.api import GenshinAPI

def test_fetch_characters():
    data = GenshinAPI.fetch_characters()
    assert isinstance(data, list)
    assert len(data) > 0

def test_fetch_weapons():
    data = GenshinAPI.fetch_weapons()
    assert isinstance(data, list)
    assert len(data) > 0
