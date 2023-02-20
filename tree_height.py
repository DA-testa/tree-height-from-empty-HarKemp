# python3
# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    a = 0
    # Your code here
    while a != -1:
        # a = numpy.where(parents==parents[a])
        a = parents[a]
        max_height = max_height + 1
    return max_height



def main():
    # implement input form keyboard and from files
    text = input()
    if "I" in text:
        n = input("Skaits: ")
        text = input("Elementi: ")
        arr = numpy.array(map(text.split()))
        compute_height(n, arr)

    elif "F" in text:
        failaNosaukums = input("Faila nosaukums:")
        with open("./test/" + failaNosaukums, mode="r") as fails:
            n = fails.readLine()
            text = fails.read()
        arr = numpy.array(map(text.split()))
        compute_height(n, arr)
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

