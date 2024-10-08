import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import KFold


# id:6--12-6 
df = pd.read_csv("week3.csv",sep=',')
x1=df.iloc[:,0]
x2=df.iloc[:,1]
X=np.column_stack((x1,x2))
y=df.iloc[:,2]

#(i)
#(a) plot 3d scatter
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X[:, 0], X[:, 1], y)
ax.set_xlabel('X_1')
ax.set_ylabel('X_2')
ax.set_zlabel('Target Value')
plt.show()

#(b) (c)
poly = PolynomialFeatures(5)
Xpoly5 = poly.fit_transform(X)
# split training and test data
Xpoly5_train, Xpoly5_test, y_train, y_test = train_test_split(Xpoly5, y, test_size = 0.2, random_state=1)

## get all combinations of the two features with the power of 5
# feature_names = poly.get_feature_names_out(input_features=['x1', 'x2'])
# # Print the feature names
# for name in feature_names:
#     print(name)

# create grid little bigger than the range of original features
x1_grid = np.linspace(X[:, 0].min() - 0.1,  X[:, 0].max() + 0.1)
x2_grid = np.linspace(X[:, 1].min() - 0.1,  X[:, 1].max() + 0.1)
x1_grid, x2_grid = np.meshgrid(x1_grid, x2_grid)
print("feature 0 extented range:{}-{}".format(x1_grid.min(), x1_grid.max()))
print("feature 1 extented range:{}-{}".format(x2_grid.min(), x2_grid.max()))
# create polynomial features for the grid data so that 
# it can be tested by a model trained with polynomial features up to the power of 5
x_grid_test = np.c_[x1_grid.ravel(), x2_grid.ravel()]
x_grid_test = poly.fit_transform(x_grid_test)

Crange = [1,10,100,1000]
for C in Crange:
    model = Lasso(alpha = 1/(2*C), fit_intercept=True)
    model.fit(Xpoly5_train, y_train)
    ypred = model.predict(Xpoly5_test)

    # (b) report the parameters
    print("lasso C = {}: Coefficients: {} Intercept: {}".format(C, model.coef_, model.intercept_))
    print("Mean Squared Error: ", mean_squared_error(y_test, ypred))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(X[:, 0], X[:, 1], y)

    # (c) draw Xtest and ypred on a 3D surface
    ypred = model.predict(x_grid_test)
    ypred = ypred.reshape(x1_grid.shape)
    
    # Plot surface
    ax.plot_surface(x1_grid, x2_grid, ypred, cmap='viridis', edgecolor='none')

    # Labels
    ax.set_xlabel('X_1')
    ax.set_ylabel('X_2')
    ax.set_zlabel('Output')
    ax.set_title('C={}'.format(C))

    # Show plot
    plt.show()

# (e)
Crange = [0.001, 0.01, 1, 10]
for C in Crange:
    model = Ridge(alpha=1/(2*C))
    model.fit(Xpoly5_train, y_train)
    ypred = model.predict(Xpoly5_test)

    # (b) report the parameters
    print("Ridge C = {}: Coefficients: {} Intercept: {}".format(C, model.coef_, model.intercept_))
    print("Mean Squared Error: ", mean_squared_error(y_test, ypred))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(X[:, 0], X[:, 1], y)

    # (c) draw Xtest and ypred on a 3D surface
    ypred = model.predict(x_grid_test)
    ypred = ypred.reshape(x1_grid.shape)
    
    # Plot surface
    ax.plot_surface(x1_grid, x2_grid, ypred, cmap='viridis', edgecolor='none')

    # Labels
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Predicted Value')
    ax.set_title('C={}'.format(C))

    # Show plot
    plt.show()

# (ii)
# (a) (b)
kf = KFold(n_splits=5)
def drawErrorBarLasso(Crange):
    train_mean_error=[]; train_std_error=[]
    test_mean_error=[]; test_std_error=[]	
    for C in Crange: 
        model = Lasso(alpha=1/(2*C))
        temp_train = []
        temp_test = []

        # iterate the 5-fold 
        for train, test in kf.split(Xpoly5): 
            model.fit(Xpoly5[train], y[train]) 

            ypred_train = model.predict(Xpoly5[train]) 
            temp_train.append(mean_squared_error(y[train], ypred_train))

            ypred_test = model.predict(Xpoly5[test]) 
            temp_test.append(mean_squared_error(y[test], ypred_test))

        train_mean_error.append(np.array(temp_train).mean())
        train_std_error.append(np.array(temp_train).std())
        test_mean_error.append(np.array(temp_test).mean()) 
        test_std_error.append(np.array(temp_test).std())

    plt.errorbar(Crange, train_mean_error, yerr=train_std_error, linewidth=3, label='Train Mean MSE with error bars') 
    plt.errorbar(Crange, test_mean_error, yerr=test_std_error, linewidth=3, label='Test Mean MSE with error bars') 
    plt.xlabel('C') 
    plt.ylabel('Mean square error')
    plt.legend(loc='best')
    plt.show()

drawErrorBarLasso([0.1, 1, 10, 100])
drawErrorBarLasso([1, 5, 10, 20, 50])
drawErrorBarLasso([1, 5, 7.5, 10, 20])

# (c)
# Crange = [0.1, 0.5, 1.5, 2, 2.5, 3, 10]
def drawErrorBarRidge(Crange):
    train_mean_error=[]; train_std_error=[]
    test_mean_error=[]; test_std_error=[]	
    for C in Crange: 
        model = Ridge(alpha=1/(2*C))
        temp_train = []
        temp_test = []

        # iterate the 5-fold 
        for train, test in kf.split(Xpoly5): 
            model.fit(Xpoly5[train], y[train]) 

            ypred_train = model.predict(Xpoly5[train]) 
            temp_train.append(mean_squared_error(y[train], ypred_train))

            ypred_test = model.predict(Xpoly5[test]) 
            temp_test.append(mean_squared_error(y[test], ypred_test))

        train_mean_error.append(np.array(temp_train).mean())
        train_std_error.append(np.array(temp_train).std())
        test_mean_error.append(np.array(temp_test).mean()) 
        test_std_error.append(np.array(temp_test).std())

    plt.errorbar(Crange, train_mean_error, yerr=train_std_error, linewidth=3, label='Train Mean MSE with error bars') 
    plt.errorbar(Crange, test_mean_error, yerr=test_std_error, linewidth=3, label='Test Mean MSE with error bars') 
    plt.xlabel('C') 
    plt.ylabel('Mean square error')
    plt.legend(loc='best')
    plt.show()

drawErrorBarRidge([0.1, 1, 10, 100])
drawErrorBarRidge([0.1, 0.5, 1, 10])
drawErrorBarRidge([0.1, 0.5, 0.75, 1])
