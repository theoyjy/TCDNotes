## Image Pyramids
often called Multi scale/layer analysis
top is level 0, bottom is level j(base)

### Down sampling:
- the resolution of each layer is the 1/factor of the previous layer
- lose information
#### Re-scale & Correlation
- **Re-scale (Down sampling)**: This process involves creating smaller versions of the original image, typically by reducing the width and height by a factor (e.g., 2x, 4x) at each level, resulting in a pyramid of images at multiple resolutions.
- **Correlation** refers to comparing a smaller **template or filter(a smaller image or pattern you are searching for)** to *every possible position(slide the template)* within the downscaled image at each pyramid level. 
- **Lose information**
  >At each level of the pyramid, you slide a template over the entire image and compute a correlation score at every position *to identify where the template matches best*.
### Up sampling - interpolation:
- to make the resolution upscale by factor n, have to predict many pixels
- predict by **interpolation**

>[!important]
>Only up sampling then down sampling will result the same image as origin
>Down then up will lose info in the first place

### Interpolation 
#### Zeroth-order Interpolation - **Nearest Neighbor Interpolation**
**Uses a constant value** - the nearest known point
- round off the float coordinates to int
	predicted pixel value = nearest neighbor from original  $f(10.2) = f(10)$
- Simply replicate the value from neighboring
#### First-order interpolation
##### 1. Linear Interpolation
**Uses the values of the two closest points and assumes a straight-line relationship between them**
closer to a pixel, higher the weight is assigned
   ![[wk03-Image Pyramids-20240925100324311.webp|300]]
   $f(n + a) = (1 - a) * f(n) + a * f(n + 1) \quad 0 < a < 1$ 
   系数与乘的pixel的值是反的: 假设 a < 0.5, 则 a 离 f(n) 更近，所以f(n) 的weight 更大，所以 f(n) * (1- a)

##### 2. Bilinear Interpolation
**The assigned value is an intermediate value between the for nearest pixels**
*linear in both directions*
![[wk03-Image Pyramids-20240925101556305.webp|300]]
1. To calculate P, get R1 and R2 first
2. R1 = (x2 - x) / (x2 - x1) * Q11 + (x - x1) / (x2 - x1) * Q21
   Just normalize the distance
3. so is the R2
4. P = (y2 - y) /(y2 - y1) * R1 + (y - y1) / (y2 - y1) * R2

#### Cubic Interpolation
向左取两个点，向右取两个点，在四个点之间插值
![[wk03-Image Pyramids-20240925103538442.webp|500]]

##### Bicubic Interpolation
**The assign value is a weighted sum of the 4x4 nearest pixels**
![[wk03-Image Pyramids & Segmentation-20241001223903020.webp]]

## Image Segmentation

### K-Means Clustering
![[wk03-Image Pyramids & Segmentation-20241001224902834.webp|400]]
1. *Initialization*: Choose the number of clusters k. **Randomly initial k centroids**
2. *Assignment*: For each pixel in the image, calculate its distance to each of the k centroid, and **assign the pixel to the nearest centroids**, *forming k clusters*
3. *Update*: For each cluster, calculate the **mean color of all pixels assigned to that cluster**. This mean becomes the **new centroids** for the cluster.
4. *Repeat*: Repeat assignment and update steps until the centroids no longer change or the change below a threshold
5. *Convergence*: When the centroids stop changing or have minimal changes, the algorithm has converged, and you have the final clusters (segments).

The result is a segmented image where **each pixel is replaced by the mean color of its corresponding cluster**, leading to distinct regions that can highlight different objects, textures, or features within the image.

Semantic Segmentation
- not about the intensity
- but the high level information, each object should be distinguished.
- ![[wk03-Image Pyramids & Segmentation-20240925105426064.webp|300]]