- input is image
- output is anime
# Harris Corner Detection
Identify the edge, flat, corner
   Flat is low pass, no content changing (low pass content)
   Edge: Changes in few directions (high pass)
   Corner: change in all directions (high)
![[wk04-Feature Detection and Matching-20241002092510474.webp|600]]

 Calculate the change of intensity for the shift`[u, v]` of one patch.
![[wk04-Feature Detection and Matching-20241002093820945.webp]]
- window function is just giving weight of each pixel, for example, all 1 inside image; or Gaussian function, center has more weights
Tylor Series for 2D function
![[wk04-Feature Detection and Matching-20241002094031601.webp|400]]
- the $I(x+u, y+u)$ can be approx. the same way.
  ![[wk04-Feature Detection and Matching-20241002094706726.webp|400]]

Difference for one direction called $\lambda$, 
	if $\lambda_1$ and $\lambda_2$ are both small -> flat
	If one is large and one is small -> edge
	both larger -> corner

## Harris Detector Properties

### Invariance
**Invariance** in the context of the Harris Corner Detector refers to the algorithm's ability to detect corners consistently, regardless of certain transformations or changes in the image.
1. *Rotation* Invariance
	Corner response R is invariant to image rotation
2. Intensity *Shift* Invariance
	only derivatives are used, not original intensity values
3. Invariant to *intensity* scaling
#### Not Invariant to image scaling
it may struggle to detect the same corners if the image is scaled (zoomed in or out). Corners detected at one scale may not be detected at another scale.

# Scale Invariant Feature Transform (SIFT)
This method achieves all the invariance, better than Harris. Also achieve the feature matching
1. Apply Gaussian to images repeatedly, and Calculate Difference of Gaussian(DOG).
2. local maximum
   Compare the value of a pixel not only with its own neighbors, but also across all DOG
   For example, 3 DOG, 27 points in total, center is 1 point, so we have to compare 1 points to other 26 points.
- [x] Dive into the steps ✅ 2024-11-11

Key point  Localization
![[wk04-Feature Detection and Matching-20241009093104592.webp]]

3. Orientation Assignment: calculate the rotation and rotate back
   ![[wk04-Feature Detection and Matching-20241009092541707.webp|500]]

4. The local Image Descriptor
   ![[wk04-Feature Detection and Matching-20241009094013046.webp]]
   
   

# SURF (self-study)



