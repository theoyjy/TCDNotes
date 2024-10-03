# Model Selection
## 1. Cross validation
*Test how well the model generalizes*
- Split training data into E.g. 20% is test data, 80% is training data.
- Typically split the data randomly. So as avoid inadvertently 无意间 introducing bias.

```python
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.2)
```

### K-fold cross validation

>[!info] K-fold cross-validation
>* divide data into k equal sized parts
>* use part 1 as test, the rest as training data
>* use part 2 as test data, rest as training data
>* ...
>* This gives k estimates of $J(\theta)$, so we can use this to estimate the average and  the spread of the data

```python
from sklearn.model_selection import cross_val_score 
scores = cross_val_score(model, X, y, cv=5, scoring=’neg_mean_squared_error’) 
print(scores) 
print(”Accuracy: %0.2f (+/− %0.2f)” % (scores.mean(), scores.std())) 

from sklearn.model_selection import KFold kf = KFold(n_splits=5) 
for train, test in kf.split(X): 
	from sklearn.linear_model import LinearRegression 
	model = LinearRegression().fit(X[train], y[train]) 
	ypred = model.predict(X[test])
	from sklearn.metrics import mean_squared_error 
	print(”intercept %f, slope %f, square error %f”%(model.intercept_, model.coef_,mean_squared_erro
```

>[!question] how to choose k
>* usually 5 or 10
>* The test data is noisy
>* The training data is noisy and so the learned model parameters change from one set of training data to another
>* We want to use as much data as possible to train the model, so that we learn representative parameter values
>* Also, as k increases the computation times increases (remember we need to fit the model k times), so don’t want k to be too large.

## 2. Add Penalty - Tuning Model Hyperparameters

To prevent linear regression overfit the training data which capture noise, **add a penalty to the model's complexity by constraining the coefficients**.
![[wk03 Cross-Validation & Regularization-20240926162611841.webp|500]]

* to choose value of C, use cross validation for each C and plot distribution of prediction error.
* *increase C by factor of 5 or 10 so can quickly scan across a large range* e.g. [0.1,1,10,100] or [0.1, 0.5, 1, 5, 10, 50, 100]

### polynomial features

*If the data is quadratic plus noise, but we don't know that*
we can use 
```python
Xpoly = PolynomialFeatures(q).fit_transform(X) 
```
to generate polynomial data. In this way, we can apply linear regression to see find out the relationship between features and targets

```python
import numpy as np 
X = np.arange(0,1,0.01).reshape(−1, 1) 
y = 10* (X** 2) + np.random.normal(0.0,1.0,X.size).reshape(−1, 1) 

from sklearn.model_selection import KFold 
kf = KFold(n_splits=5) 
import matplotlib.pyplot as plt 
plt.rc(’font’, size=18); plt.rcParams[’figure.constrained_layout.use’] = True

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
		if ((q==1) or (q==2) or (q==6)) and not plotted: 
			plt.scatter(X, y, color=’black’) 
			ypred = model.predict(Xpoly) 
			plt.plot(X, ypred, color=’blue’, linewidth=3) 
			plt.xlabel(”input x”); plt.ylabel(”output y”) 
			plt.show() plotted = True 
			mean_error.append(np.array(temp).mean()) 
			std_error.append(np.array(temp).std()) 
plt.errorbar(q_range,mean_error,yerr=std_error,linewidth=3) 
plt.xlabel(’q’) 
plt.ylabel(’Mean square error’) 
plt.show()
```

>[!Caution] Errors fluctuate as q increases on training data and Test data: 
>1. On training data:
>	As q increases, it can fit better and better on training data, so the error decreases
>	
>2. On Test Data:
>	1. When q is too small, underfitted, can not capture the feature well, so more errors
>	2. When q is too large, overfitted, learning precisely on noise, this leads to poor generalization ability of the model, resulting in increased error on the test data.

#### `errorbar`
`plt.errorbar(x, y, yerr=error, fmt='o', ecolor='red', capsize=5)`
* 用于绘制带有**误差范围（误差条 `yerr`）的图表**，它不仅显示了数据点的值，还显示了这些点的不确定性或误差范围。
- `capsize`：误差条末端横线的长度。

