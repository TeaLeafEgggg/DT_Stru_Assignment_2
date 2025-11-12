'''
Individual Assignment 2
Working File
Please start your work with this file
YourName: Oscar Ng Cheuk Hau
StudentID: 11558129
Class: Monday
'''

# TODO
class Node: #Required in the 
    '''
    Define a Class call Node, that include two elements:
    Object Name: it is the label of the node.  
    Object Neighbour: it is a list to add all collected node(s)
    '''
    def __init__(self, name): 
        self.name = name # the label of the node
        self.neighbours = [] # list to store neighbour nodes
    
    def add_neighbour(self, neighbour_node): 
        if neighbour_node not in self.neighbours: # avoid duplicate neighbours 
            self.neighbours.append(neighbour_node) # add neighbour node to the list

#TODO: Install the BFS() here

def BFS(start_node, target_node): # define BFS function
    '''
    Perform Breadth-First Search (BFS) to find the shortest path from start_node to target_node.
    Without going back the path (as required in the assignment guidline).
    '''
    from collections import deque #import deque from collections module for easier queue processing in FIFO
    
    visited = set()  # Set to keep track of visited nodes
    queue = deque([(start_node, [start_node])])  # Queue for BFS,

    while queue:
        current_node, path = queue.popleft()  # Dequeue a node and the path to it

        if current_node == target_node: # Check if we reached the target
            return path  # Return the path if target is found

        visited.add(current_node)  # Mark the current node as visited

        for neighbour in current_node.neighbours: # Explore each neighbour
            if neighbour not in visited: # If neighbour hasn't been visited
                queue.append((neighbour, path + [neighbour]))  # Enqueue unvisited neighbours with updated path


# Main Program: test the BFS implementation
def main():
    
#====================================================
# TODO: Use you created Class Node to creating Graph for Traversal

#Create all Node Objects
    nodes = {} # dictionary to hold node objects
    for char in 'abcdef': # create nodes a to f
        nodes[char] = Node(char) # instantiate Node object

#Use neighbour to create the graphic
    # Define the graph connections according to the assignment requirement
    nodes['a'].add_neighbour(nodes['d'])
    nodes['b'].add_neighbour(nodes['d'])
    nodes['c'].add_neighbour(nodes['b'])
    nodes['d'].add_neighbour(nodes['e'])
    nodes['d'].add_neighbour(nodes['f'])
    nodes['e'].add_neighbour(nodes['a'])
    nodes['f'].add_neighbour(nodes['b'])

#Output the graphic connections

    print() 
    print("=== GRAPH CONNECTIONS ===") # formatting for better readability
    for name, node_obj in nodes.items(): # iterate through each node
        neigh_str = ', '.join(n.name for n in node_obj.neighbours) # get neighbour names
        print(f"Node {name}: → {neigh_str}") # print node and its neighbours
    print("====================================\n") # formatting for better readability

#====================================================

# TODO: geting the source and destination
# Note: your program needs to verify validate inputs, 
# such as node such node in the graphic, the sourse and destination are the same!
    '''
    Loop until the program get valid source and destination nodes from user 
    '''
    while True: # loop until valid input is received
        while True: # loop until valid source node is received
            src_start = input("Enter the source node: ").strip().lower() # get source node user input
            if src_start in nodes: # validate source node
                break # exit loop if valid
            print("Invalid source node. Please try again.") # error message for invalid input
        while True: # loop until valid destination node is received
            dest_end = input("Enter the destination node: ").strip().lower() # get destination node user input
            if dest_end in nodes: # validate destination node
                break # exit loop if valid
            print("Invalid destination node. Please try again.") # error message for invalid input
        if src_start == dest_end: # check if source and destination are the same
            print("Source and destination cannot be the same. Please try again.") # if same, prompt user error message and continue the loop until valid input
        else:
            break # exit loop if valid and source and destination nodes are different
#=====================================================

# TODO: BFS to find the path

    path = BFS(nodes[src_start], nodes[dest_end]) # call BFS function to find path
#=====================================================

# TODO: Output the path if found
    if path: # check if a path was found
        path_str = ' -> '.join(n.name for n in path) # format the path for output
        print(f"Path found: {path_str}") # print the found path
    else:
        print("NO path found between the specified nodes.") # print message if no path found

#=====================================================
    cont = input("Will you want to continue? Y/N\n").strip().upper() # ask user if they want to continue
    if cont == 'N': # check if user wants to exit
        print("System Terminate!") # print termination message
        exit() # exit the program
    else: # continue the loop
        main() # restart the main function 
        print() # formatting for better readability

if __name__ == "__main__":
    main() # call main function to start the program
 

