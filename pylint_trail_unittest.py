import unittest
import pylint_trail

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text ='python'
        result = pylint_trail.capText(text)
        self.assertEqual(result,'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = pylint_trail.capText(text)
        self.assertEqual(result,'Monty Python')

if __name__=="__main__":
    unittest.main()


