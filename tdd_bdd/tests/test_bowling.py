from bowling import Game
import unittest

class BowlingTest(unittest.TestCase):
    def setUp(self):
        print('\nTest Pre-Setup: Initialize Game object')
        self.game = Game()
        
    def test_scoreboard_frames(self):
        self.assertEqual(len(self.game.scoreboard.frames), 10)
        
    def test_frame_rolls(self):
        self.assertEqual(self.game.scoreboard.frames[0].roll_one, -1)
        self.assertEqual(self.game.scoreboard.frames[0].roll_two, -1)

    def test_one_pin(self):
        self.game.roll(1)
        self.assertEqual(self.game.score(), None)
    
    def test_five_two_pins(self):
        self.game.roll(5)
        self.game.roll(2)
        self.assertEqual(self.game.score(), 7)
        
    def test_second_frame(self):
        self.game.roll(5)
        self.game.roll(2)
        
        self.game.roll(4)
        self.game.roll(5)
        self.assertEqual(self.game.score(), 16)
        
    def test_first_spare(self):
        self.game.roll(9)
        self.game.roll(1)
        
        self.game.roll(5)
        self.game.roll(4)
        self.assertEqual(self.game.score(), 24)
        
    def test_first_strike(self):
        self.game.roll(10)
        
        self.game.roll(5)
        self.game.roll(4)
        self.assertEqual(self.game.score(), 28)
        