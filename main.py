import sys
import math
import random
import datetime

def printWordsFromArray(words: list):
  for i in words:
    print(i)
  return

def lexicographicSort(words: list): # Todo. Make it faster?
  lenOfWords = len(words)
  for i in range(lenOfWords):
    for j in range(0, lenOfWords - i - 1):
      if words[j].lower() > words[j + 1].lower():
        words[j], words[j + 1] = words[j + 1], words[j]
  return words

def checkIfIndexIsInRange(arrOne: list, arrTwo: list, index: int):
  return index < len(arrOne) and index < len(arrTwo)

def lexicographicSortOnChar(words: list, index: int):
  lenOfWords: int = len(words)
  for i in range(lenOfWords):
    for j in range(0, lenOfWords - i - 1):
      indexInRange: bool = checkIfIndexIsInRange(words[j], words[j + 1], index)
      if indexInRange and words[j][index].lower() > words[j + 1][index].lower():
        words[j], words[j + 1] = words[j + 1], words[j]
  return words

def flatten(array: list):
  result = []
  for i in array:
    if isinstance(i, list):
      result.extend(flatten(i))
    else:
      result.append(i)
  return result

def createBuckets(words: list, index: int):
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
      indexInRange: bool = checkIfIndexIsInRange(words[i], buckets[j][0], index)
      if indexInRange and words[i][index].lower() == buckets[j][0][index].lower():
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
  words: list = lexicographicSortOnChar(words, index)
  # if there is nothing to sort, return after lexicographic sort
  if lexAndReturn:
    return words
  buckets = createBuckets(words, index)
  nothingToSort: bool = False
  if len(buckets) < 2:
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

def sortWordsByLength(words: list):
  words.sort(key=len)
  return words

