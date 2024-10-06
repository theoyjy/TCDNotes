import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
import matplotlib.pyplot as plt


def FindKForkNNClassifier():
    m = 25
    Xtrain = np.linspace(0.0,1.0,num=m)
    ytrain = np.sign(Xtrain-0.5+np.random.normal(0,0.2,m))
    Xtrain = Xtrain.reshape(-1, 1)

    model = KNeighborsClassifier(n_neighbors=3,weights='uniform').fit(Xtrain, ytrain)

    Xtest=np.linspace(0.0,1.0,num=1000).reshape(-1, 1)
    ypred = model.predict(Xtest)
    plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred, color='green')
    plt.xlabel("input x"); plt.ylabel("output y")
    plt.legend(["predict","train"])
    plt.show()

    model = KNeighborsClassifier(n_neighbors=7,weights='uniform').fit(Xtrain, ytrain)
    ypred = model.predict(Xtest)
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred, color='green')
    plt.xlabel("input x"); plt.ylabel("output y")
    plt.legend(["predict","train"])
    plt.show()

# FindKForkNNClassifier()

m = 25
Xtrain = np.linspace(0.0,1.0,num=m)
ytrain = 10* Xtrain + np.random.normal(0.0,1.0,m)
Xtrain = Xtrain.reshape(-1, 1)
Xtest=np.linspace(0.0,1.0,num=1000).reshape(-1, 1)

def FindKForkNNRegression():    
    model = KNeighborsRegressor(n_neighbors=3,weights='uniform').fit(Xtrain, ytrain)
    
    ypred = model.predict(Xtest)
    plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred, color='green')
    plt.xlabel("input x"); plt.ylabel("output y"); plt.legend(["predict","train"])
    plt.show()
    
    model2 = KNeighborsRegressor(n_neighbors=7,weights='uniform').fit(Xtrain, ytrain)
    ypred2 = model2.predict(Xtest)
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred2, color='blue')
    plt.xlabel("input x"); plt.ylabel("output y"); plt.legend(["predict","train"])
    plt.show()


def gaussian_kernel100(distances):
    weights = np.exp(-100*(distances**2))
    return weights/np.sum(weights)
def gaussian_kernel1000(distances):
    weights = np.exp(-1000*(distances**2))
    return weights/np.sum(weights)

def gaussian_kernel10000(distances):
    weights = np.exp(-10000*(distances**2))
    return weights/np.sum(weights)

def FindGaussianKernel():
    model2 = KNeighborsRegressor(n_neighbors=7,weights=gaussian_kernel100).fit(Xtrain, ytrain)
    ypred2 = model2.predict(Xtest)
    model3 = KNeighborsRegressor(n_neighbors=7,weights=gaussian_kernel1000).fit(Xtrain, ytrain)
    ypred3 = model3.predict(Xtest)
    model4 = KNeighborsRegressor(n_neighbors=7,weights=gaussian_kernel10000).fit(Xtrain, ytrain)
    ypred4 = model4.predict(Xtest)
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred2, color='blue')
    plt.plot(Xtest, ypred3, color='orange')
    plt.plot(Xtest, ypred4, color='green')
    plt.xlabel("input x"); plt.ylabel("output y")
    plt.legend(["train","k=7,gamma=100","k=7,gamma=1000","k=7,gamma=10000"])
    plt.show()


# FindKForkNNRegression()
# FindGaussianKernel()

def DecisionTree():
    m = 25
    Xtrain = np.linspace(0.0,1.0,num=m)
    ytrain = np.sign(Xtrain-0.5+np.random.normal(0,0.2,m))
    Xtrain = Xtrain.reshape(-1, 1)

    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier().fit(Xtrain, ytrain)

    Xtest=np.linspace(0.0,1.0,num=1000).reshape(-1, 1)
    ypred = model.predict(Xtest)

    from sklearn.tree import export_text
    print(export_text(model))

    from sklearn.tree import plot_tree
    plot_tree(model, fontsize=4, impurity=False, class_names=['-1','+1'])
    plt.show()
    plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred, color='green')
    plt.xlabel("input x"); plt.ylabel("output y")
    plt.legend(["predict","train"])
    plt.show()

    model = DecisionTreeClassifier(max_depth=1).fit(Xtrain, ytrain)
    ypred = model.predict(Xtest)
    plot_tree(model, fontsize=4, impurity=False, class_names=['-1','+1'])
    plt.show()
    plt.scatter(Xtrain, ytrain, color='red', marker='+')
    plt.plot(Xtest, ypred, color='green')
    plt.xlabel("input x"); plt.ylabel("output y")
    plt.legend(["predict","train"])
    plt.show()

