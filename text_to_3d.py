import trimesh

def mft(prompt):
    print(f"Using dummy 3D model for: \"{prompt}\"")
    sphere = trimesh.creation.icosphere(radius=1.0)
    return sphere
