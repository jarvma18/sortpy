import unittest
import math
# Prints can be tested with io and sys
import io
import sys

from main import lexicographic_sort
from main import read_file
from main import read_file_and_sort_words
from main import open_file
from main import print_words_from_array
from main import clear_duplicated_words
from main import split_words_to_array
from main import check_len_of_arguments
from main import read_arguments
from main import radix_sort_msb
from main import radix_sort_with_buckets
from main import create_buckets_for_radix
from main import flatten
from main import lexicographic_sort_on_char
from main import is_index_in_range
from main import sort_words_by_length
from main import divide_array
from main import merge_sort
from main import quick_sort
from main import divide_array_by_index
from main import swap
from main import max_heapify
from main import heap_sort
from main import hash_array
from main import random_sort

TEST_DATA_1: list = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'e']
TEST_DATA_2: list = ['e', 'd', 'c', 'c', 'c', 'b', 'a', 'a']
TEST_DATA_3: str = 'a\na\nb\nc\nc\nc\nd\ne'
TEST_DATA_4: list = ['main.py']
TEST_DATA_5: list = ['main.py', 'words.txt']
TEST_DATA_6: list = ['main.py', '-u', 'words.txt']
TEST_DATA_7: list = ['tuple', 'anyones', 'bass', 'ananas',\
                     'anywhere', 'The', 'banana', 'A']
TEST_DATA_8: list = [[['ananas']], ['banana'],[['bass', 'basso']]]
TEST_DATA_9: list = ['ananas', 'pineapple', 'banana']
TEST_DATA_10: list = ['main.py', '-u', 'sort=radix', 'words.txt']
TEST_DATA_11: list = ['tuple', 'anyone', 'bass', 'ananas',\
                      'anywhere', 'The', 'banana']
TEST_DATA_12: list = ['The', 'Project', 'Gutenberg',\
                      'eBook', 'of', 'Art', 'War', 'This',\
                      'ebook', 'is', 'for', 'the', 'use',\
                      'anyone', 'anywhere', 'in', 'United',\
                      'States', 'and', 'most', 'other',\
                      'parts', 'world', 'at', 'no', 'cost',\
                      'with', 'almost', 'restrictions',\
                      'whatsoever', 'You', 'may', 'copy',\
                      'it', 'give', 'away', 'or', 're']
TEST_DATA_13: list = ['main.py', '-u', 'sort=merge', 'words.txt']
TEST_DATA_14: list = ['tuple', 'anyones', 'bass', 'ananas',\
                     'anywhere', 'The', 'banana', 'A']
TEST_DATA_15: list = ['The', 'Project', 'Gutenberg',\
                      'eBook', 'of', 'Art', 'War', 'This',\
                      'ebook', 'is', 'for', 'the', 'use',\
                      'anyone', 'anywhere', 'in', 'United',\
                      'States', 'and', 'most', 'other',\
                      'parts', 'world', 'at', 'no', 'cost',\
                      'with', 'almost', 'restrictions',\
                      'whatsoever', 'You', 'may', 'copy',\
                      'it', 'give', 'away', 'or', 're']
TEST_DATA_16: list = ['ananas', 'A', 'anywhere', 'anyone', 'all']
TEST_DATA_17: list = ['main.py', '-u', 'sort=quick', 'words.txt']
TEST_DATA_18: list = ['The', 'Project', 'Gutenberg',\
                      'eBook', 'of', 'Art', 'War', 'This',\
                      'ebook', 'is', 'for', 'the', 'use',\
                      'anyone', 'anywhere', 'in', 'United',\
                      'States', 'and', 'most', 'other',\
                      'parts', 'world', 'at', 'no', 'cost',\
                      'with', 'almost', 'restrictions',\
                      'whatsoever', 'You', 'may', 'copy',\
                      'it', 'give', 'away', 'or', 're']
TEST_DATA_19: list = ['main.py', '-u', 'sort=heap', 'words.txt']
TEST_DATA_20: list = ['ananas', 'A', 'anywhere', 'anyone', 'all']
TEST_DATA_21: list = ['tuple', 'anyones', 'bass', 'ananas',\
                     'anywhere', 'The', 'banana', 'A']
