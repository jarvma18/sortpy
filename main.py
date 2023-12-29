import sys

def printWordsFromArray(words):
  for i in words:
    print(i)
  return

def sortLexiographically(contentToSort):
  contentToSort.sort()
  return contentToSort

def clearDuplicatedWords(contentToClear):
  listOfUniqueWords = []
  for i in contentToClear:
    if i not in listOfUniqueWords:
      listOfUniqueWords.append(i)
  return listOfUniqueWords

def splitWordsToArray(contentToSplit):
  splittedContent = contentToSplit.split('\n')
  return splittedContent

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

def readFileAndSortContent(fileName, isUnique):
  fileContent = readFile(fileName)
  fileContentArray = splitWordsToArray(fileContent)
  if (isUnique):
    fileContentArray = clearDuplicatedWords(fileContentArray)
  sortedFileContent = sortLexiographically(fileContentArray)
  return sortedFileContent;

def checkArgumentLen(arguments):
  if len(arguments) < 2:
    raise Exception('Too few arguments, provide at least file name')
  else:
    return

def readPassedArguments(arguments):
  lastArgument = arguments[len(arguments) - 1]
  argumentObject = {
    'fileName': lastArgument,
    'isUnique': False
  }
  for i in arguments:
    if i == '-u':
      argumentObject['isUnique'] = True
  return argumentObject

checkArgumentLen(sys.argv)
arguments = readPassedArguments(sys.argv)
fileName = arguments['fileName']
isUnique = arguments['isUnique']
sortedContent = readFileAndSortContent(fileName, isUnique)
printWordsFromArray(sortedContent)

