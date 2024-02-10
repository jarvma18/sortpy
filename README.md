# sortpy

More information about this challenge here:
https://codingchallenges.fyi/challenges/challenge-sort/

Basically this code tries to implement same functionalities as sort tool. I use python here because I want to learn it more.

Install python to run this code

## How to run

```
// Basic lexicographic sort
// This might take long because on inefficient algorithm
python3 main.py words.txt | uniq | head -n50

// Basic lexicographic sort with the -u (unique) option
python3 main.py -u words.txt | head -n50

// Radix sort with the -u (unique) option
python3 main.py -u sort=radix words.txt | head -n50

// Merge sort with the -u (unique) option
python3 main.py -u sort=merge words.txt | head -n50

// Quick sort with the -u (unique) option
python3 main.py -u sort=quick words.txt | head -n50

// Heap sort with the -u (unique) option
python3 main.py -u sort=heap words.txt | head -n50

// Run unit tests
python3 -m unittest test.py
```

## Radix sort

Radix sort, a non-comparative sorting algorithm that avoids comparison by placing elements of sorting into buckets according their radix.
Bucketing will be done for each character along the way and sorting the elements by their current radix (or character for words).

I implemented MSD radix sort, so I start with most significant digit and work the elements to the least significant digit. This is because I read that LSD (least significant digit) sorting will work well when you have same length words. My test data words are in different lengths.

![](radix-msd.png)

![](radix-msd-final.png)

## Merge sort

Merge sort is comparison-based sorting algorithm. It is divide-and-conquer algorithm (that breaks a problem into sub-problems to simplify the needed solution). Merge sort is efficient and general-purpose.

Simply the merge sort divides the sortable items and stops dividing when there is nothing to divide anymore (list lengths are 1). Then the items are rearranged in right order.

![](mergesort.png)

## Quick sort

Quick sort is efficient general-purpose sorting algorithm. Like merge sort the quick sort is divide-and-conquer algorithm. It is said to be slightly faster than merge sort or heap sort with randomized data.

Choose the pivot and then compare the other elements to pivot starting for the start of the list. If the comparable item is less than the pivot, then increment the counter that start from -1 index and swap item with incremented counter index with the item that was compared to pivot. After going through the list, lastly increment the counter once ore and swap the item with the pivot. Divide list with the pivot and do same until there is nothing to sort anymore and rearrange list with the new order.

I implemented the quick sort with pivot that is last element in word array. I chose to do that because it was very common way to implement the quick sort algorithm.

![](quicksort.png)

## Heap sort

Heap sort is comparison-based sorting algorithm. Heap sort divides the array into a sorted and an unsorted. It iteratively shrink the unsorted array by extracting the current largest item from it and placing it to sorted array.