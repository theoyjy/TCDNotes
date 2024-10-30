# KNN
Only matching, not training
* Supervised learning: there are ground rules required

# NN
* **Perceptron**: take several binary inputs and produces a single binary output
* Compare the output with a **threshold**. 
	  $\sum{w_ix_i} >= threshold$ 
	  $\sum{w_ix_i} - threhold >= 0$
	  $\sum{w_ix_i} + b >= 0 \space where \space b(bias) = -threshold$
* Some data that not quite related should be removed, for example, the performance of students who don't attend classes should not be considered as a metrics of teaching quality
* Only suits for certain data sets
* **Multi Layer Perceptron**: hidden layer
* Non-linear
	* **sigmoid neurons**: control the range of the output within the boundary
	  $\sigma(z)=\frac{1}{1 + e^-z}\space where \space z = \sum{w_ix_i} + b$
	* **tanh function** 
* Activation function should be tried out to decide



# Deep Learning (CNN)

