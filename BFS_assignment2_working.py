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
        self.name = name
        self.neighbouts = []
    
    def add_neighbour(self, neighbour_node):
        if neighbour_node not in self.neighbours: 
            self.neighbours.append(neighbour_node)

#TODO: Install the BFS() here

def BFS(start_node, target_node):
    '''
    Perform Breadth-First Search (BFS) to find the shortest path from start_node to target_node.
    Without going back the path (as required in the assignment guidline).
    '''
    from collections import deque #import deque from collections module for easier queue processing in FIFO
    
    visited = set()  # Set to keep track of visited nodes
    queue = deque([(start_node, [start_node])])  # Queue for BFS,

    while queue:
        current_node, path = queue.popleft()  # Dequeue a node and the path to it

        if current_node == target_node:
            return path  # Return the path if target is found

        visited.add(current_node)  # Mark the current node as visited

        for neighbour in current_node.neighbours:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))  # Enqueue unvisited neighbours with updated path


# Main Program: test the BFS implementation
def main():
    
#====================================================
# TODO: Use you created Class Node to creating Graph for Traversal

#Create all Node Objects

#Use neighbour to create the graphic

#====================================================

# TODO: geting the source and destination
# Note: your program needs to verify validate inputs, 
# such as node such node in the graphic, the sourse and destination are the same!

#=====================================================

# TODO: BFS to find the path

#=====================================================

# TODO: Output the path if found

#=====================================================

 

