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
        self.neighbours = []
    
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
    nodes = {}
    for char in 'abcdef':
        nodes[char] = Node(char)

#Use neighbour to create the graphic
    nodes['a'].add_neighbour(nodes['d'])
    nodes['b'].add_neighbour(nodes['d'])
    nodes['c'].add_neighbour(nodes['b'])
    nodes['d'].add_neighbour(nodes['e'])
    nodes['d'].add_neighbour(nodes['f'])
    nodes['e'].add_neighbour(nodes['a'])
    nodes['f'].add_neighbour(nodes['b'])

#Output the graphic connections
    print("=== GRAPH CONNECTIONS ===")
    for name, node_obj in nodes.items():
        neigh_str = ', '.join(n.name for n in node_obj.neighbours)
        print(f"Node {name}: → {neigh_str}")
    print("====================================\n")
#====================================================

# TODO: geting the source and destination
# Note: your program needs to verify validate inputs, 
# such as node such node in the graphic, the sourse and destination are the same!
    while True:
        while True:
            src_start = input("Enter the source node: ").strip().lower()
            if src_start in nodes:
                break
            print("Invalid source node. Please try again.")
        while True:
            dest_end = input("Enter the destination node: ").strip().lower()
            if dest_end in nodes:
                break
            print("Invalid destination node. Please try again.")
        if src_start == dest_end:
            print("Source and destination cannot be the same. Please try again.")
        else:
            break
#=====================================================

# TODO: BFS to find the path

    path = BFS(nodes[src_start], nodes[dest_end])
#=====================================================

# TODO: Output the path if found
    if path:
        path_str = ' -> '.join(n.name for n in path)
        print(f"Path found: {path_str}")
    else:
        print("NO path found between the specified nodes.")

#=====================================================
    cont = input("Will you want to continue? Y/N\n").strip().upper()
    if cont == 'N':
        print("System Terminate!")
        exit()
    print()

if __name__ == "__main__":
    main()
 

