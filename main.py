#Graph Cycle Detection
#Determines if a graph is cyclic. Uses Depth First Search algorithm for recursion.


#Graph class stores a node list and can perform is_cyclic test 
class Graph():
    def __init__(self, node_list):
        self.node_list = node_list
        self.node_dict = {}

    def is_cyclic(self):
        #convert list to a dictionary to know which nodes are adjacent
        for i, node in enumerate(self.node_list):
            self.node_dict[i] = node
        searched = {state : False for state in self.node_dict} #set searched to false for all initially
        cyclic = [False]
    
        for state in self.node_dict:
            if not searched[state]:
                self.search(state, cyclic, state, searched) #initial search has no predecessor so passes the state of the initial node twice.
            if cyclic[0]:
                break
        return cyclic[0]
    
    #Search checks node and its neighbors for a cycle
    def search(self, state, cyclic, predecessor, searched):
        if cyclic[0]:
            return
        searched[state] = True #node has been searched so will not be searched again
        for neighbor in self.node_dict[state]:
            if searched[neighbor] and neighbor != predecessor: #check if neighbor is marked but not previous node, if true it is cyclical
                cyclic[0] = True
                return
            if not searched[neighbor]:
                self.search(neighbor, cyclic, state, searched) #if neighbor hasn't been searched, repeat search until cycle is found or ends

graph1 = Graph([[1,4], [0,2], [0,1,3,4], [2,4], [2,3]])
print(graph1.is_cyclic()) #returns true

graph2 = Graph([[1], [0,2,3,5], [1], [1,4], [3,5], [1,4] ])
print(graph2.is_cyclic()) #returns true

graph3 = Graph([[1,2], [2], []])
print(graph3.is_cyclic()) #returns false