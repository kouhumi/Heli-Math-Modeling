import matplotlib.pyplot as plt 
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

def sig(x, para_0, para_1):
# combined function of logistic regression.
    return 1/(1 + np.exp(- para_0 - para_1 * x))

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
# figure of the data plot.

theta_0 = np.arange(-10, 10, 0.1)
theta_1 = np.arange(-10, 10, 0.1)
# the range of parameters.

dataset = [[1, 1], [2, 0], [3, 1], [4, 1], [5, 0]]
# trainset.

lost = []
# fill in the lost function paired with different values of theta_0 and theta_1
for i in theta_0:
    tmp = []
    for j in theta_1:
        sum = 0
        for k in dataset:
            cost_1 = sig(k[0], i, j)
            # invented cost function when y_i = 1
            cost_2 = 1 - sig(k[0], i, j)
            # invented cost function when y_i = 0 
            sum = sum + (k[1] * np.log(cost_1) + (1 - k[1]) * np.log(cost_2))
        sum = sum * (-1 / len(dataset))
        tmp.append(sum)
    lost.append(tmp)

lost = np.array(lost)
theta_0, theta_1 = np.meshgrid(theta_0, theta_1)
surf = ax.plot_surface(theta_0, theta_1, lost)
plt.show()
# plotting