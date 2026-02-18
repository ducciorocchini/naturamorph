import numpy as np
import matplotlib.pyplot as plt


def koch_curve(p0, p1, depth):
    """Return points along a Koch curve from p0 to p1."""
    p0 = np.array(p0, dtype=float)
    p1 = np.array(p1, dtype=float)

    if depth == 0:
        return np.array([p0, p1])

    v = (p1 - p0) / 3.0
    a = p0 + v
    b = p0 + 2.0 * v

    # Rotate v by +60 degrees to get the "spike" point
    angle = np.deg2rad(60)
    rot = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
    c = a + rot @ v

    p01 = koch_curve(p0, a, depth - 1)
    p12 = koch_curve(a, c, depth - 1)
    p23 = koch_curve(c, b, depth - 1)
    p34 = koch_curve(b, p1, depth - 1)

    # Stitch segments (avoid duplicate endpoints)
    return np.vstack([p01[:-1], p12[:-1], p23[:-1], p34])


def koch_snowflake(depth=4, scale=1.0, center=(0.0, 0.0)):
    """Return Nx2 array of points for a Koch snowflake polygon."""
    cx, cy = center
    # Equilateral triangle
    h = np.sqrt(3) / 2 * scale
    p0 = (cx - scale / 2, cy - h / 3)
    p1 = (cx + scale / 2, cy - h / 3)
    p2 = (cx,            cy + 2 * h / 3)

    s1 = koch_curve(p0, p1, depth)
    s2 = koch_curve(p1, p2, depth)
    s3 = koch_curve(p2, p0, depth)

    # Combine, dropping duplicated endpoints
    pts = np.vstack([s1[:-1], s2[:-1], s3[:-1], s1[:1]])
    return pts


def plot_snowflake(depth=4, scale=1.0, line_width=1.2, color="black",
                   figsize=(6, 6), save=None, show=True):
    pts = koch_snowflake(depth=depth, scale=scale)

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(pts[:, 0], pts[:, 1], lw=line_width, color=color)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()

    if save:
        plt.savefig(save, dpi=300, bbox_inches="tight", pad_inches=0)

    if show:
        plt.show()
    else:
        plt.close(fig)

    return pts
