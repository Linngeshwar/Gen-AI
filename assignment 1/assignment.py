import numpy as np
from matplotlib import pyplot as plt


class assignment:
    def __init__(self,slope,x,noise):
        
        # initialize the slope , linespace , noise and the y
        self.slope = slope
        self.x = x
        self.noise = noise
        self.y = self.slope*self.x
    
    def visualise_data(self):
        
        #plot the like y = mx + c where m = slope and c = noise
        
        plt.title('Data Visualisation')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.scatter(self.x,self.y)
        plt.plot(self.x,self.slope*self.x,color='red')
        plt.show()
    
    def linear_approach(self):
        # linear approach to find the best slope
        #create a list of errors 
        errors = []
        mGuess = np.linspace(0,20,100)
        for i in mGuess:
            yGuess = i*self.x
            error = np.mean((self.y - yGuess)**2)
            errors.append(error)
        #find the best slope by getting the minimum error
        mBest = mGuess[np.argmin(errors)]
        print(mBest)
        
        #plot the errors and the best slope
        plt.title('Linear Approach')
        plt.xlabel('X')
        plt.ylabel('Y')
        #plotting the errors
        plt.plot(mGuess,errors)
        #plotting the best slope
        plt.plot(mBest,min(errors),marker='o',markersize=3,color='red')
        plt.show()
        
    def gradient_descent(self):
        #define the learnign rate,slope
        lr = 0.01
        m = np.random.random()
        errors = []
        
        #iteration over n times 
        for _ in range(10000):
            #finding the gradient and updating the slope 
            yGuess = m*self.x
            grad = 2*np.mean((yGuess - self.y)*self.x)
            #changing the slop with regards to the gradient
            m -= lr*grad
            errors.append(m)
        print(m)
        
        plt.plot(errors,label='predicted slope')
        plt.axhline(self.slope,color='red',label='Slope')
        plt.legend()
        plt.show()
    
if __name__ == "__main__":
    slope = 10
    x = np.linspace(-10,10,100)
    noise = np.random.normal(0,1,100)
    data = assignment(slope,x,noise)
    data.visualise_data()
    data.linear_approach()
    data.gradient_descent()
    