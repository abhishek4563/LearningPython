import unittest 
import cap

class TestCap(unittest.TestCase): # inherit from unittest class
	def test_one_word(self):
		r = cap.cap('name') # run the function
		self.assertEqual(r,'Name') # compare the outputs using assertEqual method inherited from unittest
	def test_two_words(self):
		r = cap.cap('no name')
		self.assertEqual(r,'No Name')

if __name__ == '__main__':
	unittest.main() # run the main function of unittest 
