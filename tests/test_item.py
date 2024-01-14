"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_init():
    return Item("iphone14_plus", 78000, 10)


def test_first(item_init):
    assert 78000 * 10 == item_init.calculate_total_price()

    Item.pay_rate = 0.8
    item_init.apply_discount()
    assert item_init.price == 78000 * 0.8
