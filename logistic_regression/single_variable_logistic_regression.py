from sklearn import linear_model
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
# read data from file.
df = pd.read_csv('C:/dataset/bald.csv')

# use a scatter plot to visualize data.
plt.scatter(df.iloc[:, 0], df.iloc[:, 1]) 

# complete the logistic regression.
model = linear_model.LogisticRegression(C = 1000000.) 
# array.reshape(-1,1) converts X to a column vector for X may has more than 1 dimension.
X = np.array(df['hairs']).reshape(-1, 1)
Y = np.array(df['bald'])
model.fit(X, Y)

# print the result of the model.
print('θ_1 = ', model.intercept_)
print('θ_0 = ', model.coef_[0])
print(model.score(X, Y))

# 'create' the logistic function, namely a list of x and another of f(x).
# np.linspace() generates a list of (0, 1, 2, 3, 4, ...., 21712).
x = np.linspace(0, 21712, 21712)
y = 1 / (1 + math.e ** -(model.coef_[0] * x + model.intercept_) )

# plot the result.
plt.plot(x, y)
plt.show()