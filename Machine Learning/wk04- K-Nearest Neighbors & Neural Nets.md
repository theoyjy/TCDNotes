
## Linear and Logistic Regression Summary
- Model $\hat{y}=h_\theta(x)$
	- $\hat{y}=\theta_T x$ (regression)
	- $\hat{y}=sign(\theta^T x)$(classification)
- Input features x is a vector of real numbers 
- Prediction $h_\theta(x)$ is a real number (regression) or an integer (classification)

*Solve problem for now mostly be like:*
- Use linear models
- Add nonlinearity via feature engineering
- Easy and fast to train → cost function is convex in parameters. 
- Scale well, can be used with pretty big data. 
- Interpretable, sort of: ∗ 
	- Magnitude of parameter $\theta_j$ tells how important the $j$’th input feature is (if θj v small maybe can delete $j$’th feature) 
	- Sign of $\theta_j$ tells whether prediction tends to increase/decrease with $j$’th feature. 
	- ... this assumes $j$’th feature itself has a reasonable interpretation 
- SVMs and logistic regression generally perform much the same

# k-Nearest Neighbors(kNN)

>[!definition] kNN makes predictions based directly on the training data

## Steps
**Given feature vector $x$(that you want to make prediction)**
1. For each training data point i, calculate distance $d(x^{(i)}, x)$ between feature vector $x^{(i)}$and $x$
2. Select the *k* training data that are closest to $x$
3. Predict output $y$ using the outputs $y^{(i)}$ for these *k* closest training points>
	1. In a classification problem, taking majority vote from *k* training points
	2. In a regression problem, calculate the average of the $y^{(i)}$ from the *k* closest training points and use that as prediction

## 4 Basic Elements
1. A Distance metrics, typically Euclidean 欧几里得，两点的直线距离
   ![[wk04- K-Nearest Neighbors & Neural Nets-20241005233606056.webp|250]]
2. The number of k (usually decided by using cross-validation)
3. Weighting of neighbor points e.g. *uniform w(i) = 1* or Gaussian ![[wk04- K-Nearest Neighbors & Neural Nets-20241005233723555.webp|150]](*attach less weight to training points that are further away from query point x as $\gamma$ **gamma** increases*).
	1. $\gamma$ usually decided by using cross-validation
	2. $w(i)=e^{\gamma d(x^{(i)}, x)^2}$ where $\gamma = \frac {1} {2\sigma^2}$, sigma is the standard division(scaling factor)
4. Method for aggregating the k neighbor points $N_k$
   ![[wk04- K-Nearest Neighbors & Neural Nets-20241005233843372.webp|500]]


>[!example]
>![[wk04- K-Nearest Neighbors & Neural Nets-20241005234519896.webp]]

>[!warning] Relationship between Parameters and Prediction
>1. **K** number of neighbors
>	- Increasing k will tend to smooth out the function, decreasing k to make it more complex 
>	- Increasing k tends to cause under-fitting, decreasing k to cause over-fitting. Choose k by cross-validation.
>2. **w(i)** weights of neighbors
>   ![[wk04- K-Nearest Neighbors & Neural Nets-20241006151829559.webp|400]]
>	- Decreasing sigma $\sigma$ -> would increase $\gamma$ -> the "spread" is narrow, higher weight to the closest points and ignoring the most distant points -> **less smooth = rougher = sharper**
>	- Increasing $\sigma$ -> decreases $\gamma$-> **smoother**

## Summary
- easy to use
- need to choose distance function and weighting
- **small data only** -> each prediction requires a search over training data to find k nearest neighbors, this becomes expensive/slow when there is a lot of training data


# Decision Tree Classifier

> Model uses **if-then rules**
![[wk04- K-Nearest Neighbors & Neural Nets-20241006153209868.webp]]

