import sys
import math
import random
import datetime

def print_words_from_array(words: list):
  for i in words:
    print(i)
  return

def lexicographic_sort(words: list): # Todo. Make it faster?
  len_of_words = len(words)
  for i in range(len_of_words):
    for j in range(0, len_of_words - i - 1):
      if words[j].lower() > words[j + 1].lower():
        words[j], words[j + 1] = words[j + 1], words[j]
  return words

def is_index_in_range(first_array: list, second_array: list, index: int):
  return index < len(first_array) and index < len(second_array)

def lexicographic_sort_on_char(words: list, index: int):
  len_of_words: int = len(words)
  for i in range(len_of_words):
    for j in range(0, len_of_words - i - 1):
      index_in_range: bool = is_index_in_range(words[j], words[j + 1], index)
      if index_in_range and words[j][index].lower() > words[j + 1][index].lower():
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

def create_buckets_for_radix(words: list, index: int):
  buckets: list = []
  for i in range(len(words)):
    is_bucket: bool = False
    if len(buckets) == 0:
      buckets.append([])
      buckets[0].append(words[i])
      is_bucket: bool = True
    if (is_bucket):
      continue
    for j in range(len(buckets)):
      index_in_range: bool = is_index_in_range(words[i], buckets[j][0], index)
      if index_in_range and words[i][index].lower() == buckets[j][0][index].lower():
        buckets[j].append(words[i])
        is_bucket: bool = True
    if (is_bucket):
      continue
    else:
      buckets.append([words[i]])
  return buckets

def radix_sort_with_buckets(words: list, max_len: int, index: int, return_after_lexiographic_sort: bool):
  if len(words) < 2:
    return words
  words: list = lexicographic_sort_on_char(words, index)
  if return_after_lexiographic_sort:
    return words
  buckets = create_buckets_for_radix(words, index)
  nothing_to_sort: bool = False
  if len(buckets) < 2:
    nothing_to_sort: bool = True
  for i in range(len(buckets)):
    buckets[i] = lexicographic_sort_on_char(buckets[i], index)
  sorted_buckets: list = []
  if index == max_len:
    return buckets;
  else:
    for i in range(len(buckets)):
      sorted_buckets.append(radix_sort_with_buckets(buckets[i], max_len, index + 1, nothing_to_sort))
  return sorted_buckets

def sort_words_by_length(words: list):
  words.sort(key=len)
  return words

