#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''

from statistics import median
from subprocess import list2cmdline

def quicksort(numbers_in_a_list):

    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list

    medianNum = median(numbers_in_a_list)
    lowList = []
    highList = []

    for i in numbers_in_a_list:
        if i <= medianNum:
            lowList.append(i)
        else:
            highList.append(i)

    

    return quicksort(lowList) + quicksort(highList)


def main():
    numbersFile = open("numbers.txt","r")
    #https://www.w3schools.com/python/python_file_open.asp
    fileIn = numbersFile.read()
    numList = strToNumList(fileIn)
    sortedList = quicksort(numList)
    print(sortedList)
    strList = ' '.join(str(e) for e in sortedList)
    #https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
    strList = strList.replace(' ',", ")
    numbersFile = open("sorted.txt","a")
    numbersFile.write("[" + strList + "]")
    numbersFile.close()
    return 0

def strToNumList(str):
    str = str.replace('[','')
    str = str.replace(']','')
    strList = str.split(",")
    numList = [eval(i) for i in strList]
    #Method Found from https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    return numList

def prntList(numList):
    reStr = "["


if __name__ == "__main__":
    main()
