from PIL import Image
from rembg import remove
import trimesh
import os

def generate_mesh_from_photo(image_path):
    print("🧼 Removing background...")
    with open(image_path, "rb") as f:
        image = Image.open(f).convert("RGBA")
    fg = remove(image)
      # 🔽 Save the background-removed image
    bg_removed_path = os.path.join("outputs", "bg_removed.png")
    fg.save(bg_removed_path)
    print(f"✅ Background removed image saved to: {bg_removed_path}")

    # TODO: Replace with actual depth -> mesh logic
    print("🔧 Creating dummy cube for now...")
    mesh = trimesh.creation.box(extents=[1.0, 1.0, 1.0])
    return mesh