def divide_array(array: list):
  len_of_array: int = len(array)
  return array[:len_of_array//2], array[len_of_array//2:]

def merge_sort(words: list):
  if len(words) > 1:
    first_half, second_half = divide_array(words)
    merge_sort(first_half)
    merge_sort(second_half)
    i: int = 0
    j: int = 0
    k: int = 0
    while i < len(first_half) and j < len(second_half):
      if first_half[i].lower() <= second_half[j].lower():
        words[k] = first_half[i]
        i += 1
      else:
        words[k] = second_half[j]
        j += 1
      k += 1
    while i < len(first_half):
      words[k] = first_half[i]
      i += 1
      k += 1

    while j < len(second_half):
      words[k] = second_half[j]
      j += 1
      k += 1

def radix_sort_msb(words: list):
  words: list = lexicographic_sort_on_char(words, 0)
  buckets = create_buckets_for_radix(words, 0)
  sorted_buckets: list = []
  for i in range(len(buckets)):
    buckets[i] = sort_words_by_length(buckets[i])
    max_len: int = len(max(buckets[i], key=len))
    sorted_buckets.append(radix_sort_with_buckets(buckets[i], max_len, 1, False))
  sorted_words = flatten(sorted_buckets)
  return sorted_words

def divide_array_by_index(array: list, i: int):
  return array[:i], array[i + 1:]

def quick_sort(words: list):
  if len(words) > 1:
    len_of_words: int = len(words)
    pivot: str = words[len_of_words - 1]
    tmp_word: str = ''
    swap_counter: int = -1
    for i in range(0, len_of_words):
      if i == len_of_words - 1 or words[i].lower() <= pivot.lower():
        swap_counter += 1
        tmp_word = words[swap_counter]
        words[swap_counter] = words[i]
        words[i] = tmp_word
        tmp_word = ''
    mid: str = words[swap_counter]
    first, second = divide_array_by_index(words, swap_counter)
    first: list = quick_sort(first)
    second: list = quick_sort(second)
    return first + [mid] + second
  else:
    return words

def swap(array: list, i: int, j: int):
  temp: str = array[i]
  array[i] = array[j]
  array[j] = temp
  return array

def max_heapify(words: list, index_of_node: int):
  largest_index: int = index_of_node
  max_index: int = len(words) - 1
  left_index: int = 2 * index_of_node + 1
  right_index: int = 2 * index_of_node + 2
  if left_index <= max_index and words[left_index].lower() <= words[index_of_node].lower():
    words = swap(words, index_of_node, left_index)
    largest_index: int = left_index
  if right_index <= max_index and words[right_index].lower() <= words[index_of_node].lower():
    words = swap(words, index_of_node, right_index)
    largest_index: int = right_index
  if largest_index != index_of_node:
    words = max_heapify(words, largest_index)
  return words;

def heap_sort(words: list):
  sorted_words: list = [];
  while len(words) > 0:
    max_len: int = len(words)
    index_if_last_non_leaf: int = math.floor(max_len / 2 - 1)
    for i in range(index_if_last_non_leaf, -1, -1):
      words = max_heapify(words, i);
    sorted_words.append(words[0])
    swap(words, 0, max_len - 1)
    words.pop()
    words = max_heapify(words, 0)
  return sorted_words;

def hash_array(array: list, randomValue):
  len_of_array = len(array)
  hashed_array = []
  for i in range(len_of_array):
    hash_value: str = str(hash(hash(array[i]) + hash(randomValue)))
    hashed_array.append(hash_value)
  return hashed_array

def random_sort(words: list):
  random_value: float = random.random()
  hashed_words: list = hash_array(words, random_value)
  sorted_hashed_words: list = quick_sort(hashed_words)
  sorted_dehashed_words: list = []
  for i in range(len(sorted_hashed_words)):
    index_of_original_value: int = hashed_words.index(sorted_hashed_words[i])
    sorted_dehashed_words.append(words[index_of_original_value])
  return sorted_dehashed_words

def clear_duplicated_words(words: list):
  list_of_unique_words: list = []
  for i in words:
    if i not in list_of_unique_words:
      list_of_unique_words.append(i)
  return list_of_unique_words

def split_words_to_array(words: str):
  splitted_content: list = words.split('\n')
  return splitted_content

def open_file(file_name: str):
  try:
    file = open(file_name, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def read_file(file_name: str):
  file = open_file(file_name)
  if file:
    file_content: str = file.read()
    file.close()
    return file_content
  else:
    return

def read_file_and_sort_words(file_name: str, is_unique: bool, sort_algorithm: str):
  content_of_file: str = read_file(file_name)
  array_of_file_content: list = split_words_to_array(content_of_file)
  if (is_unique):
    array_of_file_content: list = clear_duplicated_words(array_of_file_content)
  sorted_content: list = []
  if sort_algorithm == 'radix':
    sorted_content: list = radix_sort_msb(array_of_file_content)
  elif sort_algorithm == 'merge':
    merge_sort(array_of_file_content)
    sorted_content: list = array_of_file_content
  elif sort_algorithm == 'quick':
    sorted_content: list = quick_sort(array_of_file_content)
  elif sort_algorithm == 'heap':
    sorted_content: list = heap_sort(array_of_file_content)
  elif sort_algorithm == 'random':
    sorted_content: list = random_sort(array_of_file_content)
  else:
    sorted_content: list = lexicographic_sort(array_of_file_content)
  return sorted_content;

def check_len_of_arguments(arguments: list):
  if len(arguments) < 2:
    raise Exception('Too few arguments, provide at least file name')
  else:
    return

def read_arguments(arguments: list):
  last_argument: str = arguments[len(arguments) - 1]
  argument_object: dict = {
    'file_name': last_argument,
    'is_unique': False,
    'sort_algorithm': 'default', # lexicographic
    'capture_execution_time': False
  }
  for i in arguments:
    if i == '-u':
      argument_object['is_unique'] = True
    elif i == '-ct':
      argument_object['capture_execution_time'] = True
    elif i == 'sort=radix':
      argument_object['sort_algorithm'] = 'radix'
    elif i == 'sort=merge':
      argument_object['sort_algorithm'] = 'merge'
    elif i == 'sort=quick':
      argument_object['sort_algorithm'] = 'quick'
    elif i == 'sort=heap':
      argument_object['sort_algorithm'] = 'heap'
    elif i == 'sort=random':
      argument_object['sort_algorithm'] = 'random'
  return argument_object

check_len_of_arguments(sys.argv)
arguments: dict = read_arguments(sys.argv)
file_name: str = arguments['file_name']
is_unique: bool = arguments['is_unique']
sort_algorithm: str = arguments['sort_algorithm']
capture_execution_time: bool = arguments['capture_execution_time']
execution_start_time = datetime.datetime.now()
sorted_words: list = read_file_and_sort_words(file_name, is_unique, sort_algorithm)
execution_elapsed_time = datetime.datetime.now() - execution_start_time
if capture_execution_time:
  print('Elapsed time in sorting was:', execution_elapsed_time.total_seconds() * 1000, 'milliseconds')
print_words_from_array(sorted_words)