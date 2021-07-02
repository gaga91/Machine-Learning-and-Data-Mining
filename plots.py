#Matplotlib is a Python library used for 2D graphics
# https://matplotlib.org/

import numpy as np
import matplotlib.pyplot as plt

#Graph of function sin(x) on an equidistant network of  100  points from the interval $ [1, 20] $.
# equidistant network with function values
x = np.linspace (0, 10, 100)
y = np.sin (x)

# Adjust graphic titles and axis features
plt.title ('Graph of function y = sin (x)')
plt.xlabel ('x')
plt.ylabel ('y')

# drawing graphics
plt.plot (x, y)

#view graphics
plt.show ()


#Graphs of the functions y =sin (x)  and $ y = \ cos (x) $ on the interval $ [- \ pi, \ pi] $.

x = np.linspace (-np.pi, np.pi, 100)
y_sin = np.sin (x)
y_cos = np.cos (x)

# Draw functions with settings for display colors and features that will appear in the legend
plt.plot (x, y_sin, label = 'sin', color = 'blue')
plt.plot (x, y_cos, label = 'cos', color = 'green')

# setting a legend
plt.legend (loc = 'upper left')

#view graphics
plt.show ()