### Apply hyperparameters to control the high degree of the polynomial.

>[!caution] 
>Remember ==increasing C -> decreases contribution of $\theta^T \theta / C$ penalty== to cost, so tend to revert to previous linear regression behaviour as C gets large.

## Summary - Model Selection

Two main approaches
### 1. Sequential Model Selection
   Keep repeating: add a new feature -> fit model -> use cross-validation to evaluate.
   Until predictions start to getting worse or improvement is small 
### 2.Regularization:
   Add penalty cost to cost function
Two common Regularization penalties:
#### 1. Quadratic/L2 Penalty
![[wk03 Cross-Validation & Regularization-20240926181741390.webp|200]]
Also called *Tikhonov regularisation*. **Encourages elements of θ to have small value.**
- Adding quadratic penalty to *linear regression cost function* → **ridge regression**, see above.
- A quadratic penalty is **always included in SVM cost function** 
- *Can add quadratic penalty to logistic regression* too.

#### L1 Penalty
![[wk03 Cross-Validation & Regularization-20240926181932175.webp|150]]
**Encourage sparsity of solution** i.e. few non-zero elements in $\theta$

The L1 penalty encourages the optimization process to **reduce some coefficients to zero completely**, especially those features that are less important or contribute little to predicting the target variable.

- When C is small, almost makes all coefficients to zero

---

# Evaluating Performance

>[!abstract] Basic rules
>To measure how well overall objectives are met by a proposed ML system
>1. Probably multiple metrics are of interest
>2. Goodhart's Law: when a measure becomes a target it ceases to be a good measure.
>	keep a focus on what outcomes really matter, rarely just minimising/maximising some metric(s)
>3. Establish a baseline: how well do existing solutions perform, what are comparable problems, and how have they been solved

## Choice of Metric for Regression
- **Mean Square Error (MSE)**:![[wk03 - Model Selection & Performance Evaluation-20240926185009605.webp|200]]
- **Root Mean Square Error (RMSE)**: ![[wk03 - Model Selection & Performance Evaluation-20240926185031096.webp|220]]
- **Mean Absolute Error (MAE)**: ![[wk03 - Model Selection & Performance Evaluation-20240926185110109.webp|180]]
  *Gives less weight to large errors than mean square error*
- $R^2$: ![[wk03 - Model Selection & Performance Evaluation-20240926185243237.webp|600]]

## Comparison with A Baseline Predictor
Even though We reach the lowest mean square error, that doesn't necessarily mean it's a good model.

>[!info] Compare the performance of our predictions against the performance of a **trivial baseline estimator**.
>- *the prediction is always a constant that doesn't depend on the input features at all.*
>	- `sklearn.dummy.DummyRegressor` and `DummyClassifier`
>- for example: A trivial constant model has lower error than our polynomial regression model!
>- But it doesn't always have to be a constant baseline model

>[!important] You should always compare the quality of any predictions with a simple baseline model
>This is mandatory in your projects and assignments

## Choice of Metric For Classification
![[wk03 - Model Selection & Performance Evaluation-20240926191606274.webp|600]]

>[!tip] There is a trade-off between true positives and false negatives.

### Imbalanced Data
For example 1000 cases, only 1 is positive, in this case, the prediction is nearly always the case. **accuracy(#correct predictions/total instances)** won't indicate well about if it's really good.

### Confusion Matrix

|               | Predicted positive | Predict negative |
| ------------- | ------------------ | ---------------- |
| True positive | TP                 | FN               |
| True negative | FP                 | TN               |
>[!important]
>- True positive rate(Recall): divide TP(predict P and it's P) over all positive data
>- False positive rate(Specificity): divide  FP(Predict P and is N) over all negative data
>- Accuracy: all correct over all data
>- Precision = TP over all predicted positive

![[wk03 - Model Selection & Performance Evaluation-20240926193133142.webp|600]]

![[wk03 - Model Selection & Performance Evaluation-20240926194118098.webp]]