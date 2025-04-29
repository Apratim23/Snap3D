# utils/preprocess_image.py

import numpy as np
from PIL import Image

def image_to_point_cloud(image):
    # Takes a PIL Image (RGBA) and creates point cloud points
    img_array = np.array(image)
    points = []

    height, width, _ = img_array.shape
    for y in range(height):
        for x in range(width):
            r, g, b, a = img_array[y, x]
            if a > 0:  # if pixel is not transparent
                points.append([x, height - y, 0])

    return np.array(points)
