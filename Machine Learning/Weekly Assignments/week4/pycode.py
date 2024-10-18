import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

df = pd.read_csv("week4.csv",sep=',')
x1=df.iloc[:,0]
x2=df.iloc[:,1]
x=np.column_stack((x1,x2))
y=df.iloc[:,2]

x_with_positive_y = x[y == 1]
x_with_negative_y = x[y == -1]

plt.scatter(x_with_negative_y[:, 0], x_with_negative_y[:, 1], color='red', marker='+', label="+1 data")
plt.scatter(x_with_positive_y[:, 0], x_with_positive_y[:, 1], color='blue', marker='o', label="-1 data")
# plt.rc('font', size=18)
plt.xlabel('X_1'); plt.ylabel('X_2')
plt.legend(loc='upper right')
plt.show()

