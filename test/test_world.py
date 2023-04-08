import unittest
from room_game import Room, Item, Character, world


class TestWorld(unittest.TestCase):
    def test_world(self):
        # create the world
        room1 = Room("Room 1", "This is room 1.")
        room2 = Room("Room 2", "This is room 2.")
        room2.is_light = False
        room3 = Room("Room 3", "This is room 3.")
        room3.close_door()
        room4 = Room("Room 4", "This is room 4.")
        room5 = Room("Room 5", "This is room 5.")

        item_key = Item("Key", "A key unlocks a door.")
        item_torch = Item("Torch", "A torch to light your way.")
        item_sword = Item("Sword", "A sword to fight with.")

        character_guard = Character("Guard", "A guard blocking your path.")

        room1.add_exit("right", room2)
        room2.add_exit("left", room1)
        room2.add_exit("up", room3)
        room3.add_exit("down", room2)
        room3.add_exit("right", room4)
        room4.add_exit("left", room3)
        room4.add_exit("up", room5)
        room5.add_exit("down", room4)

        room1.add_item(item_torch)
        room4.add_character(character_guard)
        room2.add_item(item_key)
        room3.add_item(item_sword)



        # call the world function and compare the resulting room with the expected value
        world = self.run_world()
        assert room1.name == world.name
        assert room1.name == "Room 1"

        # assert all rooms' exits are correct
        assert room1.exits["right"] == room2
        assert room2.exits["left"] == room1
        assert room2.exits["up"] == room3
        assert room3.exits["down"] == room2
        assert room3.exits["right"] == room4
        assert room4.exits["left"] == room3
        assert room4.exits["up"] == room5
        assert room5.exits["down"] == room4

        # assert all rooms' items are correct
        assert room1.items[0] == item_torch
        assert room2.items[0] == item_key
        assert room3.items[0] == item_sword

        # assert all rooms' characters are correct
        assert room4.characters[0] == character_guard


    def run_world(self):
        return world()


if __name__ == '__main__':
    unittest.main()
