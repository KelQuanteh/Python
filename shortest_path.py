#The algorithm will start at a specified node. 
#Then it will explore the graph to find the shortest path between the starting node, or source, and all the other nodes.

# Define a weighted graph using a dictionary where nodes are keys and 
# values are lists of tuples representing neighboring nodes and their distances
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Define a function to find the shortest path and distance from a starting node to a target node
def shortest_path(graph, start, target=''):
    # List of unvisited nodes
    unvisited = list(graph)
    
    # Dictionary to store distances from the start node to each node in the graph
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Dictionary to store paths from the start node to each node in the graph
    paths = {node: [] for node in graph}
    
    # Initialize the path for the start node
    paths[start].append(start)
    
    # Iterate until all nodes are visited
    while unvisited:
        # Select the unvisited node with the minimum distance from the start
        current = min(unvisited, key=distances.get)
        
        # Update distances and paths for neighboring nodes
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                # Update distance
                distances[node] = distance + distances[current]
                
                # Update path
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        
        # Mark the current node as visited
        unvisited.remove(current)
    
    # Determine which nodes to print results for (either specific target or all nodes)
    targets_to_print = [target] if target else graph
    
    # Print the results for each target node
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Return the final distances and paths
    return distances, paths

# Call the function to find the shortest path and distance from node 'A' to node 'F'
shortest_path(my_graph, 'A', 'F')
