import unittest
import io
import sys
from main import sortLexiographically
from main import readFile
from main import readFileAndSortContent
from main import openFile
from main import printWordsFromArray

class TestClass(unittest.TestCase):
  # Prints can be tested with io and sys
  def test_printWordsFromArray(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    testData = ['a', 'b', 'c', 'd', 'e']
    expectedValue = 'a\nb\nc\nd\ne\n'
    printWordsFromArray(testData)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_openNotExistingFile(self):
    expectionMessage = 'File not found, check that the file exists in that path'
    testFile = 'test-materials/this-file-should-not-exist.txt'
    with self.assertRaises(Exception) as context:
      openFile(testFile)
    self.assertTrue(expectionMessage in str(context.exception))

  # Here we also test that the file is opened and can be read
  def test_readFile(self):
    testFile = 'test-materials/short-text.txt'
    expectedValue = 'Short text'
    self.assertEqual(expectedValue, readFile(testFile))

  def test_sortLexiographically(self):
    testData = 'a\nb\nc\nd\ne'
    expectedValue = ['a', 'b', 'c', 'd', 'e']
    self.assertEqual(expectedValue, sortLexiographically(testData))

  def test_readFileAndSortContent(self):
    testFile = 'test-materials/short-words.txt'
    expectedValue = ['a', 'b', 'c', 'd', 'e']
    self.assertEqual(expectedValue, readFileAndSortContent(testFile))