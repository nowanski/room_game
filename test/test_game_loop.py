import io
import unittest
from unittest import skip
from unittest.mock import patch
from room_game import game_loop, world

@skip("Skip test_game_loop")
class TestGameLoop(unittest.TestCase):

    def test_game_loop(self):
        # Redirect stdout to capture output
        with io.StringIO() as output:
            with patch('sys.stdout', new=output):
                # Simulate user inputs
                inputs = ['move', 'right', 'move', 'up', 'move', 'down', 'item', 'take', 'torch', 'item', 'use', 'torch', 'move', 'right', 'move', 'right', 'move', 'up', 'move', 'down', 'item', 'take', 'sword', 'item', 'use', 'sword', 'move', 'down', 'move', 'right', 'move', 'right', 'move', 'up', 'move', 'down', 'item', 'take', 'key', 'move', 'left', 'item', 'use', 'key', 'move', 'right', 'move', 'up', 'move', 'down', 'move', 'right', 'move', 'right']
                with patch('builtins.input', side_effect=inputs):
                    game_loop()
                output_str = output.getvalue().strip()
                # Check if the game output is as expected
                self.assertIn("Welcome to the game!", output_str)
                self.assertIn("You are in the Room 1.", output_str)
                self.assertIn("This is room 1.", output_str)
                self.assertIn("Exits:", output_str)
                self.assertIn("right - Room 2", output_str)
                self.assertIn("Items:", output_str)
                self.assertIn("Torch - A torch to light your way.", output_str)
                self.assertIn("Characters:", output_str)
                self.assertIn("Guard - A guard blocking your path.", output_str)
                self.assertIn("Actions:", output_str)
                self.assertIn("move", output_str)
                self.assertIn("item", output_str)
                self.assertIn("help", output_str)
                self.assertIn("quit", output_str)
                self.assertIn("What would you like to do?", output_str)