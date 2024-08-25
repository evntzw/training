from fizzbuzz import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_number(self):
        self.assertEquals(fizzbuzz(1), 1)
        
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
