import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def show_mesh(mesh):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.add_collection3d(Poly3DCollection(mesh.triangles, facecolors="lightblue", edgecolors="gray", linewidths=0.3, alpha=0.8))
    ax.auto_scale_xyz(*mesh.bounds.T)
    plt.show()
