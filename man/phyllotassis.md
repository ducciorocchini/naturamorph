# 🌻 Phyllotaxis Simulation in Python

A simple implementation of **phyllotaxis** (sunflower / spiral plant growth pattern) using NumPy and Matplotlib.

Phyllotaxis is generated using the **golden angle**:

[
\theta = i \cdot 137.507764^\circ
]

[
r = c \sqrt{i}
]

This produces the characteristic sunflower-like spiral pattern.

---

## 📦 Requirements

```bash
pip install numpy matplotlib
```

---

## 🚀 Usage Example

```python
from phyllotaxis import phyllotaxis

phyllotaxis(
    n=4500,
    c=3.8,
    point_size=6,
    color_by="index",
    save="phyllotaxis.png",
    show=False
)
```

---

## 📜 Full Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

def phyllotaxis(
    n=4000,
    c=4.0,                 # scale factor (bigger = more spread)
    angle_deg=137.507764,  # golden angle in degrees
    jitter=0.0,            # small noise
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


# Example run
phyllotaxis(
    n=4500,
    c=3.8,
    point_size=6,
    color_by="index",
    save="phyllotaxis.png",
    show=False
)
```

---

## ⚙️ Parameters

| Parameter    | Description                              |
| ------------ | ---------------------------------------- |
| `n`          | Number of points                         |
| `c`          | Scaling factor (controls spacing)        |
| `angle_deg`  | Divergence angle (137.5° = golden angle) |
| `jitter`     | Adds randomness                          |
| `color_by`   | `"index"` or `"radius"`                  |
| `point_size` | Size of points                           |
| `save`       | Filename to save image                   |
| `show`       | Display plot window                      |

---

## 🌱 Experiments

### Golden angle (classic sunflower)

```python
phyllotaxis(angle_deg=137.507764)
```

### Visible spiral arms

```python
phyllotaxis(angle_deg=136)
```

### Add natural irregularity

```python
phyllotaxis(jitter=0.2)
```

---
