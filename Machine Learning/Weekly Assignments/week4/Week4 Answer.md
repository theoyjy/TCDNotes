# Question 1 - Data set 1 'week4_1.csv'
## a
The plot shows the data in `week4_1.csv`, there are two features `x_1` and `x_2`, and the target values only have two values: +1 and -1, where the green plus signs represent the +1 data while blue dot markers represent the -1 data.  Which indicates that the data requires a classification model. And there is a clear curve boundary between the two types of the target values, so the polynomial degree might be 2.
![[Pasted image 20241017233839.png]]
<center>Figure 1: Plot of Data Set week4_1.csv</center>

To find out the parameters of the most fit logistic regression model, the `accuracy` metrics is applied to evaluate the performance classification models. With continuously calculating the mean and standard deviation of accuracy scores through `cross_val_scores`, we are able to draw an `errorbar` to analyze the performance. 

Firstly, iterating the values of  polynomial degree from 1 to 15 on to generate the additional features to train the model, and evaluate the performance for each degree. The results are presented in the figure 2, where the x-axis is for the polynomial degree and the y-axis is for the accuracy. The accuracy reaches its maximum(0.963) at `degree = 2` and stays steady after that. In this case, the value 2 is the best polynomial degree for this data set, because there is no significant raise after 2 which means overfit would happen for any value greater than 2. That shows that the relationship between the features and target value is quadratic. 

![[Pasted image 20241018095824.png]]
<center>Figure 2: Plot of accuracy vs different polynomial degrees on logistic regression model</center>

Secondly, in order to decide the value of `C`, the same methodology is applied, which is iterating a range of `C` values while evaluating and showing their performance calculated from `cross_val_score`.  The following plot is an `errorbar` with x-axis having the values of `C` and y-axis with mean of the accuracy. The range of `C` being tested is from 1 to 1000, and from the plot below, we can find that that highest accuracy is around `c=100`, so let's dive deep around 100 to get a more accurate number.

![[Pasted image 20241018101144.png]]


<center>Figure 3: Errorbar of Logistic Regression Model</center>
With the following figure, it can be seen that the highest accuracy is found at  `C = 57.36`, and that is the best value of `C`.

![[Pasted image 20241018101557.png]]
<center>Figure 4: Errorbar of Logistic Regression Model</center>

To plot the model predictions, the following steps are taken: setting the polynomial degree to `2` to generate additional features, splitting the data into training and testing sets by `train_test_split`, instantiating a logistic regression model with `c = 57.36` and train the model on the training data, and finally predicting on the testing set, then we are able to get figure 5.  There are upwards red triangles representing +1 predictions and downwards orange triangles representing -1 predictions. The predictions are quite accurate, all the red upwards triangles(+1 prediction) locate inside the region of green plus signs(+1 data), and all the -1 predictions are in the region of -1 data.

![[Pasted image 20241017235206.png]]
<center>Figure 5: Plot of original data and predictions by logistic regression model</center>
## b
The kNN model has been evaluated by `cross_val_score` with different `K` values from 1 to 30. The following plot presents an accuracy error bars of the performance of the KNN model, where the x-axis is for values of `K`, and y-axis is for the values of accuracy. In this plot, it could be found that highest accuracy(0.9625) is at `K = 17`. The most suitable value for `K` is 17 for k-nearest neighbor mode of this data set, a precise prediction for a point is under the influence of its 17 nearest neighbors.
![[Pasted image 20241018000735.png]]
<center>Figure 5: Plot of error bar of KNN model</center>

With the `K` set to `17`, the predictions by KNN model are shown in the following plot, all the red upwards triangles(+1 prediction) locate inside the region of green plus signs(+1 data), and all the -1 predictions are in the region of -1 data.

![[Pasted image 20241018002138.png]]
<center>Figure 6: Plot of original data and predictions by logistic regression model</center>

## c
To deeply analyze the performance of each model, the confusion matrices are retrieved to form heatmaps to visualize the prediction accuracy. There are 4 heatmaps, in which two for dummy classifiers( one predicts most frequent and the other one predicts randomly), one plot for logistic, regression and one for KNN. And for each heatmap, the true positive is at the top-left, and true negative is at top-right, false positive is at bottom-left and false negative is at bottom-right. 

![[Pasted image 20241018011225.png|600]]
<center>Figure 7: Heatmaps of confusion matrices from different models</center>