TEST_DATA_22: list = ['The', 'Project', 'Gutenberg',\
                      'eBook', 'of', 'Art', 'War', 'This',\
                      'ebook', 'is', 'for', 'the', 'use',\
                      'anyone', 'anywhere', 'in', 'United',\
                      'States', 'and', 'most', 'other',\
                      'parts', 'world', 'at', 'no', 'cost',\
                      'with', 'almost', 'restrictions',\
                      'whatsoever', 'You', 'may', 'copy',\
                      'it', 'give', 'away', 'or', 're']
TEST_DATA_23: list = ['main.py', '-u', 'sort=random', 'words.txt']
TEST_DATA_24: list = ['ananas', 'A', 'anywhere', 'anyone', 'all']
TEST_DATA_25: list = ['The', 'Project', 'Gutenberg',\
                      'eBook', 'of', 'Art', 'War', 'This',\
                      'ebook', 'is', 'for', 'the', 'use',\
                      'anyone', 'anywhere', 'in', 'United',\
                      'States', 'and', 'most', 'other',\
                      'parts', 'world', 'at', 'no', 'cost',\
                      'with', 'almost', 'restrictions',\
                      'whatsoever', 'You', 'may', 'copy',\
                      'it', 'give', 'away', 'or', 're']
TEST_DATA_26: list = ['main.py', '-u', '-ct', 'words.txt']
EXPECTED_1: str = 'a\na\nb\nc\nc\nc\nd\ne\n'
EXPECTED_2: str = 'Short text'
EXPECTED_3: list = ['a', 'b', 'c', 'd', 'e']
EXPECTED_4: list = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'e']
EXPECTED_5: dict = {'file_name': 'words.txt', 'is_unique': False,\
                    'sort_algorithm': 'default', 'capture_execution_time': False}
EXPECTED_6: dict = {'file_name': 'words.txt', 'is_unique': True,\
                    'sort_algorithm': 'default', 'capture_execution_time': False}
EXPECTED_7: list = ['A', 'ananas', 'anyones', 'anywhere',\
                    'banana', 'bass', 'The', 'tuple']
EXPECTED_8: list = ['ananas', 'banana', 'bass', 'basso']
EXPECTED_9: list = [['tuple', 'The'],\
                    ['anyones', 'ananas','anywhere', 'A'],\
                    ['bass', 'banana']]
EXPECTED_10: list = ['ananas', 'banana', 'pineapple']
EXPECTED_11: dict = {'file_name': 'words.txt', 'is_unique': True,\
                     'sort_algorithm': 'radix', 'capture_execution_time': False}
EXPECTED_12: list = ['anyone', 'ananas', 'anywhere', 'bass',\
                     'banana', 'tuple', 'The']
EXPECTED_13: list = ['almost', 'and', 'anyone', 'anywhere',\
                     'Art', 'at', 'away', 'copy', 'cost',\
                     'eBook', 'ebook', 'for', 'give',\
                     'Gutenberg', 'in', 'is', 'it', 'may',\
                     'most', 'no', 'of', 'or', 'other',\
                     'parts', 'Project', 're', 'restrictions',\
                     'States', 'The', 'the', 'This', 'United',\
                     'use', 'War', 'whatsoever', 'with',\
                     'world', 'You']
EXPECTED_14: dict = {'file_name': 'words.txt', 'is_unique': True,\
                     'sort_algorithm': 'merge', 'capture_execution_time': False}
EXPECTED_15: list = ['The', 'bass', 'tuple', 'anyone', 'ananas',\
                     'banana', 'anywhere']
EXPECTED_16: tuple = ['tuple', 'anyone', 'bass'],\
                      ['ananas', 'anywhere', 'The', 'banana']
EXPECTED_17: list = ['A', 'ananas', 'anyones', 'anywhere',\
                    'banana', 'bass', 'The', 'tuple']
EXPECTED_18: list = ['almost', 'and', 'anyone', 'anywhere',\
                     'Art', 'at', 'away', 'copy', 'cost',\
                     'eBook', 'ebook', 'for', 'give',\
                     'Gutenberg', 'in', 'is', 'it', 'may',\
                     'most', 'no', 'of', 'or', 'other',\
                     'parts', 'Project', 're', 'restrictions',\
                     'States', 'The', 'the', 'This', 'United',\
                     'use', 'War', 'whatsoever', 'with',\
                     'world', 'You']
