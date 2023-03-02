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
    temp = numpy.where(parents==maximum)
    a = temp[0][0]

    while a != -1:
        a = parents[a]
        max_height = max_height + 1
    return max_height


def main():
    # get input from the user
    source = input()

    if source == "I":
        # input from the keyboard
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))
    elif source == "F":
        # input from a file
        filename = input("Enter filename: ")
        # while "a" in filename.tolower():
        #     filename = input("Invalid filename. Enter filename again (excluding 'a'): ")
        try:
            with open(filename) as f:
                content = f.read()
                n = int(content)
                parents = numpy.array(list(map(int, content.split())))
        except FileNotFoundError:
            print("file not found")
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
main()
