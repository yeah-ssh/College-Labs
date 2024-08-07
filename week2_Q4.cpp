// https://github.com/Helyousfi/DijkstraAlgorithm

// Let's take a closer look at the dijkstra.c file from the Helyousfi/DijkstraAlgorithm project:

// Main Function (main):

// Initializes variables and reads input for the number of nodes, the adjacency matrix, and the starting node.
// Calls the dijkstra function to compute the shortest paths from the starting node to all other nodes.
// Dijkstra Function (dijkstra):

// Takes the adjacency matrix, the number of nodes, and the starting node as inputs.
// Uses arrays to keep track of the shortest distance from the starting node to each other node and whether a node has been visited.
// Implements the core logic of Dijkstra's algorithm by iteratively selecting the unvisited node with the smallest distance and updating the distances of its neighbors.
// Utility Functions:

// minDistance: Finds the unvisited node with the smallest distance.
// printSolution: Prints the shortest distances from the starting node to each other node.
