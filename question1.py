from logic import Logic
import numpy as np
import os

def get_input(filename):

    '''##
    Fetch number of nodes and coordinates of zearth from textfile.
    
    Args: 
        filename: txt file containing coordinates
    
    Returns: 
            a tuple containing (zearth, nodes)
            zearth: coordinates of Zearth
            nodes: An array containing coordinates of nodes
    ##'''
    lines = open(filename).read().split('\n')    
    
    # Get number of nodes
    num_node = int(lines[1])
    # Check value of num_node
    if (num_node < 1) or (num_node > 500):
        #If number of station is less than 1 and more than 500
        raise Exception('Number of stations should be in between 1 to 500')    
    earth = [0.0, 0.0, 0.0] # Earth coordinates
    zearth = parse_coordinates(lines[0])
    nodes = []
    nodes.append(earth)
    nodes.append(zearth)

    for i in range(num_node):
        # get coordinates excluding num_nodes and zearth
        coord = parse_coordinates(lines[i+2])    
        nodes.append(coord)
    return nodes, num_node + 1 + 1 #include earth and zearth

def parse_coordinates(line):
    '''
    Extracts coordinates from strings read from a txt file.
    Args: 
        line: string read from a txt file
    
    Returns:
        coordinate: coordinate value extracted from string
    '''
    coordinate = []
    # split string in terms of whitespace
    string = line.split()
    # convert string to floats
    for num in string:
        num = float(num)
        
        # Check for values
        if (num < -10000.0) | (num > 10000.0):
            raise Exception('Coordinate values must be within -10000, 10000')
        
        coordinate.append(num)
    return coordinate

def find_route(start, end, mst):
    '''
    Find route from start to end on a minimal spanning tree
    '''
    mst = sorted(mst, key=lambda item:item[0])
    

def get_distance(coord1, coord2):
    ''' 
    Calculates euclidian distance between nodes (l2-norm)    
    '''
    # convert to numpy array form as list cannot do subtraction
    coord1 = np.asarray(coord1)
    coord2 = np.asarray(coord2)
    return np.linalg.norm(coord1 - coord2)
    

if __name__ == "__main__":
    # load file containing data
    filename = 'input.txt'
    lines = get_input(filename)
    
    # Retrieve data
    coordinates, num_nodes = get_input(filename)
    
    # initialise Graph object for constructing minimum spanning tree
    mst = Logic(num_nodes)
    
    # load edges to graph. Assume fully connected
    # node 0 is earth, node 1 is zearth
    for i, coord1 in enumerate(coordinates): 
        for j, coord2 in enumerate(coordinates):
            if (i != j) & (i<j): 
                weight = get_distance(coord1, coord2)
                mst.add_edge(i,j,weight)
    
    result = mst.find_MST()
    
    # Get best route from mst
    route = mst.find_shortest_path(0,1,result)
    # Get max weight path in route
    max_weight = mst.get_max_weight(route)
    
    # print results
    print("Best route is: {}".format(route))
    print("Output: %.2f" % max_weight)
    
    
    
