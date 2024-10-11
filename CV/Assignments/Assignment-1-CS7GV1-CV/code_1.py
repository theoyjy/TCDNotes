# %% [markdown]
# # Assignment #01

# %% [markdown]
# # **Question 1: Image Convolution and Gaussian Filter**
# 
# ## Importing Necessary Libraries

# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from scipy.ndimage import gaussian_filter

# %% [markdown]
# ###1a. Grayscale Image Convolution with 2D Filter (2 Points)

# %%
def convolve2d(image, kernel):
    """
    Perform a 2D convolution of a grayscale image with a given kernel.
    Args:
    - image: 2D numpy array representing the grayscale image`
    - kernel: 2D numpy array representing the filter/kernel

    Returns:
    - convolved_image: 2D numpy array of the same size as the input image
    """

    # get the padding required for the convolution
    # if kernel is odd, pad by (k-1)/2
    # if kernel is even, pad by k/2
    # either way, the pad is the floor of the division
    kernel_height, kernel_width = kernel.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # convert the image and kernel to float to avoid truncation
    image = np.array(image, dtype=np.float32)
    kernel = np.array(kernel, dtype=np.float32)

    # Pad the image with 0
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

    # Initialize the convolved image and set the type to float,to avoid truncation
    convolved_image = np.zeros_like(image, dtype=np.float32)

    # Iterate over each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Extract the region that we are going to convolve
            region = padded_image[i:i + kernel_height, j:j + kernel_width]
            # Perform the convolution operation (element-wise multiplication and sum)
            convolved_image[i, j] = np.sum(region * kernel)

    # Normalize the image and convert back to uint8
    # convolved_image = cv2.normalize(convolved_image, None, 0, 255, cv2.NORM_MINMAX)
    # convolved_image = convolved_image.astype(np.uint8)

    return convolved_image


# Sobel vertical
kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])


# Read the image in grayscale
image = cv2.imread("template.png", cv2.IMREAD_GRAYSCALE)


# Apply the convolution
resulting_image = convolve2d(image, kernel)

plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display Grayscale Image Convolution with 2D Filter
plt.subplot(1, 3, 2)
plt.imshow(resulting_image, cmap='gray')
plt.title("Grayscale Image Convolution with 2D Filter ")
plt.axis("off")

plt.show()

# %% [markdown]
# ### 1b. RGB Image Convolution with 3D Filter (1 Point)

# %%
def convolve_rgb(image, kernel):
    """
    Perform a convolution on an RGB image using a 3D filter.
    Args:
    - image: 3D numpy array representing the RGB image
    - kernel: 3D numpy array (filter) with a depth of 3 (RGB)

    Returns:
    - convolved_image: 3D numpy array of the same size as the input image
    """
    # calculate the padding size
    kernel_height, kernel_width, kernel_depth = kernel.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # convert the image and kernel to float to avoid truncation
    image = np.array(image, dtype=np.float32)
    kernel = np.array(kernel, dtype=np.float32)

    # pad the image with 0
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), mode='constant')

    # Initialize the convolved image and set the type to uint8
    convolved_image = np.zeros_like(image, dtype=np.float32)
    # Iterate over each channel of each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                # Extract the region that we are going to convolve
                region = padded_image[i:i + kernel_height, j:j + kernel_width, k]
                # Perform the convolution operation on each channel
                convolved_image[i, j, k] = np.sum(region * kernel[:, :, k])

    # Normalize the image and convert back to uint8
    convolved_image = cv2.normalize(convolved_image, None, 0, 255, cv2.NORM_MINMAX)
    convolved_image = convolved_image.astype(np.uint8)

    return convolved_image


# Read the image in color
image = cv2.imread("template.png", cv2.IMREAD_COLOR)

