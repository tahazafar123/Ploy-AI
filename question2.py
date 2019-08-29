import numpy as np

def load_file(fname):
    # get rid of \n
    lines = open(filename).read().split('\n')
    # get rid of whitespace
    firstline = lines[0].split()
    
    # get grid size
    dim = int(firstline[0])
    # get number of inputs ('pizzerias')
    num_inputs = int(firstline[1])
    
    # get pizzeria info
    info = []
    for i in range(1,num_inputs + 1):
        line = [int(l) for l in lines[i].split()]
        info.append(line)
      
    return dim, num_inputs, info  
    
class Block():
    def __init__(self, dim, location, capacity, debug=True):
        # Check values
        if (dim < 1) | (dim > 1000):
            raise Exception('Dimensions should be within 1 to 1000')
        
        if (location[0] < 1) | (location[1] > dim):
            raise Exception('Pizzeria location must be within {} x {}'.format(dim,dim))
        
        if (capacity < 1) | (capacity > 100):
            raise Exception('Pizzeria range cannot be zero or exceed 100')
        self.debug = debug
        self.dim = dim
        self.location = location 
        self.capacity = capacity 
        self.block = np.zeros((dim,dim))
        
    def build_block(self):
        '''
        Build a 2D array showing the range of the pizzeria. 
        Within range set to 1, outside range set to 0. 
        '''
        x = self.location[0] - 1 # zero indexing
        y = self.location[1] - 1 # zero indexing
        
        for i in range(self.capacity + 1):
            # get vertical and horizontal
            if (x+i) < dim: # upper bound
                self.block[x+i][y] = 1
            if (x-i) >= 0: # lower bound
                self.block[x-i][y] = 1
            if (y+i) < dim:
                self.block[x][y+i] = 1
            if (y-i) >= 0:
                self.block[x][y-i] = 1

        for i in range(1,self.capacity):
            # get diagonals 
            if (x+i < dim) & (y+i < dim):
                self.block[x+i][y+i] = 1
            if (x-i >= 0) & (y-i >= 0): 
                self.block[x-i][y-i] = 1
            if (x+i < dim) & (y-i >= 0):
                self.block[x+i][y-i] = 1
            if (x-i >= 0) & (y+i < dim):
                self.block[x-i][y+i] = 1
        
        # flip block upside down to match indexing in question. 
        # Default indexing (0,0) on top left corner
        # Question requires indexing (0,0) at bottom left corner
        
        self.block = np.flipud(self.block)
        
        if self.debug:
            print(self.block)    
            
        return self.block
    

if __name__ == '__main__':
    # load data
    filename = 'input2.txt'
    
    # extract data
    dim, num_pizzerias, pizzerias = load_file(filename)
    
    sum_range = np.zeros((dim,dim))
    for pizzeria in pizzerias:
        block = Block(dim, pizzeria[0:-1], pizzeria[-1], debug=False)
        pizz_range = block.build_block()
        sum_range += pizz_range
    
    # print(sum_range)
    print(int(np.max(sum_range)))
    
    
    
    
