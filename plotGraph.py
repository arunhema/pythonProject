import numpy as np
from matplotlib import pyplot as plt

# Title Matplotlib demo
plt.title("SyntaxBoard Line Graph Demo")

# x axis caption
plt.xlabel("Years")

# y axis caption
plt.ylabel("Dollors")

# Data Set Values
y1 = [10, 12, 15, 16, 10, 12]
y2 = [2,3,5,6,8,9]
y3 = [12,23,35,16,8,19]

# Y-Axis data set
x = [2000, 2001, 2002, 2003, 2004, 2005]


# Plot a Line Graph, in red color
plt.plot(x,y1,'r')

# Plot another Line Graph, in blue color
plt.plot(x,y2,'b')

# Plot another Line Graph, in green color
plt.plot(x,y3,'g')

# Render the Graph
plt.show()
# MARKDOWN ```