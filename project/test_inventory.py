import pytest
from inventory import Inventory

def test_add_item():
    inv = Inventory()
    inv.add_item("Pensil", 10)
    assert inv.get_quantity("Pensil") == 10

def test_get_quantity_nonexistent():
    inv = Inventory()
    assert inv.get_quantity("Pulpen") == 0

def test_remove_item_success():
    inv = Inventory()
    inv.add_item("Buku", 5)
    result = inv.remove_item("Buku", 3)
    assert result is True
    assert inv.get_quantity("Buku") == 2

def test_integration_add_and_remove():
    inv = Inventory()
    inv.add_item("Kertas", 100)
    inv.remove_item("Kertas", 30)
    inv.add_item("Kertas", 20)
    assert inv.get_quantity("Kertas") == 90
