import unittest
from unittest.mock import MagicMock

from room_game import Inventory, Item


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()

    def test_add_item(self):
        item = MagicMock()
        self.inventory.add_item(item)
        self.assertIn(item, self.inventory.items)

    def test_remove_item(self):
        item = MagicMock()
        self.inventory.add_item(item)
        self.inventory.remove_item(item)
        self.assertNotIn(item, self.inventory.items)

    def test_search_item(self):
        item1 = Item("Item 1", "This is item 1.")
        item2 = Item("Item 2", "This is item 2.")
        self.inventory.add_item(item1)
        self.inventory.add_item(item2)
        self.assertEqual(self.inventory.search_item("Item 1"), item1)
        self.assertEqual(self.inventory.search_item("Item 2"), item2)
        self.assertIsNone(self.inventory.search_item("Item 3"))


if __name__ == '__main__':
    unittest.main()
