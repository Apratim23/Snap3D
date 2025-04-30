# utils/preprocess_image.py

import numpy as np
from PIL import Image

def itc(image):
    # Takes a PIL Image (RGBA) and creates point cloud points
    img_array = np.array(image)
    pts = []

    h, w, _ = img_array.shape
    for y in range(h):
        for x in range(w):
            r, g, b, a = img_array[y, x]
            if a > 0:  # if pixel is not transparent
                pts.append([x, h - y, 0])

    return np.array(pts)
