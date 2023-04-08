import unittest

from room_game import Item


class TestItem(unittest.TestCase):

    def test_init(self):
        item = Item("Test Item", "This is a test item.")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.description, "This is a test item.")


if __name__ == '__main__':
    unittest.main()
