from fizzbuzz import fizzbuzz
import unittest

class FizzBussTest(unittest.TestCase):
    def testFizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        
    def testBuzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        
    def testFizzBuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
