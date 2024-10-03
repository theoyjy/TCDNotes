# Lec 1
Supervised machine learning
- classification
  Target values are *discrete*
- regression 
  Target values are *continues*

classifier(functions) train by training data to predict.
* when training/input data is a number vector, such as pixels in image, called **feature vector***
1. map from real data to numeric feature vector
2. train function h(x)
   
We need to label data
Data can be unrepresentative, noisy/unreliable, not useful relationship(correlation vs causation)

### example -- sensation of movie reviews
1. delete uninteresting words -- stop words
2. truncate word endings -- stemming-- get rid of the tense
3. map text of reviews to an array, `array["word"] = NumberOfAppearance`
4. Assign weight $\theta_{i}$ to work $i$

---
# Lec 2 - Linear Regression
$x$ input variables - *independent* variable
$y$ target values - *dependent* variable
$\theta_{0} \quad \theta_{1}$ are unknown parameters
* (Hypothesis) Prediction: $y = h_{\theta}(x) = \theta_{0} + \theta_{1}x$
* Idea is to choose $\theta_{0}$ and $\theta_{1}$ so that $h_{\theta_{0}}(x^{(i)})$ is close to $y^{i}$ for each of our training examples
* **Cost function(Mean Squared Error)** Least square case :
  ![[wk01-20240913121715773.webp|292]]
  - $m$ is the number of training examples
* (Goal) Optimization: select the values for θ0 and θ1 that minimize cost function

### Gradient Descent - optimization algorithm

>[!info]
>* start with some $\theta_{0}$ and $\theta_{1}$
>* Repeat: update params to new values which makes $J(\theta_{0}, \theta_{1})$ smaller:
>  **Stopping criteria**: stop when decreases by less than e.g. 10−2 or after a fixed number of iterations e.g. 200, whichever comes first
>* The curve may have multiple local minimum, converge to that, global minimum may be unachievable
>##### Select Step Size
>- too small -> long time
>- too large -> overshoot the minimum
>- adjust step $\alpha$ at each iteration
>The number of steps taking can be considered as the **learning rate**, and this is how fast the algo converges to the minima.

#### Derivatives is the slope
So for equation with multiple variables, we have multiple slopes
![[wk01-20240917172720277.webp|600]]
To find the lowest point (local minimum), you need to go downhill. By moving in the opposite direction of the gradient at each step, you're gradually descending the hill.
![[wk01-20240917180052199.webp|600]]

### Normalization both $x$ and $y$
If the range of data is too large, the larger valued data tends to dominate cost function and training focusses on the data
![[wk01-20240917180759966.webp|551]]
- $\mu_j$ is the **mean** of feature $x_{j}$, and subtracting it helps to center the feature around zero.
- $\sigma_j$​ is the **standard deviation (scaling factor)**, and dividing by it ensures the feature values lie in a reasonable range, typically `[-1, 1]`.
- The statement "do not apply to $x_0=1$" refers to leaving the bias term $x_0$ unchanged, as it's conventionally set to 1.

### sklearn basic

```python
from sklearn.linear_model import LinearRegression
import numpy as np
Xtrain = np.arange(0,1,0.01).reshape(-1, 1)

# mean is 0
# standard deviation is 1, so the range is (-1, 1)
# 100 samples
ytrain = 10*Xtrain + np.random.normal(0.0,1.0,100).reshape(-1, 1)
model = LinearRegression().fit(Xtrain, ytrain)
print(model.intercept_, model.coef_)
```

>[!tip] APIs
>* `arange(start, end, step)`: generate numbers for an array
>* `reshape(#rows, #cols)`: -1 means as many as it needs
>* `np.random.normal(mean, standard deviation, $random samples)`: 
>**normal(Gaussian) distribution**: the data range would be ($\mu -\sigma$, $\mu + \sigma$)

