>[!tip]
>1. Control *complexity* of model by *limiting tree depth* -- choose by cross-validation
>>Why it matters: Simplicity is one of the advantages of decision trees, but that simplicity can disappear as the tree grows too large. This is why controlling the size of the tree is important in real-world applications.
>2. NP-hard, special-purpose algorithms are used(Not gradient descent)
>>- **Why NP-hard**: In a decision tree, each split is a choice between multiple features and possible values. The number of possible trees you can create increases exponentially as the number of features and data points grows, making it very difficult to find the "best" tree.
>>- **Special-purpose algorithms**: Due to the NP-hard, machine learning algorithms use **heuristic methods(approximations)** rather than brute-force search. Algorithms like **CART (Classification and Regression Trees)** or **ID3** (Iterative Dichotomiser 3) are used to find a "good enough" tree efficiently.
>>- **Not gradient descent**: decision tree doesn't use gradient descent to minimize the errors. Instead, they rely on techniques like *greedy splitting* - choosing the best split based on criteria like information gain or Gini impurity
>3. Decision trees often used as an ensemble  
>> Usually *combining multiple models to create a stronger model.* such as random forest. Since a single decision tree can easily grow too complex and overfit the data, capturing noise rather than true patterns
>> 
>> **Random forest**: To overcome this, decision trees are often used in **forests**—*multiple trees are built using different subsets* of the data and features, and their predictions are averaged (for regression) or voted on (for classification). This helps **reduce overfitting** and improves the model’s generalization to new data.

# Neural Networks
Neural networks are particularly good at solving problems where the *relationship between input and output is complex, non-linear, or difficult to define with simple rules*.

>[!definition] Take the weighted sum of the inputs x1, x2 etc. and then apply function f to result.
>![[wk04- K-Nearest Neighbors & Neural Nets-20241006155723917.webp|500]]


## Multi-layer Perceptron

![[wk04- K-Nearest Neighbors & Neural Nets-20241006155655897.webp|400]]
1. input layer
2. hidden layer $z_1$ $z_2$
3. output layer
- $f$ is called the *activation* function, $g$ is the *output* function.
- No restricted to the number of nodes in hidden layer, also number of outputs

### Choices of Activation & Output Function
- **ReLU (Rectified纠正的 Linear Unit)** $f(x) = max(0, x)$
	- simple and quick to compute
	- can lead to "dead" neurons where output is always zero -> *leaky ReLU*
- **Sigmoid** $g(x) = \frac {e^x} {1+e^x}$ 
	- Used when output is a probability (0~1).
	- For classification problems +1 when g(x) > 0.5
