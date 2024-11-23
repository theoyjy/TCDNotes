# CNN
The size of output shrinks
- Distinguish linear and non-linear filters
	- ReLU, Sigmoid, **pooling** are not linear
	- Linear means one input maps to one unique output
- Pooling 投票: Max, Average
- Dense: flatten the channels **maybe?** to one channel big image
- FC
- **Vanishing** point in ResNet slide mentioned
-  Dk is tensor dimension, M is number of channel, N is number of image, F is the image size

The difference between different types of the machine learning models:
- supervised learning
- unsupervised
- semi-supervised
- classification
- regression: numbers

### Auto-Encoders
Encoder **h = f(x)**+ Decoder Structure **r=g(h)**
**Non-linear process, unsupervised**

- **Definition:** An autoencoder is a neural network that is trained to attempt to copy its input to output

* Modern autoencoders also generalized to stochastic mappings $Pencoder(h|x), Pdecoder(x|h)$

- 
