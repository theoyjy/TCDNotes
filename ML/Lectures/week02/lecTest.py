from sklearn.linear_model import LinearRegression
import numpy as np
Xtrain = np.arange(0,1,0.01).reshape(-1, 1)
ytrain = 10*Xtrain + np.random.normal(0.0,1.0,100).reshape(-1, 1)
model = LinearRegression().fit(Xtrain, ytrain)
print(model.intercept_, model.coef_)

import numpy as np 
Xtrain = np.random.uniform(0,1,100)
ytrain = np.sign(Xtrain - 0.5)
Xtrain = Xtrain.reshape(-1, 1) 

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(penalty=None, solver='lbfgs') 
model.fit(Xtrain, ytrain) 
print("intercept %f, slope %f" % (model.intercept_, model.coef_))

# -117.85 + 232.6x > 0
# 232.6x > 117.85
# x > 117.85/232.6
# x > 0.507

import matplotlib.pyplot as plt

ypred = model.predict(Xtrain)

plt.rc('font', size=18)
plt.rcParams['figure.constrained_layout.use'] = True
plt.scatter(Xtrain, ytrain, color='red', marker='+')
plt.scatter(Xtrain, ypred, color='green', marker='+')
plt.xlabel('input x'); plt.ylabel('output y')
plt.legend(['train','predict'])
plt.show()