### Logistic Regression with 2 Classes

>[!definition] Logistic regression:
>**Binary Output**: Logistic regression is mainly used when the output variable (target) is binary, such as 0 or 1, true or false, positive or negative
>
>**Logistic Function (Sigmoid)**: Logistic regression uses a special function called the **sigmoid function** (or logistic function) to map any real-valued number into a probability range of 0 to 1

- Still use the linear compositions of $\theta$ like linear regression, but results in 2 classes
- In classification, $y$ often referred to as the **label** 
- The **Classifier** is to predict the label of a new object

>[!important] Decision Boundary
>Model: $sign(\theta^T x)$ predict output $+1$ when $\theta^T x > 0$ and output $-1$ when  $\theta^T x < 0$

- When data can be separate by a line like $0.5x_1 - 0.5x_2 > 0$, we say that it's *linear separatable*

>[!info] Cost Function: 0-1 loss function
>![[wk02 - Logistic regression & SVM-20240917231746652.webp|557]]

>[!challenge] Gradient Descent

### SMV - Logistic Regression with Multiple Classes

>[!tip] Convert multi classes problem into 2 classes problem
>![[wk02 - Logistic regression & SVM-20240917233725321.webp]]
>Train a classifier $sign(\theta^T x)$ for each class $i$ to predict the probability that $y=i$. **Re-label** data as $y = -1$ when $y != i$

#### hinge loss function
![[wk02 - Logistic regression & SVM-20240920121131603.webp|400]]
1. Not smooth -- un-differentiable
2. assign zero penalty to all values of $\theta$ which ensures $\theta^T x >= 1$ when $y = 1$ and  $\theta^T x <= -1$ when $y = 1$

#### Gradient Descent for SVMs
![[wk02 - Logistic regression & SVM-20240920121511614.webp]]

### Feature Engineering
When encounter **non-linear curves**.

>[!tip] Changing Input Features:
>Basic idea:
>1. Process or transform them to produce new features
>	1. Modify individual features $x_i^{new} = (x_i - \mu_i) / \sigma_i$
>	2. Create multiple features from one original features 
>	   replace $x_i$ by $x_i, x_i^2, x_i^3, ...$
>	3. Create new feature from multiple original features
>	   Products can be used to model interaction between features $x_1 x_2$
>2. Use these new features in your predictor/model
>
>It's a good idea to train on both original features and new features, then evaluate their performance

>[!info] Choosing outputs
> convert the equation to linear, for example: 
>![[wk02 - Logistic regression & SVM-20240920123530839.webp|500]]

>[!caution] Under or Over -fitting
>* If too many features -> fit all the up and downs -> cause "noise"-> overfitting
>* too less -> capture not enough behavior -> underfitting
>* Model Selection









### Sklearn
```python
import numpy as np 
Xtrain = np.random.uniform(0,1,100)
# Xtrain > 0.5 would be positive
# Xtrain < 0.5 would be negative
ytrain = np.sign(Xtrain−0.5)
Xtrain = Xtrain.reshape(−1, 1) 

from sklearn.linear\_model import 
LogisticRegression model = LogisticRegression(penalty=’none’,solver=’lbfgs’) 
model.fit(Xtrain, ytrain) 
print(”intercept %f, slope %f”%(model.intercept_, model.coef_))
```


- `np.random.uniform(low, high, size)`:
  The uniform distribution is a type of probability distribution in which all outcomes are equally likely within a specified range.
- `np.sign(x)`