import unittest

from room_game import Character


class TestCharacter(unittest.TestCase):

    def test_init(self):
        character = Character("Test Character", "This is a test character.")
        self.assertEqual(character.name, "Test Character")
        self.assertEqual(character.description, "This is a test character.")


if __name__ == '__main__':
    unittest.main()
