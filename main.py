import sys

def printWordsFromArray(words):
  for i in words:
    print(i)
  return

def sortLexiographically(contentToSort):
  sortedContent = contentToSort.split('\n')
  sortedContent.sort()
  return sortedContent

def readFile(fileName):
  file = open(fileName, 'r')
  fileContent = file.read()
  file.close()
  return fileContent

rawFileContent = readFile(sys.argv[1])
sortedFileContent = sortLexiographically(rawFileContent)
printWordsFromArray(sortedFileContent)