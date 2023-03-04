# python3
import sys
import threading
import numpy

def compute_height(n, parents):
    for i in range(n):
        if parents[i] == -1:
            break

    levels = numpy.zeros(n)
    max_height = 1

    while True:
        updated = False
        for i in range(n):
            if levels[i] == max_height-1:
                for j in range(n):
                    if parents[j] == i:
                        levels[j] = max_height
                        updated = True
        if not updated:
            break
        max_height += 1

    return max_height


def main():
    # get input from the user
    inputType = input()
    n = 0

    # input from the keyboard
    if "I" in inputType:
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))

    # input from a file
    elif "F" in inputType:
        filename = input()
        if "a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        else:
            try:
                with open(filename) as f:
                    n = int(f.readline().strip())
                    parents = numpy.array(list(map(int, f.readline().strip().split())))
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
