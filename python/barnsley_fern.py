import numpy as np
import matplotlib.pyplot as plt


def barnsley_fern(
    n=200_000,
    seed=0,
    point_size=0.2,
    color="black",
    show=True,
    save=None,
    figsize=(6, 10)
):
    """
    Generate and optionally plot a geometric Barnsley fern.

    Parameters
    ----------
    n : int
        Number of points.
    seed : int
        Random seed for reproducibility.
    point_size : float
        Size of points in the plot.
    color : str
        Point color.
    show : bool
        Whether to display the plot.
    save : str or None
        Filename to save the figure (e.g. 'fern.png'), or None.
    figsize : tuple
        Figure size.

    Returns
    -------
    xs, ys : numpy arrays
        Coordinates of the fern points.
    """

    rng = np.random.default_rng(seed)

    x, y = 0.0, 0.0
    xs = np.empty(n)
    ys = np.empty(n)

    for i in range(n):
        r = rng.random()

        if r < 0.01:
            # stem
            x, y = 0.0, 0.16 * y
        elif r < 0.86:
            # main leaflet
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            # left leaflet
            x, y = 0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            # right leaflet
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

        xs[i] = x
        ys[i] = y

    if show or save:
        fig, ax = plt.subplots(figsize=figsize)
        ax.scatter(xs, ys, s=point_size, c=color, marker=".", linewidths=0)
        ax.set_aspect("equal")
        ax.axis("off")
        plt.tight_layout()

        if save is not None:
            plt.savefig(save, dpi=300, bbox_inches="tight", pad_inches=0)

        if show:
            plt.show()
        else:
            plt.close(fig)

    return xs, ys
