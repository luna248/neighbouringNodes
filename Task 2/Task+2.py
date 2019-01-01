
# coding: utf-8

# In[246]:


from math import sqrt
from enum import Enum


# In[442]:


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
                
    def setShape(self, *args):
        #Check the number of parameters to identify if i or xy have been entered
        if(len(args)) == 5:
            grid = args[0]
            xCoord = args[1]
            yCoord = args[2]
            m = args[3]
            shapeType = args[4]
                    
        elif(len(args)) == 4:
            grid = args[0]
            index = args[1] 
            m = args[2] 
            shapeType = args[3]
            xCoord = self.getNodeCoordinates(grid, index)[0]
            yCoord = self.getNodeCoordinates(grid, index)[1]
            
        else:
            print("\033[0;31;1mPlease enter valid parameters")
            return
        
        if (xCoord-m)<0 or (yCoord-m)<0 or (xCoord+m)>=self.size or (yCoord+m)>=self.size:
                print("The given radius exceeds the grid boundaries. Try again.")
                return
            
        #Set origin and neighbour nodes
        grid[xCoord][yCoord].setOrigin()
        if(shapeType == "square"):
            for i in range(xCoord-m, xCoord+m+1, 1):
                for j in range(yCoord-m, yCoord+m+1, 1):
                    grid[i][j].setNeighbour()
        elif(shapeType == "cross"):
            for i in range(xCoord-m, xCoord+m+1, 1):
                grid[i][yCoord].setNeighbour()    
            for j in range(yCoord-m, yCoord+m+1, 1):
                grid[xCoord][j].setNeighbour()
        elif(shapeType == "diamond"):
            layer=0
            for offset in range(m, m-m-1, -1):
                for i in range(xCoord-offset, xCoord+offset+1, 1):
                        if(layer==0):
                            grid[i][yCoord-layer].setNeighbour()
                        else:
                            grid[i][yCoord-layer].setNeighbour()
                            grid[i][yCoord+layer].setNeighbour()
                layer+=1
        else:
            print("\033[0;31;1mPlease enter a valid shape")
            return
        
        #Print the new grid
        print("New grid:")
        for i in range(self.size):
            for j in range(self.size):
                if(gridx[i][j].origin):
                    print("\033[0;31;35m",gridx[i][j].printCoordinates(), end="\033[0;30;0m ")
                elif(gridx[i][j].neighbour):
                    print("\033[0;31;11m",gridx[i][j].printCoordinates(), end="\033[0;30;0m ")
                else:
                    print(gridx[i][j].printCoordinates(), end=" ")
            print("\n")


# In[443]:


class node:
    
    def __init__(self, x, y, i):
        self.x = x
        self.y = y 
        self.i = i
        self.origin = False
        self.neighbour= False
    
    def getI(self):
        return self.i
    
    def getXY(self):
        return self.x, self.y
    
    def printCoordinates(self):
        return self.x, self.y, self.i
    
    def setOrigin(self):
        self.origin = True
    
    def setNeighbour(self):
        self.neighbour = True


# In[458]:


# Create object and run the function 
x= neighbouringNodes(7, True)
gridx = x.constructGrid()


# In[459]:


print("Node coordinates:", x.getNodeCoordinates(gridx, 12))


# NOTE: If the arguments are being changed in setShape, the original grid might have to be intialized again in some cases for the changes to show

# In[461]:


#Set shape
x.setShape(gridx, 3, 3, 3, "diamond")

