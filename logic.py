from collections import defaultdict

class Logic():
    '''
    Class to represent logic
    '''
        
    def add_edge(self, node1, node2, weight):
        self.graph.append([node1, node2, weight])
        
    
    def find(self,parent,node):
        '''
        Find parent nodes of a node. 
        '''
        if parent[node]== node:
            # No parent
            return node
        # iterate
        return self.find(parent, parent[node])

    def __init__(self, num_stations):
        # For Kruskal's Algorithm
        self.n = num_stations # number of stations
        self.graph = []
        # For Dijkstra's Algorithm
        self.edges = defaultdict(list)
        self.weights={}
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        
        # attach smaller rank tree under root of
        # high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: # function to find set the parent of a nodeyroot]:
            parent[yroot] = xroot
        else:
            # if ranks are the same, then make one 
            # a root and increment its rank by one
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def find_MST(self):
        '''
        Creates a minimum spanning tree for a given coordniates
        and returns the minimum spanning tree
            
        Returns: 
            result: A list containing a list of [node1, node2, weight]
                    values that belong to the minimum spanning tree
        '''
        result = [] # store the resultant minimum spanning tree
        i,j = 0,0 # index variables for sorted 
                  # edges and result respectively
                  
        # sort graph acording to edge size
        self.graph = sorted(self.graph,key=lambda item:item[2])
        
        parent, rank = [], []
        
        # create n subsets with single elements
        for node in range(self.n):
            parent.append(node)
            rank.append(0)
        
        # number of edges to be taken is n-1
        while j < self.n - 1:
            # pick the smallest edge
            node1,node2,weight = self.graph[i]
            # increment index to consider next largest edge
            i += 1
            x = self.find(parent, node1)
            y = self.find(parent, node2)
            
            # if including this edge doesn't cause 
            # a cycle, include it in result
            if x is not y:
                j+=1
                result.append([node1,node2,weight])
                self.union(parent, rank, x, y)
            # else discard the edge
            
        return result
    
    def find_shortest_path(self, start, end, mst):
        '''
        Find the shortest weight path in a graph using Dijkstra's algorithm.
        
        Args: 
            start: Start node
            end: End node
            mst: Graph in which to find shortest path
        
        Returns: 
            path: Shortest path from start to end
            
        '''
        def _add_edge(mst):
            for edge in mst:
                node1 = edge[0]
                node2 = edge[1]
                weight = edge[2]
                self.edges[node1].append(node2)
                self.edges[node2].append(node1)
                self.weights[(node1,node2)] = weight
                self.weights[(node2,node1)] = weight
        
        # initialise graph for dijkstra implementation
        _add_edge(mst)
        shortest_paths = {start: (None, 0)}
        current_node = start
        visited = set()
        weight = 0
        
        while current_node != end:
            visited.add(current_node)
            destinations = self.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]
            
            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths: 
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
                        
            next_destinations = (
                    {node: shortest_paths[node] for node in shortest_paths if node not in visited}
                    )
            if not next_destinations:
                return "route not possible"
            
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k:next_destinations[k][1])
            
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        
        return path
    
    def get_max_weight(self, path):
        '''
        Find maximum weight between two nodes in a path. 
        
        Args: 
            path: minimum weight edge in a path
            
        Returns:
            max_weight: maximum weight between two nodes
        '''
        max_weight = 0.0
        for i in range(len(path)-1):
            node1 = path[i]
            node2 = path[i+1]
            weight = self.weights[(node1,node2)]
            if weight > max_weight:
                max_weight = weight
                
        return max_weight
    
                
            
            
            
            
            
            