EXPECTED_19: list = [[['ananas'], [['anyone'], ['anywhere']]], ['A'], ['all']]
EXPECTED_20: dict = {'file_name': 'words.txt', 'is_unique': True,\
                     'sort_algorithm': 'quick', 'capture_execution_time': False}
EXPECTED_21: list = ['almost', 'and', 'anyone', 'anywhere',\
                     'Art', 'at', 'away', 'copy', 'cost',\
                     'ebook', 'eBook', 'for', 'give',\
                     'Gutenberg', 'in', 'is', 'it', 'may',\
                     'most', 'no', 'of', 'or', 'other',\
                     'parts', 'Project', 're', 'restrictions',\
                     'States', 'The', 'the', 'This', 'United',\
                     'use', 'War', 'whatsoever', 'with',\
                     'world', 'You']
EXPECTED_22: tuple = ['tuple', 'anyones', 'bass'],\
                    ['anywhere', 'The', 'banana', 'A']
EXPECTED_23: dict = {'file_name': 'words.txt', 'is_unique': True,\
                     'sort_algorithm': 'heap', 'capture_execution_time': False}
EXPECTED_24: list = ['all', 'A', 'anywhere', 'anyone', 'ananas']
EXPECTED_25: list = ['tuple', 'anyones', 'bass', 'A',\
                     'anywhere', 'The', 'banana', 'ananas']
EXPECTED_26: list = ['anyones', 'A', 'bass', 'ananas',\
                     'anywhere', 'The', 'banana', 'tuple']
EXPECTED_27: list = ['almost', 'and', 'anyone', 'anywhere',\
                     'Art', 'at', 'away', 'copy', 'cost',\
                     'eBook', 'ebook', 'for', 'give',\
                     'Gutenberg', 'in', 'is', 'it', 'may',\
                     'most', 'no', 'of', 'or', 'other',\
                     'parts', 'Project', 're', 'restrictions',\
                     'States', 'the', 'The', 'This', 'United',\
                     'use', 'War', 'whatsoever', 'with',\
                     'world', 'You']
EXPECTED_28: dict = {'file_name': 'words.txt', 'is_unique': True,\
                     'sort_algorithm': 'random', 'capture_execution_time': False}
EXPECTED_29: list = ['ananas', 'A', 'anywhere', 'anyone', 'all']
EXPECTED_30: dict = {'file_name': 'words.txt', 'is_unique': True,\
                    'sort_algorithm': 'default', 'capture_execution_time': True}
EXCEPTION_1: str = 'File not found, check that the file exists in that path'
EXCEPTION_2: str = 'Too few arguments, provide at least file name'
EXCEPTION_3: str = 'Given index is out of range'
TEST_FILE_1: str = 'testing/this-file-should-not-exist.txt'
TEST_FILE_2: str = 'testing/short-text.txt'
TEST_FILE_3: str = 'testing/short-words.txt'

