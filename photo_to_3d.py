from PIL import Image
from rembg import remove
import trimesh
import os

def generate_mesh_from_photo(image_path):
    print("Removing background...")
    with open(image_path, "rb") as f:
        image = Image.open(f).convert("RGBA")
    fg = remove(image)
  
    bg_rem = os.path.join("outputs", "bg_removed.png")
    fg.save(bg_rem)
    print(f"Background removed image saved to: {bg_rem}")


    print("Creating dummy cube for now...")
    mesh = trimesh.creation.box(extents=[1.0, 1.0, 1.0])
    return mesh
