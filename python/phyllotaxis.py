import numpy as np
import matplotlib.pyplot as plt

def phyllotaxis(
    n=4000,
    c=4.0,                 # scale factor (bigger = more spread)
    angle_deg=137.507764,  # golden angle in degrees
    jitter=0.0,            # 0.. small noise
    seed=0,
    color_by="index",      # "index" or "radius"
    point_size=6,
    save=None,             # e.g. "phyllotaxis.png"
    show=True
):
    rng = np.random.default_rng(seed)

    # indices 1..n
    i = np.arange(1, n + 1)

    # golden-angle spiral
    theta = np.deg2rad(angle_deg) * i
    r = c * np.sqrt(i)

    # convert to Cartesian
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    if jitter > 0:
        x = x + rng.normal(0, jitter, size=n)
        y = y + rng.normal(0, jitter, size=n)

    # coloring
    if color_by == "radius":
        col = r
    else:
        col = i

    fig, ax = plt.subplots(figsize=(7, 7))
    sc = ax.scatter(x, y, s=point_size, c=col, marker="o", linewidths=0)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()

    if save is not None:
        plt.savefig(save, dpi=300, bbox_inches="tight", pad_inches=0)
        print(f"Saved {save}")

    if show:
        plt.show()
    else:
        plt.close(fig)

    return x, y