class TestClass(unittest.TestCase):
  def test_print_words_from_array(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    test_data: list = TEST_DATA_1
    expeted_value: str = EXPECTED_1
    print_words_from_array(test_data)
    sys.stdout = sys.__stdout__
    self.assertEqual(expeted_value, captured_output.getvalue())

  def test_open_not_existing_file(self):
    exception_message: str = EXCEPTION_1
    test_file: str = TEST_FILE_1
    with self.assertRaises(Exception) as context:
      open_file(test_file)
    self.assertTrue(exception_message in str(context.exception))

  def test_read_file(self):
    test_file: str = TEST_FILE_2
    expeted_value: str = EXPECTED_2
    read_file_content: str = read_file(test_file)
    self.assertEqual(expeted_value, read_file_content)

  def test_sort_lexicographically(self):
    test_data: list = TEST_DATA_2
    expeted_value: list = EXPECTED_4
    sorted_data: list = lexicographic_sort(test_data)
    self.assertEqual(expeted_value, sorted_data)

  def test_read_file_and_sort_content_with_false_uniqueness(self):
    test_file: str = TEST_FILE_3
    expeted_value: list = EXPECTED_4
    sorted_content: list = read_file_and_sort_words(test_file, False, 'default')
    self.assertEqual(expeted_value, sorted_content)

  def test_read_file_and_sort_content_with_true_uniqueness(self):
    test_file: str = TEST_FILE_3
    expeted_value: list = EXPECTED_3
    sorted_content: list = read_file_and_sort_words(test_file, True, 'default')
    self.assertEqual(expeted_value, sorted_content)

  def test_clear_duplicated_words(self):
    test_data: list = TEST_DATA_1
    expeted_value: list = EXPECTED_3
    unique_list: list = clear_duplicated_words(test_data)
    self.assertEqual(expeted_value, unique_list)

  def test_split_words_to_array(self):
    test_data: str = TEST_DATA_3
    expeted_value: list = EXPECTED_4
    words: list = split_words_to_array(test_data)
    self.assertEqual(expeted_value, words)

  def test_check_argument_len_with_too_few_args(self):
    exception_message: str = EXCEPTION_2
    with self.assertRaises(Exception) as context:
      check_len_of_arguments(TEST_DATA_4)
    self.assertTrue(exception_message in str(context.exception))

  def test_read_passed_arguments_filename_is_provided(self):
    test_data: list = TEST_DATA_5
    expeted_value: dict = EXPECTED_5
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_read_passed_arguments_filename_and_unique_is_provided(self):
    test_data: list = TEST_DATA_6
    expeted_value: dict = EXPECTED_6
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_read_passed_arguments_filename_unique_and_radix_is_provided(self):
    test_data: list = TEST_DATA_10
    expeted_value: dict = EXPECTED_11
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_read_passed_arguments_filename_unique_and_mergesort_is_provided(self):
    test_data: list = TEST_DATA_13
    expeted_value: dict = EXPECTED_14
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test__read_passed_arguments_filename_unique_and_quicksort_is_provided(self):
    test_data: list = TEST_DATA_17
    expeted_value: dict = EXPECTED_20
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_read_passed_arguments_filename_unique_and_heapsort_is_provided(self):
    test_data: list = TEST_DATA_19
    expeted_value: dict = EXPECTED_23
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_read_passed_arguments_filename_unique_and_randomsort_is_provided(self):
    test_data: list = TEST_DATA_23
    expeted_value: dict = EXPECTED_28
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_read_passed_arguments_filename_and_unique_and_capture_time_is_provided(self):
    test_data: list = TEST_DATA_26
    expeted_value: dict = EXPECTED_30
    argument_object: dict = read_arguments(test_data)
    self.assertEqual(expeted_value, argument_object)

  def test_radix_sort(self):
    test_data: list = TEST_DATA_7
    expeted_value: list = EXPECTED_7
    sorted_data: list = radix_sort_msb(test_data)
    self.assertEqual(expeted_value, sorted_data)

  def test_radix_sort_with_larger_data(self):
    test_data: list = TEST_DATA_12
    expeted_value: list = EXPECTED_13
    sorted_data: list = radix_sort_msb(test_data)
    self.assertEqual(expeted_value, sorted_data)

  def test_radix_bucket_sort_early_return(self):
    sorted_data = radix_sort_with_buckets(['ananas'], 1, 1, False)
    self.assertEqual(['ananas'], sorted_data)

  def test_radix_bucket_sort_lex_and_return(self):
    test_data: list = TEST_DATA_9
    expeted_value: list = EXPECTED_10
    sorted_data: list = radix_sort_with_buckets(test_data, 3, 0, True)
    self.assertEqual(expeted_value, sorted_data)

  def test_create_buckets(self):
    test_data: list = TEST_DATA_7
    expeted_value: list = EXPECTED_9
    buckets: list = create_buckets_for_radix(test_data, 0)
    self.assertEqual(expeted_value, buckets)

  def test_flatten(self):
    test_data: list = TEST_DATA_8
    expeted_value: list = EXPECTED_8
    flattened_array: list = flatten(test_data)
    self.assertEqual(expeted_value, flattened_array)

  def test_lexicographic_sort_on_char(self):
    test_data: list = TEST_DATA_11
    expeted_value: list = EXPECTED_12
    sorted_data: list = lexicographic_sort_on_char(test_data, 0)
    self.assertEqual(expeted_value, sorted_data)

  def test_check_if_index_is_not_in_range(self):
    arr1: list = TEST_DATA_1
    arr2: list = TEST_DATA_4
    expeted_value: bool = False
    index_in_range: bool = is_index_in_range(arr1, arr2, 100)
    self.assertEqual(expeted_value, index_in_range)

  def test_check_if_index_is_in_range(self):
    arr1: list = TEST_DATA_1
    arr2: list = TEST_DATA_4
    expeted_value: bool = True
    index_in_range: bool = is_index_in_range(arr1, arr2, 0)
    self.assertEqual(expeted_value, index_in_range)

  def test_check_if_index_is_not_in_range_of_other(self):
    arr1: list = TEST_DATA_1
    arr2: list = TEST_DATA_4
    expeted_value: bool = False
    index_in_range: bool = is_index_in_range(arr1, arr2, 2)
    self.assertEqual(expeted_value, index_in_range)

  def test_sortw_words_by_length(self):
    test_data: list = TEST_DATA_11
    expeted_value: list = EXPECTED_15
    sorted_array: bool = sort_words_by_length(test_data)
    self.assertEqual(expeted_value, sorted_array)

  def test_divide_array(self):
    test_data: list = TEST_DATA_11
    expeted_value: tuple = EXPECTED_16
    divided_array: tuple = divide_array(test_data)
    self.assertEqual(expeted_value, divided_array)

  def test_merge_sort(self):
    test_data: list = TEST_DATA_14
    expeted_value: list = EXPECTED_17
    merge_sort(test_data)
    self.assertEqual(expeted_value, test_data)

  def test_merge_sort_with_larger_data(self):
    test_data: list = TEST_DATA_15
    expeted_value: list = EXPECTED_18
    merge_sort(test_data)
    self.assertEqual(expeted_value, test_data)

  def test_radix_bucket_sort(self):
    test_data: list = TEST_DATA_16
    max_len: int = len(max(test_data, key=len))
    expected_value: list = EXPECTED_19
    sorted_data: list = radix_sort_with_buckets(test_data, max_len, 1, False)
    self.assertEqual(expected_value, sorted_data)

  def test_quick_sort_with_larger_data(self):
    test_data: list = TEST_DATA_18
    # EXPECTED_21 differs one value from others but we compare
    # characters as lower() so it does not matter so much
    expeted_value: list = EXPECTED_21
    sorted_data = quick_sort(test_data)
    self.assertEqual(expeted_value, sorted_data)

  def test_divide_by_array_index(self):
    test_data: list = TEST_DATA_14
    expeted_value: list = EXPECTED_22
    divided_array = divide_array_by_index(test_data, 3)
    self.assertEqual(expeted_value, divided_array)

  def test_swap_first_and_last_item_in_array(self):
    test_data: list = TEST_DATA_20
    expeted_value: list = EXPECTED_24
    swapped_array = swap(test_data, 0, len(test_data) - 1)
    self.assertEqual(expeted_value, swapped_array)

  def test_max_heapify_last_non_leaf_node(self):
    test_data: list = TEST_DATA_21
    expeted_value: list = EXPECTED_25
    last_non_leaf_index: int = math.floor(len(test_data) / 2 - 1)
    max_heapified_array: list = max_heapify(test_data, last_non_leaf_index)
    self.assertEqual(expeted_value, max_heapified_array)

  def test_max_heapify_root_node(self):
    test_data: list = TEST_DATA_21
    expeted_value: list = EXPECTED_26
    max_heapified_array: list = max_heapify(test_data, 0)
    self.assertEqual(expeted_value, max_heapified_array)

  def test_heap_sort_with_larger_data(self):
    self.max_diff = None
    test_data: list = TEST_DATA_22
    # EXPECTED_27 differs one value from others but we compare
    # characters as lower() so it does not matter so much
    expeted_value: list = EXPECTED_27
    sorted_data = heap_sort(test_data)
    self.assertEqual(expeted_value, sorted_data)

  def test_hash_array(self):
    test_data: list = TEST_DATA_24
    hashed_array = hash_array(test_data, 1)
    # Result set is always different
    # so we expect that the count is equal
    self.assertEqual(len(test_data), len(hashed_array))

  def test_random_sort_with_larger_data(self):
    test_data: list = TEST_DATA_25
    sorted_data = random_sort(test_data)
    # Result set is always different
    # so we expect that the count is equal
    self.assertEqual(len(test_data), len(sorted_data))