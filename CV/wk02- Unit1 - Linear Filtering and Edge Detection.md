# Point Processing:
  ==consider no neighborhood points but the point itself==

## Gray-level mapping
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001225148175.webp|500]]

## Non-linear Gray-Level Mapping 
###  Gamma Mapping
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001225232750.webp|150]]

### Logarithmic & exponential gray-level mappings
- Logarithmic mapping is useful for bringing out details in dark images
- Exponential mapping is useful for bringing out details in bright images
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001225432280.webp|250]]![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001225534147.webp|400]]

## Image Histogram
**Frequency vs Intensity**

![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001225747329.webp]]

### Histogram Stretching
**To make a low contrast image -> high contrast**
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001230347052.webp|300]]

![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001225914506.webp|500]]
### Histogram Equalization
**Stretching not work well when there is pixel at 0 and 255 where `f2-f1=255`**
Image Size: `MxN` 
Histogram:` H[i]; i=0,1,2,…..,255` 
Normalized Hist.: `H[i]/(MxN)`
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001230215166.webp|200]]

![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001230304595.webp]]

- [ ] keep reading point process


# Neighborhood Processing
## Convolution
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001230818183.webp]]
- *padding* for edge points.
- convolution only for LTI system
	- **kernel** with predefined weights
>[!tip] LTI system
>An **LTI (Linear Time-Invariant) system** is a system that satisfies two properties:
>1. **Linearity**: The system's response to a weighted sum of inputs is the weighted sum of the responses to each input.
>2. **Time-Invariance**: The system's behavior does not change over time, meaning that if you shift the input signal in time, the output will shift by the same amount.
>
>LTI systems are fundamental in signal processing because they are predictable, stable, and easy to analyze using mathematical tools like convolution.
## The Median Filter
>[!important] Non-linear filter, cannot implement with convolution.
> Be wise about when it's appliable

### Application: **Image Denoising**
For each pixels:
1. Apply the kernel, collect neighborhood values
2. **Sort the pixel values and find the median value**
3. Replace the original pixel

especially effective in removing "salt-and-pepper" noise while preserving edges better than averaging filters

### Mean Filter
The process is quite same as median filter
**But This is linear filter, can be processed by convolution**

## Correlation
>[!info] cross-correlation
>![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001232110580.webp|400]]
>- $g(x,y)$: The *output* image after applying the correlation.
>- $f(x+i,y+j)$: The pixel *values from the original image at position* $(x+i,y+j)$. This represents the neighborhood of pixels centered around position $(x,y)$.
>- $h(i,j)$: *The values from the filter/kernel of size* $(2R+1) \times (2R + 1)$. This kernel determines how much influence each neighboring pixel has in the output.
>- $\sum$: Summation over all pixels covered by the kernel.

### Correlation vs Convolution
>[!important]
>The difference lies in how the kernel $h(i,j)$ is applied:
>- Correlation: The kernel $h(i,j)$ is applied as is.
>- Convolution: The kernel $h(i,j)$ is flipped both horizontally and vertically(rotated by 180 degrees) before being applied to the image.

>[!info] Application done by correlation
>- Template matching
>- Image blue 
>	- mean filter
>	- gaussian filter(preserving better edges)
>- Detect edges - Sobel Kernel
>- Normalized cross-correlation
>![[wk02- Unit1 - Linear Filtering and Edge Detection-20241001234402288.webp|500]]
>- NCC between 0 - 1.

- Application by convolution - **Optical Convolution**
  since the ==lens system automatically performs convolution (which includes flipping)==, achieving optical correlation would require extra steps to "un-flip" the kernel before it interacts with the image, making it less straightforward.

### Separable Filter
- *convert filter to one vertical and one horizontal filter*
  Result same, but times of multiplication and additions are decreased
- One famous separable filter - Gaussian Filter
[Calculation example](https://www.songho.ca/dsp/convolution/convolution2d_separable.html)
Since the kernel size is 3x3, the regular 2D convolution requires 9 multiplications and 9 additions per sample. However, using separable convolution, each sample requires only 6 multiplications (3 for vertical and 3 for horizontal convolution) and 4 additions.
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241002000601606.webp]]
#### Edge Detection
##### Image Edges: **Gradients** - Prewitt and Sobel
* $g_x$ is for detecting horizontal gradients
* $g_y$ is for vertical gradients
* **Combine together, calculating the magnitude to be able to apply the threshold**

![[wk02- Unit1 - Linear Filtering and Edge Detection-20241002001000122.webp]]

>[!tip] Low-pass and high-pass FILTERs
>Low-pass filter: pass only low frequency information(smooth, gradual changes in intensity), while attenuating(reducing) high-frequency information (sharp edges, noise).
>**- If all positive or negative filter values -> low pass filter**
>**- if mixed -> high pass filter**
>
>Key Differences:
>- Low-pass filter: Smooths the image, blurs edges, and reduces noise. Examples include *Gaussian and averaging filters*.
>- High-pass filter: Enhances edges and fine details, making the image look sharper. Examples include *Sobel, Prewitt, and Laplacian filters*.

##### Contrast - image sharpening - Laplacian filter
![[wk02- Unit1 - Linear Filtering and Edge Detection-20241002001245664.webp]]

- Apply horizontal and vertical separately, then add them at the end (extra addition)
- First order / second **order** derivative. only consider it for *one direction*. 
	-  ==horizontal 1 -2 1==
		- ==first order: x2-x1  x3-x2== 
		- ==second order(combine first order):x3 - x2 - (x2 - x1)==
		- ==x3 - 2x2 + x1== 
		- that's why it is is 1 -2 1

##### Canny Edge Detector
  *Remove unwanted edges*
  1. **Smooth** image with Gaussian filter -> denoise
  2. Compute **derivative/gradient** of filtered image with Prewitt or Sobel
     
     The **gradient direction** at a pixel represents the direction of the steepest intensity increase, pointing towards the edge. Which is ==normal to the direction of the edge==
    
  3. Find **magnitude** and **orientation** of gradient
	 ![[wk02- Unit1 - Linear Filtering and Edge Detection-20240925092215521.webp|100]]
	 ==Direction of vertical edge is 0 degree==
	 ==Direction of horizontal edge is 90 degree==
  4. Apply “**Non-maximum Suppression**”
     - Compare the gradient magnitude at the current pixel to its neighbors along ==the normal to the edge(which is the direction of gradient)==
     - If the current pixel's gradient **magnitude is the largest compared to its neighbors, it is edge**
     - otherwise suppressed (set to 0).
  5. Apply “**Hysteresis Threshold**"
	 1. larger than high threshold -> strong edge
	 2. between low and high thresholds, then iterate the 8 pixels around the pixels, **it is considered edges only if connected to strong edges.**
	 3. below low threshold -> no edge