kernel = np.array([
    [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
    [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
    [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
])

convolved_rgb_image = convolve_rgb(image, kernel)

plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display RGB Image Convolution with 3D Filter
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(convolved_rgb_image, cv2.COLOR_BGR2RGB))
plt.title("RGB Image Convolution with 3D Filter")
plt.axis("off")

plt.show()

# %% [markdown]
# ### Convolve the attached waldo.png with a (2D) Gaussian filter with σ = 1 and visualize the result (display the result of the convolution). You can use built-in functions for convolution. (1 Point)

# %%
# Code for (2D) Gaussian filter with σ = 1 will go here
# image sharpening

image = cv2.imread("waldo.png", cv2.IMREAD_COLOR)

resulting_image = gaussian_filter(image, sigma=1)

plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display RGB Image Convolution with 3D Filter
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(resulting_image, cv2.COLOR_BGR2RGB))
plt.title("Gaussian Image Convolution with 3D Filter")
plt.axis("off")

plt.show()

# %% [markdown]
# 
# ##-----------------------------------------------************************----------------------------------------------------
# 
# ## Question 2: Implement Canny Edge Detection from Scratch
# 
# 
# 
# 
# 
# 

# %% [markdown]
# ## 2a. Compute Gradient Magnitude for Images. Compute magnitude of gradients for the attached images waldo.png and template.png. (1 Point)

# %%
def gradient_magnitude(image):
    """
    Calculate the gradient magnitude of a 2D image using the Sobel operator.
    
    Args:
    - image: 2D numpy array representing the grayscale image

    Returns:
    - gradient_magnitude: 2D numpy array of the same size as the input image
    """
    # Compute gradients in the x and y directions
    grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)

    # Calculate the gradient magnitude
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

    # Normalize the result to the range [0, 255]
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    return gradient_magnitude.astype(np.uint8)

# Example usage
image = cv2.imread("template.png", cv2.IMREAD_GRAYSCALE)
grad_magnitude = gradient_magnitude(image)

