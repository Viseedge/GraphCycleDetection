Graph Cycle Detection

Can determine if a graph is cyclical or not by taking in a list of connected points.

Getting Started

Create a Graph class using variable = Graph([]) where the argument is a list of lists of points connected.
Use the method is_cyclical to return True for the graph being cyclical and False for it not being cyclical.

Example:

graph1 = Graph([[1,4], [0,2], [0,1,3,4], [2,4], [2,3]])
print(graph1.is_cyclic()) # returns True

Requires:
Python 3