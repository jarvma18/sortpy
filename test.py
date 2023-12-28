import unittest
from main import sortLexiographically
from main import readFile

class TestClass(unittest.TestCase):
  def test_readFile(self):
    testFile = 'short-text.txt'
    expectedValue = 'Short text'
    self.assertEqual(expectedValue, readFile(testFile))

  def test_sortLexiographically(self):
    testData = 'a\nb\nc'
    expectedValue = ['a', 'b', 'c']
    self.assertEqual(expectedValue, sortLexiographically(testData))