# Display the result
cv2.imshow('Gradient Magnitude', grad_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
def compute_gradient_magnitude(image):
    """
    Compute the magnitude of gradients for an image.
    Args:
    - image: Grayscale image (2D numpy array)

    Returns:
    - gradient_magnitude: 2D numpy array representing gradient magnitudes
    """
    # Sobel horizontal filter
    kernel_horizontal = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    # Sobel vertical filter
    kernel_vertical = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    # Compute the horizontal and vertical gradients
    gradient_x = convolve2d(image, kernel_horizontal)
    gradient_y = convolve2d(image, kernel_vertical)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    return gradient_magnitude.astype(np.uint8)


template_image = cv2.imread("template.png", cv2.IMREAD_GRAYSCALE)
template_gradient_magnitude = compute_gradient_magnitude(template_image)

waldo_image = cv2.imread("waldo.png", cv2.IMREAD_GRAYSCALE)
waldo_gradient_magnitude = compute_gradient_magnitude(waldo_image)

plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(template_gradient_magnitude)
plt.title("Original Image")
plt.axis("off")

# Display RGB Image Convolution with 3D Filter
plt.subplot(1, 3, 2)
plt.imshow(waldo_gradient_magnitude)
plt.title("Gaussian Image Convolution with 3D Filter")
plt.axis("off")

plt.show()


# %% [markdown]
# ## 2b. MyCannyEdgeDetector Function (3 Point)

# %% [markdown]
# ### Key Stages of Canny Edge Detection (Explanation)
# 
# Explain the key stages of the Canny edge detection algorithm in detail. Your explanation should cover:
# 
# 1. **Noise Reduction**
# 2. **Gradient Calculation**
# 3. **Non-Maximum Suppression**
# 5. **Edge Tracking by Hysteresis**
# 
# Write your response in the markdown cell below.

# %% [markdown]
# ### Load the image

# %%
image_path = 'path_of_image'  # Replace with your image path

image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to grayscale

# %% [markdown]
# ####Noise Reduction (Gaussian Blur)

# %%
def apply_gaussian_blur(img, kernel_size=5):
    """Apply Gaussian blur to reduce noise."""
    return smoothed_image

# %% [markdown]
# ####Gradient Calculation (using Sobel filters)

# %%
def calculate_gradients(img):
    """Calculate gradients using Sobel filters."""
    # Code for Gradient Calculation will go here
    return gradient_magnitude, gradient_angle

# %% [markdown]
# ####Function for Non-Maximum Suppression

# %%
def non_maximum_suppression(gradient_magnitude, gradient_angle):
    """
    Perform non-maximum suppression on the gradient magnitude.
    Args:
    - gradient_magnitude: 2D array of gradient magnitudes
    - gradient_angle: 2D array of gradient directions (angles in degrees)

    Returns:
    - suppressed_magnitude: 2D array after non-maximum suppression
    """
    # Code for non-maximum suppression
    return suppressed_image


# %% [markdown]
# ####Function for Hysteresis Thresholding

# %%
def hysteresis_thresholding(suppressed_image, low_threshold, high_threshold):
    """
    Perform hysteresis thresholding on the non-max suppressed image.
    Args:
    - suppressed_image: 2D array after non-maximum suppression
    - low_threshold: Low threshold for hysteresis
    - high_threshold: High threshold for hysteresis

    Returns:
    - edge_image: Binary image after hysteresis thresholding
    """
    # Code for hysteresis thresholding
    return edge_image


# %% [markdown]
# ####Main Function for Canny Edge Detection

# %%
def MyCannyEdgeDetector(image, low_threshold, high_threshold):
    """
    Custom implementation of the Canny Edge Detector.
    Args:
    - image: Grayscale or RGB image (as numpy array)
    - threshold: Threshold value for edge detection

    Returns:
    - edge_image: Binary edge-detected image
    """

    # Apply Gaussian filter
    smoothed_image = apply_gaussian_filter(image, sigma=1)

    # Compute gradients
    gradient_magnitude, gradient_angle = compute_gradient_magnitude(smoothed_image)

    # Perform non-maximum suppression
    suppressed_image = non_maximum_suppression(gradient_magnitude, gradient_angle)

    # Apply hysteresis thresholding
    edge_image = hysteresis_thresholding(suppressed_image, low_threshold=low_threshold, high_threshold=high_threshold)

    return edge_image


# %% [markdown]
# ####Apply your custom Canny function and  built-in OpenCV Canny function
# 
# *Select the low and high thresholds according to your preference*
# 
# 

# %%
# Apply your custom Canny function
custom_edges = MyCannyEdgeDetector(gray_image, low_threshold=50, high_threshold=150)

# Apply the built-in OpenCV Canny function for comparison
opencv_edges = cv2.Canny(gray_image, 50, 150)

# %% [markdown]
# ####Compute the Structural Similarity Index Measure (SSIM) of the edges with your defined code and inbuilt commands here (2 Point).
# 

# %%

def calculate_ssim(custom_edges, opencv_edges):
    """
    Calculate the Structural Similarity Index (SSIM) between two edge-detected images.

    Args:
    - custom_edges: 2D numpy array of edges from custom Canny edge detection
    - opencv_edges: 2D numpy array of edges from OpenCV's Canny edge detection

    Returns:
    - similarity_index: SSIM between the custom and OpenCV edge-detected images
    """

    # Code for Structural Similarity Index Measure will go here

    return similarity_index


# Calculate SSIM
ssim_value = calculate_ssim(custom_edges, opencv_edges)

# Print SSIM result
print(f"SSIM between custom Canny and OpenCV Canny: {ssim_value:.4f}")


# %% [markdown]
# ###Visualize the results

# %%
plt.figure(figsize=(15, 5))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display custom Canny edge result
plt.subplot(1, 3, 2)
plt.imshow(custom_edges, cmap='gray')
plt.title("Custom Canny Edge Detection")
plt.axis("off")

# Display OpenCV's Canny edge result
plt.subplot(1, 3, 3)
plt.imshow(opencv_edges, cmap='gray')
plt.title("OpenCV Canny Edge Detection")
plt.axis("off")

plt.show()

# %% [markdown]
# ###Bonus Question: Limitations and Improvements
# 
# Discuss potential limitations of the Canny edge detection algorithm. Suggest how it could be improved for images with complex textures or lighting conditions.
# 
# 

# %% [markdown]
# Write your response here


