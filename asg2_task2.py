'''
Individual Assignment 2 Part 2
Name: Oscar Ng Cheuk Hau
StudentID: 11558129
Class: Monday
'''

class Node:
    """
    Attributes:
    - name         : node label ('a', 'b', ...)
    - neighbours   : list of connected Node objects
    - distances    : distances (parallel list) to store km
    """
    def __init__(self, name): 
        self.name = name       # Node label
        self.neighbours = []   # List of Node objects
        self.distances = []    # List of km to each neighbour

    def add_neighbour(self, neighbour_node, distance):
        """Add edge with distance"""
        if neighbour_node not in self.neighbours: # Avoid duplicate neighbours
            self.neighbours.append(neighbour_node) # Add neighbour node
            self.distances.append(distance) # Add corresponding distance


def BFS(start_node, target_node): # Define BFS function
    """ 
    Returns: (path_list, total_km) or (None, None)
    """
    from collections import deque # Library for dequeuing from the left

    visited = {start_node} # Track visited nodes
    queue = deque([(start_node, [start_node], 0)])  # (node, path, distance)

    while queue: # While there are nodes in the queue
        current, path, dist = queue.popleft() # Dequeue until there is no node left

        if current == target_node: # Found target node
            return path, dist # Return path and distance (distance for further calculation)

        # Explore neighbours
        for neigh, km in zip(current.neighbours, current.distances): # Pair neighbour node with distance
            if neigh not in visited: # If neighbour not visited
                visited.add(neigh) # Mark neighbour as visited
                queue.append((neigh, path + [neigh], dist + km)) # Enqueue neighbour with updated path and distance to the output queue



def graph(): # Graph built for traversal
    nodes = {ch: Node(ch) for ch in 'abcdef'} 

    edges = [ # Data from the guidline. The data is follwing: (start, destination, distance)
        ('a', 'd', 110),   # A to D
        ('b', 'd', 220),   # B to D
        ('c', 'b', 276),   # C to B
        ('d', 'e', 113),   # D to E
        ('d', 'f', 311),   # D to F
        ('e', 'a', 112),   # E to A
        ('f', 'b', 270)    # F to B
    ]

    for src, dst, km in edges:
        nodes[src].add_neighbour(nodes[dst], km) 
    return nodes

def print_graph(nodes): # Print the graph connections
    print() # Formatting for better readability
    print("====================================\n") # formatting for better readability
    print("=== GRAPH CONNECTIONS ===") # formatting for better readability
    for node in nodes.values(): # iterate through each node
        neigh_names = [n.name.upper() for n in node.neighbours] # get neighbour names in uppercase
        dist_list = [f"{d}km" for d in node.distances] # get distances in km format

        # Format: Node [A] → [D], [F] ; 110km, 311km
        neigh_str = ', '.join(f"[{n}]" for n in neigh_names)
        dist_str = ', '.join(dist_list)

        print(f"Node [{node.name.upper()}] → {neigh_str} ; {dist_str}") # print node and its neighbours with distances
    print("====================================\n") # formatting for better readability

def get_node(prompt): # Get valid node input from user
    while True: # Loop until valid input
        val = input(prompt).strip().lower() # Get user input and format it
        if val in 'abcdef': # Limiting user input to a, b, c, d, e, f 
            return val # Return valid node after checking else prompt error and let user input again
        print("ERROR: Invalid node! Must be a, b, c, d, e or f") # Prompt error message for invalid user input


def main(): # Main program function
    print() # Formatting for better readability
    print("=" * 60) # Formatting for better readability
    print("INT3086 ASSIGNMENT 2 - TASK 2: BFS WITH DISTANCE") # Title of the program
    print("Name: Oscar Ng Cheuk Hau")
    print("=" * 60) # Formatting for better readability
    nodes = graph() # Use the graph for traversal 

    print_graph(nodes) # Print the graph connections for user to see

    while True: # Main loop for user interaction
        start = get_node("Please start [a to f]:--> ") # Getting the starting node from user with validation checking
        dest = get_node("What is the Destination [a to f]:--> ") # Getting the destination node from user with validation checking

        if start == dest: # Preventing coliding starting and destination node
            print("ERROR: start and Destination cannot be the same!") # If colide, prompt error message and let user input again
            continue

        path_nodes, total_km = BFS(nodes[start], nodes[dest]) # Set value of path_nodes and total_km by calling BFS function and outputing (start_node, target_node)

        S = start.upper() # Formatting the start node input
        E = dest.upper() # Formatting the end node input

        if path_nodes: # If a path is found
            path_str = " → ".join(n.name.upper() for n in path_nodes) # Build the path string for user to see

            breakdown = [] # Build the breakdown of distances for user to see
            for i in range(len(path_nodes) - 1):
                curr = path_nodes[i] # Current node in the path
                nxt = path_nodes[i + 1] # Next node in the path
                idx = curr.neighbours.index(nxt) # Find index of next node in current node's neighbour list
                km = curr.distances[idx] # Get the distance using the found index
                breakdown.append(f"{km}km") # Append the distance to breakdown list accordingly

            breakdown_str = " + ".join(breakdown) # Join the breakdown list into a string for output

            print(f"\nThere is a path from {S} to {E}, which is: {path_str}") # Output the path found
            print(f"The distant from {S} to {E} is: {breakdown_str} = {total_km}km") # Output the total distance with breakdown
        else:
            print(f"\nThere is NO path from {S} to {E}") # Output no path found

        # Continue or Ternminate
        while True: 
            choice = input("\nDo you want to continue? Y/N ").strip().upper() # Ask user if they want to continue
            if choice in ('Y', 'N'): # Validate user input
                break # Exit loop if valid input
            print("ERROR: Please enter Y or N") # Prompt error message for invalid input

        if choice == 'N': # If user wants to exit & typed N
            print("Thank you for using!") # Print termination message
            exit() # Terminate the program
        else:
            main() # Restart the main function for new input


if __name__ == "__main__":
    main() # Call main function to start the program