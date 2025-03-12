import numpy as np
import matplotlib.pyplot as plt

class Heart:
    
    # create a constructor to initialize the number of points , 
    # the width fo the line and the empty lists for x & y coords
    def __init__(self, numPoint=1000, lineWidth=2, figSize=(6, 6)):
        self.numPoint = numPoint
        self.lineWidth = lineWidth
        self.figSize = figSize
        self.xCoords = []
        self.yCoords = []
    
    def generate_coordinates(self):
        # create the linespace t which is used to generate the actual hear
        t = np.linspace(0, 2 * np.pi, self.numPoint)
        
        # the equations for a heart shape
        
        # x = 16sin^3(t)
        self.xCoords = 16 * np.power(np.sin(t), 3)
        # y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)
        self.yCoords = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        
        return self.xCoords, self.yCoords
    
    def plot(self, title="Heart Function", grid=True):
        
        # Generate coordinates for plotting
        self.generate_coordinates()
        
        # Plot the heart
        
        #set thefigure size
        plt.figure(figsize=self.figSize)
        #plot the x cooridnates and y coordinates
        plt.plot(self.xCoords, self.yCoords, linewidth=self.lineWidth)
        #set the title of the plot
        plt.title(title)
        #set the x and y labels
        plt.xlabel("X")
        plt.ylabel("Y")
        #set the axis to be equal
        plt.axis("equal")
        # show the grid and the actual plots
        plt.grid(grid)
        plt.show()


if __name__ == "__main__":
    # Create a heart and plot it
    heart = Heart(numPoint=1000, lineWidth=5,figSize=(5, 5))
    heart.generate_coordinates()
    heart.plot(title="Heart Function")
