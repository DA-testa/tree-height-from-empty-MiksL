import sys
import threading
import numpy

def compute_height(n, parents):
    visitedNodeHeight = [-1] * n  # List of the heights of the nodes
    
    def getHeight(node): # Recursive function to get the height of a node
        if visitedNodeHeight[node] != -1: # If the node has been visited, the height of the node is returned
            return visitedNodeHeight[node]
        
        parentNode = parents[node] # Gets the parent node of the current node
        
        if parentNode == -1: # Checks if the parent node is the root node
            visitedNodeHeight[node] = 1
        else: # If the parent node is not the root node, the height of the current node is 1 + the height of the parent node
            visitedNodeHeight[node] = 1 + getHeight(parentNode) # Recursively call the getHeigth function
        return visitedNodeHeight[node]
    
    maxHeight = 0
    for node in range(n): # Loops through all the nodes in the tree
        if visitedNodeHeight[node] == -1: # Get the height of the node only if it has not been visited yet
            if(maxHeight < getHeight(node)): # If the height of the current node is greater than the current max height, then the current node's height is set as the new max height
                maxHeight = getHeight(node)
                
    return maxHeight

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