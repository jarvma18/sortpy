import unittest
from main import sortLexiographically
from main import readFile
from main import readFileAndSortContent

class TestClass(unittest.TestCase):
  def test_readFile(self):
    testFile = 'test-materials/short-text.txt'
    expectedValue = 'Short text'
    self.assertEqual(expectedValue, readFile(testFile))

  def test_sortLexiographically(self):
    testData = 'a\nb\nc'
    expectedValue = ['a', 'b', 'c']
    self.assertEqual(expectedValue, sortLexiographically(testData))

  def test_readFileAndSortContent(self):
    testFile = 'test-materials/short-words.txt'
    expectedValue = ['a', 'b', 'c', 'd', 'e']
    self.assertEqual(expectedValue, readFileAndSortContent(testFile))