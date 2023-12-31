import sys

def printWordsFromArray(words: list):
  for i in words:
    print(i)
  return

def createRadixBuckets(contentToCreateBucketsWith: list):
  mostSignificants: list = []
  buckets: dict = {}
  for i in contentToCreateBucketsWith:
    if i[0] not in mostSignificants:
      mostSignificants.append(i[0])
      buckets[i[0]] = []
    buckets[i[0]].append(i)
  mostSignificants.sort()
  buckets['sortedMostSignificants'] = mostSignificants
  return buckets;

def radixSort(contentToSort: list):
  placeholder = 1

def lexicographicSort(contentToSort: list):
  for i in range(len(contentToSort)):
    valueToCompare = contentToSort[i]
    for j in range(len(contentToSort)):
      if (j == i):
        continue
      valueToCompareWith = contentToSort[j]
      # print(valueToCompare, valueToCompareWith)
      if (valueToCompare.lower() == valueToCompareWith.lower()):
        contentToSort[i] = valueToCompareWith
        contentToSort[j] = valueToCompare
        i = 0
        break;
      elif (valueToCompare.lower() > valueToCompareWith.lower()):
        contentToSort[i] = valueToCompareWith
        contentToSort[j] = valueToCompare
        i = 0
        break;
  return contentToSort

def clearDuplicatedWords(contentToClear: list):
  listOfUniqueWords: list = []
  for i in contentToClear:
    if i not in listOfUniqueWords:
      listOfUniqueWords.append(i)
  return listOfUniqueWords

def splitWordsToArray(contentToSplit: str):
  splittedContent: list = contentToSplit.split('\n')
  return splittedContent

def openFile(fileName: str):
  try:
    file = open(fileName, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def readFile(fileName: str):
  file = openFile(fileName)
  if file:
    fileContent: str = file.read()
    file.close()
    return fileContent
  else:
    return

def readFileAndSortContent(fileName: str, isUnique: bool):
  fileContent: str = readFile(fileName)
  fileContentArray: list = splitWordsToArray(fileContent)
  if (isUnique):
    fileContentArray: list = clearDuplicatedWords(fileContentArray)
  sortedFileContent: list = lexicographicSort(fileContentArray)
  return sortedFileContent;

def checkArgumentLen(arguments: list):
  if len(arguments) < 2:
    raise Exception('Too few arguments, provide at least file name')
  else:
    return

def readPassedArguments(arguments: list):
  lastArgument: str = arguments[len(arguments) - 1]
  argumentObject: dict = {
    'fileName': lastArgument,
    'isUnique': False
  }
  for i in arguments:
    if i == '-u':
      argumentObject['isUnique'] = True
  return argumentObject

checkArgumentLen(sys.argv)
arguments: dict = readPassedArguments(sys.argv)
fileName: str = arguments['fileName']
isUnique: bool = arguments['isUnique']
sortedContent: list = readFileAndSortContent(fileName, isUnique)
printWordsFromArray(sortedContent)

