import numpy as np 
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