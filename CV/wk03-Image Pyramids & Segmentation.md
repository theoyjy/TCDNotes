## Image Pyramids
often called Multi scale/layer analysis

### Down sampling:
- the resolution of each layer is the 1/factor of the previous layer
- lose information
### Up sampling:
- to make the resolution upscale by factor n, have to predict many pixels
- predict by *interpolation*

#### Interpolation 
##### 1. round off the float coordinates to int
##### 2. **Nearest Neighbor Interpolation**
predicted pixel value = nearest neighbor from original  $f(10.2) = f(10)$
##### 3. Linear Interpolation
closer to a pixel, higher the weight is assigned
   ![[wk03-Image Pyramids-20240925100324311.webp|300]]
   $f(n + a) = (1 - a) * f(n) + a * f(n + 1) \quad 0 < a < 1$ 
   系数与乘的pixel的值是反的: 假设 a < 0.5, 则 a 离 f(n) 更近，所以f(n) 的weight 更大，所以 f(n) * (1- a)

##### 4. Bilinear Interpolation
*linear in both directions*
![[wk03-Image Pyramids-20240925101556305.webp|300]]
1. To calculate P, get R1 and R2 first
2. R1 = (x2 - x) / (x2 - x1) * Q11 + (x - x1) / (x2 - x1) * Q21
   Just normalize the distance
3. so is the R2
4. P = (y2 - y) /(y2 - y1) * R1 + (y - y1) / (y2 - y1) * R2

##### 5. Cubic Interpolation
向左取两个点，向右取两个点，在四个点之间插值
![[wk03-Image Pyramids-20240925103538442.webp|500]]

##### Bicubic
takes 16 pixels

## Segmentation

### K-Means Clustering
assume k number as the centroids, put the objects to the nearest centroids, calculate the average of each clusters to be new k centroids. Then repeat the whole process ... finally no changes any more, we achieve the final k means.

Semantic Segmentation
- not about the intensity
- but the high level information, each object should be distinguished.
- ![[wk03-Image Pyramids & Segmentation-20240925105426064.webp|300]]