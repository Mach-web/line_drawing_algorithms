#!/usr/bin/env python
# coding: utf-8

# ## CIT-223-018/2021 ANDERSON MACHARIA KINYUA

# ## Drawing a straight line in python using line drawing algorithms i.e slope intercept algorithm and DDA algorithm

# In[75]:


# import matplotlib package to visualize our results
import matplotlib.pyplot as plt
import seaborn as sns

class line_drawing_algorithms:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def slope_intercept(self):
        # unzip the tuples in parameters
        start_x, start_y = self.start_point
        end_x, end_y = self.end_point    
    
        # Find the gradient
        m = (end_y - start_y) / (end_x - start_x)
    
        # Get the y_intercept
        # Remember c = y - mx
        c = start_y - (m * (start_x))
    
        '''We are going to use our generated equation to generate a list of x and y values. y will be incremented by
        1 whereas we find the value of y. These values will be placed in a list then plotted'''
        x_values = []
        y_values = []
        # For our loop to run, we must check to ensure the start is smaller than the end - test3 will not run without this procedure
        if start_x > end_x:
            swap = start_x, start_y
            start_x, start_y = end_x, end_y
            end_x, end_y = swap
            
        for x in range(start_x, end_x + 1):
            x_values.append(x)
            y = m * (x) + c
            # round function rounds of the value of y
            y_values.append(round(y, 0))
        # print out the equation of the line
        print(f"The equation of the line in slope intercept algorithm is: y = {m}x + {c}")
        # Print out the values in our table
        print(f"X values: {x_values}")
        print("Y values to be plotted: {}".format(y_values))
        # Call the function to draw the line
        self.drawing(x_values, y_values, "slope intercept")
    
    def DDA(self):
        # unzip tuples in parameters
        start_x, start_y = self.start_point
        end_x, end_y = self.end_point
        # find the gradient of the line
        m = (end_y - start_y) / (end_x - start_x)
        # check if the gradient is below or above one
        # Create a list that will hold  the x and y values
        x_values = []
        y_values = []
        # For our loop to run, we must check to ensure the start is smaller than the end
        if start_x > end_x:
            swap = start_x, start_y
            start_x, start_y = end_x, end_y
            end_x, end_y = swap
            
        # check if gradient is below 1
        if m < 1 and m > 0:
            y = start_y
            for x in range(start_x, end_x + 1):
                x_values.append(x)
                y_values.append(round(y, 0))
                y += m
        elif m >= 1:
            x = start_x
            for y in range(start_y, end_y + 1):
                y_values.append(y)
                x_values.append(round(x, 0))
                # we add the inverse of gradient to each subsequent value of x
                x += (m ** -1)
        # Print out the values in our table
        print(f"X values: {x_values}")
        print("Y values to be plotted: {}".format(y_values))
        # Call the function to draw the line
        self.drawing(x_values, y_values, "DDA")
    
            
    def drawing(self, x_values, y_values, title):
        plt.title(f"Visualization of {title} algorithm")
        plt.xlabel("X values")
        plt.ylabel("Y values")
#         plt.pcolormesh(shading = 'nearest')
        plt.plot(x_values, y_values, color = "black")
        plt.grid(color = "g")
        plt.show()


# #### N/B: It is assumed that any grid where a line cuts across diagonally is shaded. Implementing a shaded grid happened to be harder than expected.

# In[76]:


test1 = line_drawing_algorithms((0, 0), (10, 6))
test1.slope_intercept()
test1.DDA()


# In[77]:


test2 = line_drawing_algorithms((1, 2), (6, 12))
test2.slope_intercept()
test2.DDA()


# In[78]:


test3 = line_drawing_algorithms((10, 5), (0, 0))
test3.slope_intercept()
test3.DDA()


# In[ ]:




