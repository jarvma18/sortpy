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

def radixBucketSort(words: list, maxLen: int, index: int):
  buckets: list = []
  # early return if there is nothing to sort
  if len(words) < 2:
    return words
  words: list = lexicographicSortOnChar(words, index + 1)
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
  for i in range(len(buckets)):
    buckets[i]: list = lexicographicSortOnChar(buckets[i], index)
  # This means that there is more to sort and not just one same char
  sortedBuckets: list = []
  print(buckets)
  if index == maxLen:
    return buckets;
  else:
    for i in range(len(buckets)):
      sortedBuckets.append(radixBucketSort(buckets[i], maxLen, index + 1))
  return sortedBuckets

def radixSort(words: list):
  # order words by the leftmost character (most significant)
  words: list = lexicographicSortOnChar(words, 0)
  buckets: list = []
  # let's order words to bucket by 1st character:
  for i in range(len(words)):
    # foundBucket variable so we know if there even were bucket
    foundBucket: bool = False
    if len(buckets) == 0:
      buckets.append([])
      buckets[0].append(words[i])
      foundBucket: bool = True
    if (foundBucket):
      continue
    for j in range(len(buckets)):
      if words[i][0].lower() == buckets[j][0][0].lower():
        buckets[j].append(words[i])
        foundBucket: bool = True
    if (foundBucket):
      continue
    else:
      buckets.append([words[i]])
  sortedBuckets: list = []
  for i in range(len(buckets)):
    maxLen: int = max(buckets[i], key=len)
    sortedBuckets.append(radixBucketSort(buckets[i], maxLen, 1))
  # todo: if bucket len is 1 no need for sorting
  # if the characters in buckets in certain index are all different
  # then I think that there is no need to sort anything in that
  # bucket, create function that could be called recursively
  return sortedBuckets

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