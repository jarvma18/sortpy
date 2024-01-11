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

def lexicographicSortOnChar(words: list, index: int):
  lenOfWords = len(words)
  for i in range(lenOfWords):
    for j in range(0, lenOfWords - i - 1):
      if words[j][index].lower() > words[j + 1][index].lower():
        words[j], words[j+1] = words[j+1], words[j]
  return words

def flatten(array: list):
  result = []
  for i in array:
    if isinstance(i, list):
      result.extend(flatten(i))
    else:
      result.append(i)
  return result

def createBuckets(words, index):
  buckets: list = []
  for i in range(len(words)):
    foundBucket: bool = False
    if len(buckets) == 0:
      buckets.append([])
      buckets[0].append(words[i])
      foundBucket: bool = True
    if (foundBucket):
      continue
    for j in range(len(buckets)):
      if words[i][index].lower() == buckets[j][0][index].lower():
        buckets[j].append(words[i])
        foundBucket: bool = True
    if (foundBucket):
      continue
    else:
      buckets.append([words[i]])
  return buckets

def radixBucketSort(words: list, maxLen: int, index: int, lexAndReturn: bool):
  # early return if there is nothing to sort
  if len(words) < 2:
    return words
  # sort lexicographically based on the next character
  words: list = lexicographicSortOnChar(words, index + 1)
  # if there is nothing to sort, return after lexicographic sort
  if lexAndReturn:
    return words
  buckets = createBuckets(words, index)
  nothingToSort: bool = False
  if len(buckets) == 1:
    nothingToSort: bool = True
  for i in range(len(buckets)):
    buckets[i]: list = lexicographicSortOnChar(buckets[i], index)
  # This means that there is more to sort and not just one same char
  sortedBuckets: list = []
  if index == maxLen:
    return buckets;
  else:
    for i in range(len(buckets)):
      sortedBuckets.append(radixBucketSort(buckets[i], maxLen, index + 1, nothingToSort))
  return sortedBuckets

def radixSort(words: list):
  # order words by the leftmost character (most significant)
  words: list = lexicographicSortOnChar(words, 0)
  # let's order words to buckets by 1st character:
  buckets = createBuckets(words, 0)
  sortedBuckets: list = []
  for i in range(len(buckets)):
    maxLen: int = max(buckets[i], key=len)
    sortedBuckets.append(radixBucketSort(buckets[i], maxLen, 1, False))
  sortedWords = flatten(sortedBuckets)
  return sortedWords

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