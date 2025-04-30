import argparse
import os
from text_to_3d import generate_mesh_from_text
from photo_to_3d import mtf
from visualize import sm
import trimesh

ODIR = "outputs"
os.makedirs(ODIR, exist_ok=True)

def main():
    p = argparse.ArgumentParser()
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--image", type=str, help="Added the path to Image input")
    group.add_argument("--text", type=str, help="Input in Text Format")
    p.add_argument("--format", choices=["obj", "stl"], default="obj", help="Output format")
    p.add_argument("--no-visualize", action="store_true")
    args = p.parse_args()

    if args.image:
        print(f"Processing image: {args.image}")
        mesh = mtf(args.image)
    else:
        print(f"Generating from text: \"{args.text}\"")
        mesh = mtf(args.text)

    op = os.path.join(ODIR, f"model.{args.format}")
    mesh.export(op)
    print(f"Saved 3D model to: {op}")

    if not args.no_visualize:
        sm(mesh)

if __name__ == "__main__":
    main()
