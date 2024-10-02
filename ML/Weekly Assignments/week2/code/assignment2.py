import matplotlib.pyplot as plt

# association function of plotting linear decision boundary of a model
def pltLinearBoundary(model):
    x1 = np.linspace(-1, 1, 100)
    # y = intercept + weight1*X1 + weight1*X2
    # the desicion boundary is the line where y = 0
    # 0 = intercept + weight1*X1 + weight2*X2
    # X2 = - (intercept + weight1*X1) / weight2
    plt.plot(x1, -(model.intercept_ + model.coef_[0][0]*x1)/model.coef_[0][1], color='black', label='Decision Boundary')

# association function of plotting predictions of a model
def pltPredictions(x_test, y_pred):
    predict_postive = x_test[y_pred == 1]
    predict_negative = x_test[y_pred == -1]
    plt.scatter(predict_postive[:, 0], predict_postive[:, 1], color="red", marker='^', label='+1 Prediction')
    plt.scatter(predict_negative[:, 0], predict_negative[:, 1], color="orange", marker='v', label='-1 Prediction')

import numpy as np
import pandas as pd
df = pd.read_csv("week2.csv",sep=',')
x1=df.iloc[:,0]
x2=df.iloc[:,1]
x=np.column_stack((x1,x2))
y=df.iloc[:,2]

x_with_positive_y = x[y == 1]
x_with_negative_y = x[y == -1]

# (a)
# (i) Plot the points
plt.scatter(x_with_positive_y[:, 0], x_with_positive_y[:, 1], color='#00ff00', marker='+', label='+1 Data')
plt.scatter(x_with_negative_y[:, 0], x_with_negative_y[:, 1], color='#0000fd', marker='o', label='-1 Data')
plt.rc('font', size=18)
plt.xlabel('X_1'); plt.ylabel('X_2')
plt.legend(loc='upper right')
plt.show()

# (ii) Train a logistic regression model and report the coefficients and the intercept
from sklearn.model_selection import train_test_split
# split data into 80% train and 20% test data sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
train_positive = x_train[y_train == 1]
train_negative = x_train[y_train == -1]

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)
print("logisticRegression:")
print("coefficients: ", model.coef_[0])
print("intercept: ", model.intercept_)

# (iii)
# plot original data
plt.scatter(x_with_positive_y[:, 0], x_with_positive_y[:, 1], color='#00ff00', marker='+', label='+1 Data')
plt.scatter(x_with_negative_y[:, 0], x_with_negative_y[:, 1], color='#0000fd', marker='o', label='-1 Data')

# predict by logistic regression model
y_pred = model.predict(x_test)

# Plot the predictions of the logistic regression model
pltPredictions(x_test, y_pred)

# Plot the decision boundary of the logistic regression model
pltLinearBoundary(model)

plt.xlabel('X_1'); plt.ylabel('X_2')
plt.legend(loc='upper right', fontsize = 10)
plt.show()  

# (iv) Report the accuracy
from sklearn.metrics import accuracy_score
print("Accuracy: ", accuracy_score(y_test, y_pred))


# (b)
# (i) Train LinearSVC model with different penalties
from sklearn.svm import LinearSVC
penalties = [0.001, 1, 100]
for p in penalties:
    # train LinearSVC with each penalty value on train data
    model = LinearSVC(C=p, dual='auto').fit(x_train, y_train)
    # report model parameters
    # predict on test data
    y_pred = model.predict(x_test)
    print("Penalty: ", p, " Coefficients: ", model.coef_, " Intercept: ", model.intercept_)
    print("Accuracy: ", accuracy_score(y_test, y_pred))

# (ii) plot predictions and training data together
    # plot original data
    plt.scatter(x_with_positive_y[:, 0], x_with_positive_y[:, 1], color='#00ff00', marker='+', label='+1 Data')
    plt.scatter(x_with_negative_y[:, 0], x_with_negative_y[:, 1], color='#0000fd', marker='o', label='-1 Data')

    # plot predictions
    pltPredictions(x_test, y_pred)

    # plot boundary
    pltLinearBoundary(model)
    plt.xlabel('X_1'); plt.ylabel('X_2')
    plt.legend(loc='upper right', fontsize = 10)
    plt.show()

# (c)
# (i)
# insert x1^2 x2^2 to train dataset
x1_train = x_train[:,0]
x2_train = x_train[:,1]
x_train_4_features = x_train
x_train_4_features = np.insert(x_train_4_features, 2, values = x1_train*x1_train, axis = 1)
x_train_4_features = np.insert(x_train_4_features, 3, values = x2_train*x2_train, axis = 1)

# train logistic regression model with 4 features
model = LogisticRegression()
model.fit(x_train_4_features, y_train)
print("LogisticRegression with 4 features:\nCoefficients: ", model.coef_, " Intercept: ", model.intercept_)


# (ii) 
# insert x1^2 x2^2 to test dataset
x1_test = x_test[:, 0]
x2_test = x_test[:, 1]
x_test_4_features = x_test
x_test_4_features = np.insert(x_test_4_features, 2, values = x1_test*x1_test, axis = 1)
x_test_4_features = np.insert(x_test_4_features, 3, values = x2_test*x2_test, axis = 1)

# plot original data
plt.scatter(x_with_positive_y[:, 0], x_with_positive_y[:, 1], color='#00ff00', marker='+', label='+1 Data')
plt.scatter(x_with_negative_y[:, 0], x_with_negative_y[:, 1], color='#0000fd', marker='o', label='-1 Data')

# predict on test data
y_pred = model.predict(x_test_4_features)
pltPredictions(x_test_4_features, y_pred)

plt.xlabel('X_1'); plt.ylabel('X_2')
plt.legend(loc='upper right', fontsize = 10)
plt.show()

# (iii) train dummy classifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print("Logistic Regression on 4 Feature Accuracy: ", accuracy_score(y_test, y_pred))
from sklearn.dummy import DummyClassifier
dummy = DummyClassifier(strategy='most_frequent').fit(x_train_4_features, y_train)
base_pred = dummy.predict(x_test_4_features)
print("Dummy Classifier Accuracy: ", accuracy_score(y_test, base_pred))

# (iv) draw the decision boundary
# plot original data
plt.scatter(x_with_positive_y[:, 0], x_with_positive_y[:, 1], color='#00ff00', marker='+', label='+1 Data')
plt.scatter(x_with_negative_y[:, 0], x_with_negative_y[:, 1], color='#0000fd', marker='o', label='-1 Data')

# plot curve decision boundary
coef = model.coef_[0]
intercept = model.intercept_[0]
x1_values = np.linspace(-1, 1, 10000)

# x2 equals to the solution of the quadratic equation with respect to x1
discriminant = coef[1]**2 - 4 * coef[3] * (intercept + coef[0] * x1_values + coef[2] * x1_values**2)
x2_values = (-coef[1] + np.sqrt(discriminant)) / (2 * coef[3])

plt.plot(x1_values, x2_values, label='Decision Boundary', color='black')
plt.xlabel('X_1'); plt.ylabel('X_2')
plt.legend(loc='upper right', fontsize = 10)
plt.show()