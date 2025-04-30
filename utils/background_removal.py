from rembg import remove
from PIL import Image

def remove_background(image_path, save_path=None):
    img = Image.open(image_path).convert("RGBA")
    output = remove(img)

    if save_path:
        output.save(save_path)
        
    return output
