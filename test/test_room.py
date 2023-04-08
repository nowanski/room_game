import unittest
from unittest.mock import MagicMock

from room_game import Room, Item, Character


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Test Room", "This is a test room.")

    def test_add_item(self):
        item = MagicMock()
        self.room.add_item(item)
        self.assertIn(item, self.room.items)

    def test_remove_item(self):
        item = MagicMock()
        self.room.add_item(item)
        self.room.remove_item(item)
        self.assertNotIn(item, self.room.items)

    def test_add_exit(self):
        room2 = MagicMock()
        self.room.add_exit("north", room2)
        self.assertIn("north", self.room.exits)
        self.assertEqual(self.room.exits["north"], room2)

    def test_add_character(self):
        character = MagicMock()
        self.room.add_character(character)
        self.assertIn(character, self.room.characters)

    def test_remove_character(self):
        character = MagicMock()
        self.room.add_character(character)
        self.room.remove_character(character)
        self.assertNotIn(character, self.room.characters)

    def test_search_item(self):
        item1 = Item("Item 1", "This is item 1.")
        item2 = Item("Item 2", "This is item 2.")
        self.room.add_item(item1)
        self.room.add_item(item2)
        self.assertEqual(self.room.search_item("Item 1"), item1)
        self.assertEqual(self.room.search_item("Item 2"), item2)
        self.assertIsNone(self.room.search_item("Item 3"))

    def test_room(slef):
        room = Room("test room", "this is a test room")

        assert room.name == "test room"
        assert room.description == "this is a test room"
        assert room.items == []
        assert room.exits == {}
        assert room.characters == []
        assert room.is_light == True
        assert room.is_open == True

        room.toggle_light()
        assert room.is_light == False

        room.turn_on_light()
        assert room.is_light == True

        room.open_door()
        assert room.is_open == True

        room.close_door()
        assert room.is_open == False

        item = Item("test item", "this is a test item")
        room.add_item(item)
        assert len(room.items) == 1
        assert room.items[0] == item

        exit_room = Room("exit room", "this is the exit room")
        room.add_exit("north", exit_room)
        assert "north" in room.exits
        assert room.exits["north"] == exit_room

        character = Character("test character", "this is a test character")
        room.add_character(character)
        assert len(room.characters) == 1
        assert room.characters[0] == character

        item2 = Item("test item 2", "this is another test item")
        room.add_item(item2)
        assert len(room.items) == 2

        removed_item = room.remove_item(item)
        assert len(room.items) == 1
        assert removed_item == item

        room.remove_character(character)
        assert len(room.characters) == 0

        searched_item = room.search_item("test item 2")
        assert searched_item == item2

        searched_item = room.search_item("nonexistent item")
        assert searched_item == None