# DecisionTree()

def NeuralNetwork():
    import pandas as pd
    df = pd.read_csv("D:\Code\TCDNotes\Machine Learning\Lectures\week04\week2.csv",sep=',')
    x1=df.iloc[:,0]
    x2=df.iloc[:,1]
    X=np.column_stack((x1,x2))
    y=df.iloc[:,2]

    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=1)

    plt.rc('font', size=18);plt.rcParams['figure.constrained_layout.use'] = True
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import cross_validate
    crossval=False
    hidden_layer_range = [1,2,3,4,5,10,15,25]

    if crossval:
        mean_error=[]; std_error=[]; mean_error1=[]; std_error1=[]
        for n in hidden_layer_range:
            print("hidden layer size %d\n"%n)
            model = MLPClassifier(hidden_layer_sizes=(n), alpha=1, max_iter=500)
            scores = cross_validate(model, X, y, cv=5, return_train_score=True, scoring='roc_auc')
            mean_error.append(np.array(scores['test_score']).mean()); std_error.append(np.array(scores['test_score']).std())
            mean_error1.append(np.array(scores['train_score']).mean()); std_error1.append(np.array(scores['train_score']).
            std())
        plt.errorbar(hidden_layer_range,mean_error,yerr=std_error,linewidth=3)
        plt.errorbar(hidden_layer_range,mean_error1,yerr=std_error1,linewidth=3)
        plt.xlabel('#hidden layer nodes'); plt.ylabel('AUC')
        plt.legend(['Test Data', 'Training data'])
        plt.show()

    mean_error=[]; std_error=[]; mean_error1=[]; std_error1=[]
    C_range = [0.001,0.01,0.1,0.5,1,2,5,10]
    for C in C_range:
        print("C %d\n"%C)
        model = MLPClassifier(hidden_layer_sizes=(2), alpha = 1.0/C)
        scores = cross_validate(model, X, y, cv=5, return_train_score=True, scoring='roc_auc')
        mean_error.append(np.array(scores['test_score']).mean()); std_error.append(np.array(scores['test_score']).std())
        mean_error1.append(np.array(scores['train_score']).mean()); std_error1.append(np.array(scores['train_score']).std())
    plt.errorbar(hidden_layer_range,mean_error,yerr=std_error,linewidth=3)
    plt.errorbar(hidden_layer_range,mean_error1,yerr=std_error1,linewidth=3)
    plt.xlabel('C'); plt.ylabel('AUC')
    plt.legend(['Test Data', 'Training data'])
    plt.show()

    from sklearn.neural_network import MLPClassifier
    model = MLPClassifier(hidden_layer_sizes=(2), alpha=1.0).fit(Xtrain, ytrain)
    preds = model.predict(Xtest)
    from sklearn.metrics import confusion_matrix
    print(confusion_matrix(ytest, preds))
    from sklearn.dummy import DummyClassifier
    dummy = DummyClassifier(strategy="most_frequent").fit(Xtrain, ytrain)
    ydummy = dummy.predict(Xtest)
    print(confusion_matrix(ytest, ydummy))
    from sklearn.metrics import roc_curve
    preds = model.predict_proba(Xtest)
    print(model.classes_)
    fpr, tpr, _ = roc_curve(ytest,preds[:,1])
    plt.plot(fpr,tpr)
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(C=10000).fit(Xtrain, ytrain)
    fpr, tpr, _ = roc_curve(ytest,model.decision_function(Xtest))
    plt.plot(fpr,tpr,color='orange')
    plt.legend(['MLP','Logistic Regression'])
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.plot([0, 1], [0, 1], color='green',linestyle='--')
    plt.show()

NeuralNetwork()