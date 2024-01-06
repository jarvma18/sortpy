import sys

def printWordsFromArray(words: list):
  for i in words:
    print(i)
  return

def lexicographicSort(words: list): # Todo. Make it faster?
  lenOfWords = len(words)
  for i in range(lenOfWords):
    for j in range(0, lenOfWords - i - 1):
      if words[j].lower() > words[j + 1].lower():
        words[j], words[j+1] = words[j+1], words[j]
  return words

def lexicographicSortOnCharacter(words: list, index: int):
  lenOfWords = len(words)
  for i in range(lenOfWords):
    for j in range(0, lenOfWords - i - 1):
      if words[j][index].lower() > words[j + 1][index].lower():
        words[j], words[j+1] = words[j+1], words[j]
  return words

def radixSort(words: list):
  # order words by the leftmost character (most significant)
  words: list = lexicographicSortOnCharacter(words, 0)
  buckets: list = []
  # let's order words to bucket by 1st character:
  for i in range (len(words)):
    # foundBucket variable so we know if there even were bucket
    foundBucket = False
    if len(buckets) == 0:
      buckets.append([])
      buckets[0].append(words[i])
      foundBucket = True
    if (foundBucket):
      continue
    for j in range(len(buckets)):
      if words[i][0].lower() == buckets[j][0][0].lower():
        buckets[j].append(words[i])
        foundBucket = True
    if (foundBucket):
      continue
    else:
      buckets.append([words[i]])
  # todo: if bucket len is 1 no need for sorting
  # if the characters in buckets in certain index are all different
  # then I think that there is no need to sort anything in that
  # bucket, create function that could be called recursively
  return buckets

def clearDuplicatedWords(words: list):
  listOfUniqueWords: list = []
  for i in words:
    if i not in listOfUniqueWords:
      listOfUniqueWords.append(i)
  return listOfUniqueWords

def splitWordsToArray(words: str):
  splittedContent: list = words.split('\n')
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

def readFileAndSortWords(fileName: str, isUnique: bool):
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
sortedWords: list = readFileAndSortWords(fileName, isUnique)
printWordsFromArray(sortedWords)