def divideArray(array: list):
  arrayLen: int = len(array)
  return array[:arrayLen//2], array[arrayLen//2:]

def mergeSort(words: list):
  if len(words) > 1:
    firstHalf, secondHalf = divideArray(words)
    mergeSort(firstHalf)
    mergeSort(secondHalf)
    i: int = 0
    j: int = 0
    k: int = 0
    while i < len(firstHalf) and j < len(secondHalf):
      if firstHalf[i].lower() <= secondHalf[j].lower():
        words[k] = firstHalf[i]
        i += 1
      else:
        words[k] = secondHalf[j]
        j += 1
      k += 1
    while i < len(firstHalf):
      words[k] = firstHalf[i]
      i += 1
      k += 1

    while j < len(secondHalf):
      words[k] = secondHalf[j]
      j += 1
      k += 1

def radixSort(words: list):
  # order words by the leftmost character (most significant)
  words: list = lexicographicSortOnChar(words, 0)
  # let's order words to buckets by 1st character:
  buckets = createBuckets(words, 0)
  sortedBuckets: list = []
  for i in range(len(buckets)):
    buckets[i] = sortWordsByLength(buckets[i])
    maxLen: int = len(max(buckets[i], key=len))
    sortedBuckets.append(radixBucketSort(buckets[i], maxLen, 1, False))
  sortedWords = flatten(sortedBuckets)
  return sortedWords

def divideArrayByIndex(array: list, i: int):
  return array[:i], array[i + 1:]

def quickSort(words: list):
  if len(words) > 1:
    lenOfWords: int = len(words)
    # our pivot is always the last character in array
    pivot: str = words[lenOfWords - 1]
    tempWord: str = ''
    swapCounter: int = -1
    for i in range(0, lenOfWords):
      if i == lenOfWords - 1 or words[i].lower() <= pivot.lower():
        swapCounter += 1
        tempWord = words[swapCounter]
        words[swapCounter] = words[i]
        words[i] = tempWord
        tempWord = ''
    mid: str = words[swapCounter]
    first, second = divideArrayByIndex(words, swapCounter)
    first: list = quickSort(first)
    second: list = quickSort(second)
    return first + [mid] + second
  else:
    return words

def swap(array: list, i: int, j: int):
  temp: str = array[i]
  array[i] = array[j]
  array[j] = temp
  return array

def maxHeapify(words: list, nodeIndex: int):
  largestIndex: int = nodeIndex
  maxIndex: int = len(words) - 1
  leftIndex: int = 2 * nodeIndex + 1
  rightIndex: int = 2 * nodeIndex + 2
  if leftIndex <= maxIndex and words[leftIndex].lower() <= words[nodeIndex].lower():
    words = swap(words, nodeIndex, leftIndex)
    largestIndex: int = leftIndex
  if rightIndex <= maxIndex and words[rightIndex].lower() <= words[nodeIndex].lower():
    words = swap(words, nodeIndex, rightIndex)
    largestIndex: int = rightIndex
  if largestIndex != nodeIndex:
    words = maxHeapify(words, largestIndex)
  return words;

def heapSort(words: list):
  sortedWords: list = [];
  while len(words) > 0:
    maxLen: int = len(words)
    lastNonLeafNodeIndex: int = math.floor(maxLen / 2 - 1)
    for i in range(lastNonLeafNodeIndex, -1, -1):
      words = maxHeapify(words, i);
    sortedWords.append(words[0])
    swap(words, 0, maxLen - 1)
    words.pop()
    words = maxHeapify(words, 0)
  return sortedWords;

def hashArray(array: list, randomValue):
  lenOfArray = len(array)
  hashedArray = []
  for i in range(lenOfArray):
    hashValue: str = str(hash(hash(array[i]) + hash(randomValue)))
    hashedArray.append(hashValue)
  return hashedArray

def randomSort(words: list):
  randomValue: float = random.random()
  hashedWords: list = hashArray(words, randomValue)
  sortedHashedWords: list = quickSort(hashedWords)
  sortedDehashedWords: list = []
  for i in range(len(sortedHashedWords)):
    originalIndex: int = hashedWords.index(sortedHashedWords[i])
    sortedDehashedWords.append(words[originalIndex])
  return sortedDehashedWords

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

def readFileAndSortWords(fileName: str, isUnique: bool, sortAlgorithm: str):
  fileContent: str = readFile(fileName)
  fileContentArray: list = splitWordsToArray(fileContent)
  if (isUnique):
    fileContentArray: list = clearDuplicatedWords(fileContentArray)
  sortedFileContent: list = []
  if sortAlgorithm == 'radix':
    sortedFileContent: list = radixSort(fileContentArray)
  elif sortAlgorithm == 'merge':
    mergeSort(fileContentArray)
    sortedFileContent: list = fileContentArray
  elif sortAlgorithm == 'quick':
    sortedFileContent: list = quickSort(fileContentArray)
  elif sortAlgorithm == 'heap':
    sortedFileContent: list = heapSort(fileContentArray)
  elif sortAlgorithm == 'random':
    sortedFileContent: list = randomSort(fileContentArray)
  else:
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
    'isUnique': False,
    'sortAlgorithm': 'default', # lexicographic
    'captureTime': False
  }
  for i in arguments:
    if i == '-u':
      argumentObject['isUnique'] = True
    elif i == '-ct':
      argumentObject['captureTime'] = True
    elif i == 'sort=radix':
      argumentObject['sortAlgorithm'] = 'radix'
    elif i == 'sort=merge':
      argumentObject['sortAlgorithm'] = 'merge'
    elif i == 'sort=quick':
      argumentObject['sortAlgorithm'] = 'quick'
    elif i == 'sort=heap':
      argumentObject['sortAlgorithm'] = 'heap'
    elif i == 'sort=random':
      argumentObject['sortAlgorithm'] = 'random'
  return argumentObject

checkArgumentLen(sys.argv)
arguments: dict = readPassedArguments(sys.argv)
fileName: str = arguments['fileName']
isUnique: bool = arguments['isUnique']
sortAlgorithm: str = arguments['sortAlgorithm']
captureTime: bool = arguments['captureTime']
startTime = datetime.datetime.now()
sortedWords: list = readFileAndSortWords(fileName, isUnique, sortAlgorithm)
elapsedTime = datetime.datetime.now() - startTime
if captureTime:
  print('Elapsed time in sorting was:', elapsedTime.total_seconds() * 1000, 'milliseconds')
printWordsFromArray(sortedWords)