- **tanh** $g(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$
	- older activation function, less commonly used now
![[wk04- K-Nearest Neighbors & Neural Nets-20241006161327386.webp|400]]

## Cost Function & Regularisation

1. $L_2$ penalty i.e. the sum of the squared weights/parameters
2. Nowadays more common to use *dropout* regularization
	- sets the output of certain neurons (nodes) to zero at each training step
	- typically remove about 50% of nodes
	- This is similar to weighted $L_2$ penalty $\sum_{i=1}^n{W_i \theta_i}$ 
	- During testing (or inference), dropout is not applied. Instead, the full network is used, but the weights are scaled down to account for the dropout during training.
	- **Benefits**: Reduces overfitting by discouraging complex co-adaptations of neurons.

### Training Neural Network: Stochastic 随机 Gradient Descent

**Gradient Descent**: A method to minimize the cost function by adjusting the weights step-by-step in the direction that reduces the error.
- repeat ![[wk04- K-Nearest Neighbors & Neural Nets-20241006165249944.webp|150]] for each weights
	- where $\alpha$ is the learning rate controlling how big the steps are in each update, where 
	- Use the *negative* gradient of changing to ensure that algorithm moves in the direction of minimizing the cost function, where:
	  ![[wk04- K-Nearest Neighbors & Neural Nets-20241006165059630.webp|400]]

### SGD
Instead of computing the gradient for the entire dataset, it updates the weights after using each training sample (or a small batch). This makes training faster but noisier.

- Repeat: Pick training data point i, e.g. randomly or by cycling through all data points.
  ![[wk04- K-Nearest Neighbors & Neural Nets-20241006165807564.webp|250]]
	- *At each update we use just one point from the training data*
	  ![[wk04- K-Nearest Neighbors & Neural Nets-20241006165920659.webp|400]]
- Fast and easy
- But need more iterations to minimize $J(\theta)$

#### SGD with Mini-batches
**Mini-batches** are often used for efficient parallelization.

![[wk04- K-Nearest Neighbors & Neural Nets-20241006170040657.webp|350]], where $I_q$ is a set of $q$ training data points.

![[wk04- K-Nearest Neighbors & Neural Nets-20241006171245115.webp|450]]
- k processors and mini-batch size q, so each processor processes q/k each time
- *Repeat several epochs until the model converges*:
  -  for each **epoch**, shuffle first
	  - Choose $I_q$ by shuffling training data and then cycling through it or by selecting q points randomly from training data
	  - **for each data** in mini-batch: 
	    compute gradients **for each weights**(backpropagation) ![[wk04- K-Nearest Neighbors & Neural Nets-20241006172930308.webp|200]]
	    - Iterate all batch if only 1 processor
		- or when there is k processors, *each processor iterates q/k data* -> k time faster
	- then update the parameters![[wk04- K-Nearest Neighbors & Neural Nets-20241006172950631.webp|200]]

>[!info] 
>- Computation time tends to increase when batch size q gets too small (can’t exploit parallelism as well, communication and synchronization costs between processors are amortised 摊销的 by using larger q/k)
>- Small batches provides a sort of regularization. Using large batches is often observed to lead over-fitting.
>- **Noisy Gradients in SGD**: In **Stochastic Gradient Descent (SGD)**, gradients are calculated *using small mini-batches of data, which makes the updates "noisy" or less stable compared to batch gradient descent (which uses the entire dataset)*. This noise can cause the updates to *oscillate and make it difficult to find the optimal solution quickly*.

Note: choosing batch size q = m the training data size then mini-batch SGD = gradient descent

>[!tip]
>- *Momentum* Momentum** helps to **smooth** out these oscillations by "averaging out" the gradient updates, allowing the optimization process to focus more on the **general direction** toward the minimum rather than being misled by the noise from individual updates.
>	- Momentum works by maintaining an *exponentially decaying* moving average of past gradients and using this "momentum" to influence the current update. Instead of updating the parameters θ based purely on the current gradient​ $g_t$, we also *include a fraction of the previous update*.
>  ![[wk04- K-Nearest Neighbors & Neural Nets-20241006173741114.webp]]
>  
>- *Adam*(Adaptive Moment Estimation)
>An approach for automatically choosing the step-size α plus using momentum. Currently the default in most packages, its ok to leave it that way for assignments in this module
>
>- *Early Stopping*:  try to achieve regularisation by stopping SGD early i.e. before cost function as converged to its minimum
>	- Repeat: 
>		- Keep a hold-out test set from training data e.g. 10% of data 
>		- Run SGD for a while, e.g. 1 epoch, on remaining training data 
>		- Evaluate cost function on (i) held-out test data and (ii) on training data used for SGD 
>		- Stop when cost function of test data stops decreasing and/or when these two values start to diverge
>	- Often used with SGD in combination with a penalty or dropouts for regularisation


>[!warning] Forward Propagation
>calculate output $\hat{y}$ of neural nets -> using **forward propagation to get all the derivatives of loss function over all weights**
>![[wk04- K-Nearest Neighbors & Neural Nets-20241006175411750.webp|600]]
>- In **forward propagation**, you compute the predicted output $\hat{y}$​ by passing the input data through the network.
>- Once you have the predicted output, compute the **loss function** based on the difference between the true output y and the predicted output $\hat{y}$​.

*the sorts of neural nets we’re considering are sometimes called feedforward networks*

>[!warning] backpropagation
>To calculate derivatives of loss function over all weight $\frac {\partial l_i} {\partial \theta_j}$ which is called gradient in multi-parameter equations
>- **Backpropagation** is the algorithm used to efficiently compute the **gradient** (the vector of partial derivatives) of the loss function with respect to each parameter.
>- During backpropagation, compute how much each weight θj​ contributed to the error by calculating the **partial derivative** $\frac{\partial l_i}{\partial \theta_j}​​$for each weight $\theta_j$​ in the network.

## SoftMax Layer: Logistic Regression as a Neural Network

A neural network layer can be described as $\hat{y} = f(\theta^T x)$, where the activation function $f$ is typically **sign function** and the output is mapped to the probability

### Extension to Multi-class (K classes)classification(Soft Layer)
**Training a separate linear model for each class k.**
- For each class k, compute: $z_k = \theta_k^T x$, where, $\theta_k$​ represents the weight vector for class k.
- The **SoftMax function** normalizes the outputs so that the probabilities across all classes sum to 1: 
$$\hat{y}_k = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$
- The class with the highest probability $\hat{y}_k$ is predicted.
![[wk04- K-Nearest Neighbors & Neural Nets-20241006182713264.webp|250]]
- This is identical to a multi-class logistic regression

## Summary

- Hard to interpret what the weights mean → its a black box model
- Can be tricky/slow to train → cost function is non-convex in weights/parameters, plus often many weights/parameters that need to be learned
### Usages
Mainly used for feature engineering and especially the use of **convolutional layers** and **transformer blocks**


