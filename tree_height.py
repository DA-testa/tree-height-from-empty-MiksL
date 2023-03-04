# python3

import sys
import threading
import numpy

# Constraints: - 1 <= n <= 10^5
# Memory limit: 512MB
def compute_height(n, parents):
    # Write this function
    max_height = 0
    # recursion will be used to find the height of the tree
    
    return max_height


def main():
    print("File type input")
    inputType = input()
    print("Input type: " + inputType[:1])
    # Below file type check is very similar to the first problem, with some minor changes to account for the different input type and requirements
    if(inputType[:1] == "F"):
        #print("Input the name of the file you want to use for testing")
        fileName = input()
        print("File name: " + fileName)
        
        # If the file name contains a then we return
        if("a" in fileName):
            return
        
        try:
            with open(fileName) as readableFile:
                # n - number of total nodes, a.k.a the first line of the input
                # parents - the second line of the input, a list of integers separated by spaces
                totalNodes = int(readableFile.readline()) # Converts the first line to an integer
                parentNodes = numpy.array(readableFile.readline().split(), dtype = int) # Can also be done using list(map(...)) or a for loop
                # Numpy will be faster because it does not use a loop in python
        except FileNotFoundError:
            print("Invalid file name or path")
            return
    elif(inputType[:1] == "I"):
        totalNodes = int(input()) # Converts the first user input line to the amount of nodes the tree has
        parentNodes = numpy.array(input().split(), dtype = int) # Converts the second user input line to a list of integers
    else:
        print("Invalid input character")
        return
    
    print(compute_height(totalNodes, parentNodes)) # Outputs the max height of the tree, no need to save the result since it is not used again

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()