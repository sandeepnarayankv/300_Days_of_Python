from random import randint
import unittest
import main


class TestClass(unittest.TestCase):
    def setUp(self):
        self.answer = randint(1, 10)
        print('Run Setup')
    
    def test_correct_guess(self):
        result = main.check_guess(self.answer, self.answer)
        self.assertTrue(result)
    
    def testWrongGuess(self):
        while True:
            guess = randint(1,10)
            if guess != self.answer:
                break 
        result = main.check_guess(self.answer, guess)
        self.assertFalse(result)

    def testGreaterInput(self):
        guess = 25
        result = main.check_guess(self.answer, guess)
        self.assertEqual(result, 'Please Enter a Number between 1~10')

    def testLessInput(self):
        guess = 0
        result = main.check_guess(self.answer, guess)
        self.assertEqual(result, 'Please Enter a Number between 1~10')

    def testStrInput(self):
        guess = 'Hello'
        result = main.check_guess(self.answer, guess)
        self.assertIsInstance(result, TypeError)

print(__name__)
if __name__ == '__main__':
    unittest.main()