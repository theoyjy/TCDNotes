import numpy as np 
def func1():
	X = np.arange(0,1,0.01).reshape(-1, 1) 
	y = 10* (X** 2) + np.random.normal(0.0,1.0,X.size).reshape(-1, 1) 

	from sklearn.model_selection import KFold 
	kf = KFold(n_splits=5) 
	import matplotlib.pyplot as plt 
	plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True

	mean_error=[]; std_error=[] 
	q_range = [1,2,3,4,5,6] 
	for q in q_range: 
		from sklearn.preprocessing import PolynomialFeatures 
		Xpoly = PolynomialFeatures(q).fit_transform(X) 
		from sklearn.linear_model import LinearRegression 
		model = LinearRegression() 
		temp=[]; 
		plotted = False 
		for train, test in kf.split(Xpoly): 
			model.fit(Xpoly[train], y[train]) 
			ypred = model.predict(Xpoly[test]) 
			from sklearn.metrics import mean_squared_error 
			temp.append(mean_squared_error(y[test],ypred))
			# if not plotted: 
			# 	plt.scatter(X, y, color='black') 
			# 	ypred = model.predict(Xpoly) 
			# 	plt.plot(X, ypred, color='blue', linewidth=3) 
			# 	plt.xlabel("input x"); plt.ylabel("output y") 
			# 	plt.show() 
			# 	plotted = True
		mean_error.append(np.array(temp).mean()) 
		std_error.append(np.array(temp).std()) 

	plt.errorbar(q_range,mean_error,yerr=std_error,linewidth=3) 
	plt.plot(q_range, [0,0,0,0,0,0], color='orange', linestyle='-')
	plt.xlabel('q') 
	plt.ylabel('Mean square error') 
	plt.show()

def BaselinePredictor():
	#-1 means the dimension is inferred and will be decided by the data and another dimension
	# 1 means the size of the dimension is 1
	X = np.arange(0,1,0.01).reshape(-1, 1) # N row and 1 column, which is 1D to 2D
	y = np.random.normal(0.0,1.0,X.size).reshape(-1, 1)
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
	from sklearn.preprocessing import PolynomialFeatures
	Xtrain_poly = PolynomialFeatures(6).fit_transform(X_train)
	Xtest_poly = PolynomialFeatures(6).fit_transform(X_test)
	X_poly = PolynomialFeatures(6).fit_transform(X)

	from sklearn.linear_model import LinearRegression
	model = LinearRegression().fit(Xtrain_poly, y_train)

	ypred = model.predict(Xtest_poly)

	from sklearn.dummy import DummyRegressor
	dummy = DummyRegressor(strategy="mean").fit(Xtrain_poly, y_train)
	ydummy = dummy.predict(Xtest_poly)

	from sklearn.metrics import mean_squared_error
	print("square error %f %f"%(mean_squared_error(y_test, ypred), mean_squared_error(y_test, ydummy)))

	import matplotlib.pyplot as plt
	plt.scatter(X_test, y_test, color="black", label = "data")
	ypred = model.predict(X_poly)
	plt.scatter(X, ypred, color = "blue", label="LinearRegression")
	plt.xlabel("input x")
	plt.ylabel("output y")
	plt.legend(["training data", "predictions"])
	plt.show()

def MeasureMetrics():
	# Generate random data
	X = np.arange(0, 1, 0.01).reshape(-1, 1)
	y = np.random.choice([0, 1], size=X.shape[0]).reshape(-1, 1)  # Binary class labels
	
	from sklearn.model_selection import train_test_split
	Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=1)
	
	from sklearn.svm import LinearSVC
	model = LinearSVC(C=1.0).fit(Xtrain, ytrain)
	preds = model.predict(Xtest)

	from sklearn.metrics import confusion_matrix
	print(confusion_matrix(ytest, preds))

	from sklearn.metrics import classification_report
	print(classification_report(ytest, preds))

	from sklearn.dummy import DummyClassifier
	dummy = DummyClassifier(strategy='most_frequent').fit(Xtrain, ytrain)
	ydummy = dummy.predict(Xtest)
	print(confusion_matrix(ytest, ydummy))
	print(classification_report(ytest, ydummy))
	mean_error=[]
	std_error=[]
	Ci_range = [0.01, 0.1, 1, 5, 10, 25, 50, 100]
	for Ci in Ci_range:
		from sklearn.svm import LinearSVC
		model = LinearSVC(C=Ci)
		from sklearn.model_selection import cross_val_score
		scores = cross_val_score(model, X, y, cv=5, scoring='f1') # can change score to auc
		mean_error.append(np.array(scores).mean())
		std_error.append(np.array(scores).std())
	import matplotlib.pyplot as plt
	plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
	plt.errorbar(Ci_range,mean_error,yerr=std_error,linewidth=3)
	plt.xlabel('Ci'); plt.ylabel('F1 Score')
	plt.show()

MeasureMetrics()

def ROCcurve():
	import matplotlib.pyplot as plt
	plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
	from sklearn.model_selection import train_test_split
	# Generate random data
	X = np.arange(0, 1, 0.01).reshape(-1, 1)
	y = np.random.choice([0, 1], size=X.shape[0]).reshape(-1, 1)  # Binary class labels
	Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)
	
	from sklearn.svm import LinearSVC
	model = LinearSVC(C=1.0).fit(Xtrain, ytrain)
	from sklearn.metrics import roc_curve
	fpr, tpr, _ = roc_curve(ytest,model.decision_function(Xtest))
	plt.plot(fpr,tpr)
	plt.xlabel('False positive rate')
	plt.ylabel('True positive rate')
	plt.plot([0, 1], [0, 1], color='green',linestyle='--')
	plt.show()

ROCcurve()