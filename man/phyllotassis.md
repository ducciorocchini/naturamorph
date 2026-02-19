# 🌻 Phyllotaxis Simulation in Python

A mathematical and visual implementation of **phyllotaxis**, the spiral arrangement observed in sunflowers, pinecones, Romanesco broccoli, and many plants.

This implementation uses the **golden angle** and square-root radial growth to produce near-uniform packing.

---

# 🧮 Mathematical Development

Phyllotaxis arises from placing points using polar coordinates with a fixed divergence angle.

---

## 1️⃣ Divergence Angle

Each new element is rotated by a constant angle:

[
\theta_i = i \cdot \alpha
]

where:

* ( i ) = index of the element
* ( \alpha ) = divergence angle

The optimal packing occurs when:

[
\alpha = 360^\circ \left(1 - \frac{1}{\varphi}\right)
]

where

[
\varphi = \frac{1 + \sqrt{5}}{2}
]

is the **golden ratio**.

Numerically:

[
\alpha \approx 137.507764^\circ
]

This angle is irrational relative to (2\pi), which prevents alignment and produces uniform distribution.

---

## 2️⃣ Radial Growth Law

To maintain approximately constant density:

[
r_i = c \sqrt{i}
]

Why √i?

The area of a disk grows as:

[
A = \pi r^2
]

So to place one point per constant area:

[
r \propto \sqrt{i}
]

The constant (c) controls global scale.

---

## 3️⃣ Cartesian Conversion

From polar to Cartesian:

[
x_i = r_i \cos(\theta_i)
]
[
y_i = r_i \sin(\theta_i)
]

---

## 4️⃣ Fibonacci Spirals (Parastichy)

When (\alpha) is close to the golden angle, visible spiral arms appear.

The number of clockwise and counterclockwise spirals typically correspond to consecutive **Fibonacci numbers**:

21–34
34–55
55–89

This is a natural consequence of irrational rotation on the circle.

---

# 🎨 Enhanced Implementation with Colormap Controls

```python
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
    """
    Generate and plot a phyllotaxis pattern.

    Parameters
    ----------
    n : int
        Number of points.
    c : float
        Radial scaling factor.
    angle_deg : float
        Divergence angle in degrees.
    jitter : float
        Add small random noise.
    seed : int
        Random seed.
    color_by : str
        "index" or "radius".
    cmap : str
        Matplotlib colormap name.
    point_size : float
        Size of scatter points.
    alpha : float
        Transparency.
    save : str or None
        Save output image.
    show : bool
        Display plot.
    """

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
```

---

# 🚀 Example Usage

### Classic sunflower

```python
phyllotaxis()
```

### Visible spiral arms

```python
phyllotaxis(angle_deg=136)
```

### Botanical tones

```python
phyllotaxis(cmap="Greens", color_by="radius")
```

### High contrast scientific

```python
phyllotaxis(cmap="inferno")
```

### Add natural irregularity

```python
phyllotaxis(jitter=0.2, alpha=0.8)
```

---

# 📦 Requirements

```bash
pip install numpy matplotlib
```

---
