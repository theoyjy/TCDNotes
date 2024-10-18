# Question 1 - Data set 1 'week4_1.csv'
## a
The plot shows the data in `week4_1.csv`, there are two features `x_1` and `x_2`, and the target values only have two values: +1 and -1, where the green plus signs represent the +1 data while blue dot markers represent the -1 data.  Which indicates that the data requires a classification model. And there is a clear curve boundary between the two types of the target values, so the polynomial degree might be 2.
![[Pasted image 20241017233839.png]]
<center>Figure 1: Plot of Data Set 1</center>

To find out the parameters of the most fit logistic regression model, the `accuracy` metrics is applied to evaluate the performance classification models. With continuously calculating the mean and standard deviation of accuracy scores through `cross_val_scores`, we are able to draw an `errorbar` to analyze the performance. A nested loop is applied on the model by iterating the values of polynomial degree and `C` of the penalty together, thus it is achievable to get the best fit parameters.

The following plot is an `errorbar` with x-axis having the values of C and y-axis with mean of the accuracy. Each line is for a different polynomial degree of training data. By iterating the polynomial degrees from 1 to 4 to train the model on different training datasets, while setting the values of `C` in range of 1 to 1000, we are able to find that, the accuracy becomes steadily high after polynomial degree is equal to 2, thus the best fitting polynomial degree is 2, otherwise it will be overfitting. That means the relationship between the features and target value is quadratic.

At the same time, it could be observed that highest accuracy is around `c=100`, so let's dive deep around 100 to get a more accurate number.
![[Pasted image 20241017233818.png]]
<center>Figure 2: Errorbar of Logistic Regression Model</center>

With the following figure, it can be seen that the highest accuracy is found at  `C=74.05`, and that is the best value of C.
![[Pasted image 20241017233845.png]]
<center>Figure 3: Errorbar of Logistic Regression Model</center>

To plot the model predictions, the following steps are taken: setting the polynomial degree to `2` to generate additional features, splitting the data into training and testing sets by `train_test_split`, instantiating a logistic regression model with `c = 74.05` and train the model on the training data, and finally predicting on the testing set, we get figure 4.  There are upwards red triangles represent +1 predictions and downwards orange triangles represent -1 predictions.

![[Pasted image 20241017235206.png]]
<center>Figure 4: Plot of original data and predictions by logistic regression model</center>
## b
The kNN model has been evaluated by `cross_val_score` with different `K` values from 1 to 30. The following plot presents an accuracy error bars of the performance of the KNN model, where the x-axis is for values of `K`, and y-axis is for the values of accuracy. In this plot, it could be found that highest accuracy(0.9625) is at `K = 17`. The most suitable value for `K` is 17 for k-nearest neighbor mode of this data set, a precise prediction for a point is under the influence of its 17 nearest neighbors.
![[Pasted image 20241018000735.png]]
<center>Figure 5: Plot of error bar of KNN model</center>

With the `K` set to `17`, the predictions by KNN model are shown in the following plot:

![[Pasted image 20241018002138.png]]
<center>Figure 6: Plot of original data and predictions by logistic regression model</center>

## c


![[Pasted image 20241018005458.png]]