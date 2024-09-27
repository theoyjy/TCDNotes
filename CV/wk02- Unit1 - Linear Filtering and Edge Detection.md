- Point Processing:
  consider no neighborhood points but the point itself

### Neighborhood Processing
- *padding* for edge points.
- convolution only for LTI system
	- **kernel** with predefined weights
- The Median Filter
	- Image Denoising
	  Which one is suitable should be picked in different situation
		- ordering the neighbor points, pick the median value
			- Can not be processed by convolution
		- Or, use mean value
			- Can be processed by convolution
- Correlation between 0 - 1.
- Optical Convolution
- Separable Filter - Gaussian Filter
	- *convert filter to one vertical and one horizontal filter*
	  Result same, but times of multiplication and additions are decreased
* Edge Detection
	* Image Edges: Gradients
	* Contrast - image sharpening
	* **Low-pass filter**: pass only low frequency information
		* If all positive or negative filter values -> **low** pass filter
		* if **mixed** -> **high** pass filter
	* Image Sharpening
		* Laplacian filter
		- Apply horizontal and vertical separately, then add them at the end (extra addition)
		- First order / second **order** derivative. only consider it for *one direction*. 
			-  horizontal 1 -2 1
			  - first order: x2-x1  x3-x2 
			  - second order(combine first order):x3 - x2 - (x2 - x1)
			  - = x3 - 2x2 + x1 
			- Suppose Vertical filter is 1 -2 1
	- Canny Edge Detector
	  *Remove unwanted edges*
	  1. Smooth image with Gaussian filter -> denoise
	  2. Compute derivative of filtered image 
	  3. Find magnitude and orientation of gradient
	     ![[wk02- Unit1 - Linear Filtering and Edge Detection-20240925092215521.webp|100]]
	     Direction of vertical edge is 0 degree
	     Direction of horizontal edge is 90 degree
	  4. Apply “Non-maximum Suppression”
	     if value is not greater than maximum, then the pixel is the on the edge, neighbors are selected from the normal to the edge 
	  5. Apply “Hysteresis Threshold
	     1. larger than high threshold -> edge
	     2. between low and high thresholds, then iterate the 8 pixels around the pixels, if one is greater than the high threshold, make it the edge, otherwise, non-edge 
	     3. below low threshold -> no edge










