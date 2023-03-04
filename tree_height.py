import sys
import threading
import numpy

def compute_height(n, parents):
    maxHeight = 0 # The maximum height reached by the tree
    
    # Use recursion to traverse up the tree and check the height of each node, if the height is greater than the current max height then we set the max height to the new height
    def traverseUp(node, height):
        nonlocal maxHeight # Nonlocal variable is declared so we can change maxHeight once we find a new maximum height/depth
        if(parents[node] == -1): # If the node does not have a parent we return
            if(height > maxHeight): # If the height is greater than the current max height then we set the max height to the new height
                maxHeight = height
            return
        traverseUp(parents[node], height + 1) # Recursively traverse up the tree, looking for the parent of the current node
        
    for node in range(n): # For each node in the tree we traverse up the tree to find the height of the node
        traverseUp(node, 1)
    
    return maxHeight
# Time complexity O(n^2)

def main():
    print("File type input")
    inputType = input()
    print("Input type: " + inputType[:1])
    # Below file type check is very similar to the first problem, with some minor changes to account for the different input type and requirements
    if(inputType[:1] == "F"):
        #print("Input the name of the file you want to use for testing")
        fileName = input()
        
        # If the file name contains a then we return
        if("a" in fileName):
            return
        elif("test/" not in fileName): # Add the test/ directory to the file name if it is not already there (for Autograding tests)
            fileName = "test/" + fileName
        
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