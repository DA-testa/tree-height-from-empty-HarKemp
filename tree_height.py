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

    # index = numpy.where(parents==-1)
    maximum = (max(parents))
    print(maximum)
    temp = numpy.where(parents==maximum)
    a = temp[0][0]
    print(a)

    while a != -1:
        a = parents[a]
        max_height = max_height + 1
    return max_height


def main():
    # get input from the user
    source = input().strip()

    if source == "I":
        # input from the keyboard
        n = int(input().strip())
        parents = numpy.array(list(map(int, input().split())))
    elif source == "F":
        # input from a file
        filename = input("Enter filename (excluding 'a'): ")
        while "a" in filename.tolower():
            filename = input("Invalid filename. Enter filename again (excluding 'a'): ")
        try:
            with open("./test/{filename}") as f:
                n = int(f.read())
                parents = numpy.array(list(map(int, f.read().split())))
        except FileNotFoundError:
            print("Error: file {filename} not found")
            return
    else:
        print("Invalid input source")
        return
    
    # compute the height of the tree
    height = compute_height(n, parents)
    
    # output the result
    print(height)
    
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
