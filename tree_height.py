# python3
import sys
import threading
import numpy

def compute_height(n, parents):

    used = numpy.zeros(n)
    def height(i):
        if used[i] != 0:
            return used[i]
        if parents[i] == -1:
            used[i] = 1
        else:
            used[i] = height(parents[i]) + 1
        return used[i]
    
    for i in range(n):
        height(i)
    return int(max(used))

def main():
    # get input from the user
    inputType = input()
    height = 1

    # input from the keyboard
    if "I" in inputType:
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))
        height = compute_height(n, parents)

    # input from a file
    elif "F" in inputType:
        filename = input()
        if "a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:
            try:
                with open(filename) as f:
                    n = int(f.readline().strip())
                    parents = numpy.array(list(map(int, f.readline().strip().split())))
                    height = compute_height(n, parents)
            except FileNotFoundError:
                print("file not found")
                return
    else:
        print("Invalid input source")
        return
    
    
    # output the result
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
