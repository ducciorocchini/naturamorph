import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # registra la proiezione 3D
from matplotlib.colors import Normalize

def _set_axes_equal(ax):
    """Make 3D axes have equal scale."""
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0]); x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0]); y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0]); z_middle = np.mean(z_limits)

    plot_radius = 0.5 * max([x_range, y_range, z_range])
    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def phyllotaxis_cone(
    n=4000,
    H=6.0,
    R=2.5,
    c=1.0,
    angle_deg=137.507764,
    jitter=0.0,
    seed=0,
    color_by="z",            # "z", "radius", or "index"
    cmap="viridis",
    point_size=8,
    elev=25, azim=-60,
    show=True,
    save_png=None,
    save_obj=None
):
    """
    Generate and plot 3D phyllotaxis points on a cone (Romanesco-like).
    Returns x,y,z arrays.
    """

    rng = np.random.default_rng(seed)

    i = np.arange(1, n + 1)
    alpha = np.deg2rad(angle_deg)
    theta = alpha * i

    t = i / float(n)
    z = t * H
    r = c * R * (1.0 - np.sqrt(t))

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    if jitter and jitter > 0:
        x = x + rng.normal(0, jitter, size=n)
        y = y + rng.normal(0, jitter, size=n)
        z = z + rng.normal(0, jitter * 0.4, size=n)

    if color_by == "radius":
        col = r
    elif color_by == "index":
        col = i
    else:
        col = z

    # plotting
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    norm = Normalize(vmin=np.min(col), vmax=np.max(col))
    sc = ax.scatter(x, y, z, c=col, cmap=cmap, norm=norm, s=point_size, depthshade=True, linewidths=0)

    ax.set_xlabel(""); ax.set_ylabel(""); ax.set_zlabel("")
    ax.view_init(elev=elev, azim=azim)
    ax.grid(False)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])

    _set_axes_equal(ax)

    # create a ScalarMappable with same cmap + norm, and pass ax explicitly to avoid ValueError
    mappable = plt.cm.ScalarMappable(cmap=sc.cmap, norm=sc.norm)
    mappable.set_array(col)
    cbar = fig.colorbar(mappable, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(color_by)

    plt.tight_layout()

    if save_png:
        plt.savefig(save_png, dpi=300, bbox_inches="tight", pad_inches=0)
        print(f"Saved image: {save_png}")

    if save_obj:
        with open(save_obj, "w") as f:
            for xi, yi, zi in zip(x, y, z):
                f.write(f"v {xi:.6f} {yi:.6f} {zi:.6f}\n")
        print(f"Saved OBJ (vertices only): {save_obj}")

    if show:
        plt.show()
    else:
        plt.close(fig)

    return x, y, z
