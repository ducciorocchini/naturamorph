import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

def phyllotaxis(
    n=4000,
    c=4.0,
    angle_deg=137.507764,
    jitter=0.0,
    seed=0,
    color_by="index",        # "index" or "radius"
    cmap="viridis",          # any matplotlib colormap
    point_size=6,
    alpha=1.0,
    save=None,
    show=True
):
    rng = np.random.default_rng(seed)

    i = np.arange(1, n + 1)

    theta = np.deg2rad(angle_deg) * i
    r = c * np.sqrt(i)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    if jitter > 0:
        x += rng.normal(0, jitter, size=n)
        y += rng.normal(0, jitter, size=n)

    if color_by == "radius":
        col = r
    else:
        col = i

    norm = Normalize(vmin=np.min(col), vmax=np.max(col))

    fig, ax = plt.subplots(figsize=(7, 7))
    sc = ax.scatter(
        x,
        y,
        s=point_size,
        c=col,
        cmap=cmap,
        norm=norm,
        alpha=alpha,
        linewidths=0
    )

    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()

    if save:
        plt.savefig(save, dpi=300, bbox_inches="tight", pad_inches=0)
        print(f"Saved {save}")

    if show:
        plt.show()
    else:
        plt.close(fig)

    return x, y
