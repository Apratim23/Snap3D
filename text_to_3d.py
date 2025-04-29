import trimesh

def generate_mesh_from_text(prompt):
    print(f"🧠 Using dummy 3D model for: \"{prompt}\"")
    sphere = trimesh.creation.icosphere(radius=1.0)
    return sphere
