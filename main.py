import sys

def printWordsFromArray(words):
  for i in words:
    print(i)
  return

def sortLexiographically(contentToSort):
  sortedContent = contentToSort.split('\n')
  sortedContent.sort()
  return sortedContent

def openFile(fileName):
  try:
    file = open(fileName, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def readFile(fileName):
  file = openFile(fileName)
  if file:
    fileContent = file.read()
    file.close()
    return fileContent
  else:
    return

def readFileAndSortContent(fileName):
  rawFileContent = readFile(fileName)
  sortedFileContent = sortLexiographically(rawFileContent)
  return sortedFileContent;

def readPassedArguments(arguments):
  if len(arguments) < 2:
    raise Exception('Too few arguments, provide at least file name')
  lastArgument = arguments[len(arguments) - 1]
  argumentObject = {
    'fileName': lastArgument,
    'unique': False
  }
  for i in arguments:
    if i == '-u':
      argumentObject['unique'] = True
  return argumentObject

sortedContent = readFileAndSortContent(sys.argv[1])
printWordsFromArray(sortedContent)

