"""
File: ta10-solution.py
Author: Br. Burton
This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    if len(items) > 1:
        mid = len(items) // 2
        lefthalf = items[:mid]
        righthalf = items[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                items[k] = lefthalf[i]
                i = i + 1
            else:
                items[k] = righthalf[j]
                j = j + 1
            k = k + 1
        
        while i < len(lefthalf):
            items[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            items[k] = righthalf[j]
            j = j + 1
            k = k + 1

def quickSort(items):
    quickSortHelper(items,0,len(items)-1)

def quickSortHelper(items, first, last):
    if first<last:
       
        splitpoint = partition(items, first, last)

        quickSortHelper(items, first, splitpoint - 1)
        quickSortHelper(items, splitpoint + 1, last)

def partition(items, first, last):
    pivot = items[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and items[leftmark] <= pivot:
            leftmark = leftmark + 1
        while items[rightmark] >= pivot and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = items[leftmark]
            items[leftmark] = items[rightmark]
            items[rightmark] = temp
        
    temp = items[first]
    items[first] = items[rightmark]
    items[rightmark] = temp
    return rightmark

def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    #merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)

    print("The Quick Sort is: ")
    quickSort(items)
    display_list(items)


if __name__ == "__main__":
    main()