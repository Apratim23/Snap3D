import argparse
import os
from text_to_3d import generate_mesh_from_text
from photo_to_3d import generate_mesh_from_photo
from visualize import show_mesh
import trimesh

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--image", type=str, help="Added the path to Image input")
    group.add_argument("--text", type=str, help="Input in Text Format")
    parser.add_argument("--format", choices=["obj", "stl"], default="obj", help="Output format")
    parser.add_argument("--no-visualize", action="store_true")
    args = parser.parse_args()

    if args.image:
        print(f"Processing image: {args.image}")
        mesh = generate_mesh_from_photo(args.image)
    else:
        print(f"Generating from text: \"{args.text}\"")
        mesh = generate_mesh_from_text(args.text)

    output_path = os.path.join(OUTPUT_DIR, f"model.{args.format}")
    mesh.export(output_path)
    print(f"Saved 3D model to: {output_path}")

    if not args.no_visualize:
        show_mesh(mesh)

if __name__ == "__main__":
    main()
