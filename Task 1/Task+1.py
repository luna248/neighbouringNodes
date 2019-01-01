
# coding: utf-8

# In[37]:


from math import sqrt
from enum import Enum


# In[62]:


class neighbouringNodes:
    
    def __init__(self, size, debug):
        self.size = size
        self.debug = debug
    
    def constructGrid(self):
        grid = []
        count = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(node(i,j,count))
                count+=1
            grid.append(row)             
        
        if self.debug:
            for i in range(self.size):
                for j in range(self.size):
                    print(grid[i][j].printCoordinates(), end=" ")
                print("\n") 
        
        return grid
        
    
    def getNodeCoordinates(self, grid, iCoord):
        for i in range(self.size):
            for j in range(self.size):
                if (grid[i][j].getI() == iCoord):
                    return grid[i][j].getXY()
                


# In[63]:


class node:
    
    def __init__(self, x, y, i):
        self.x = x
        self.y = y 
        self.i = i 
    
    def getI(self):
        return self.i
    
    def getXY(self):
        return self.x, self.y
    
    def printCoordinates(self):
        return self.x, self.y, self.i
    


# In[67]:


# Create object and run the function 
x= neighbouringNodes(4, False)
gridx = x.constructGrid()

y= neighbouringNodes(3, True)
gridy = y.constructGrid()

print(x.getNodeCoordinates(gridx, 12))
print(y.getNodeCoordinates(gridy, 4))

