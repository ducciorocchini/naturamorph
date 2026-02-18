# ❄️ Koch Snowflake in Python

A simple implementation of the **Koch Snowflake fractal** using `numpy` and `matplotlib`.

---

## 📦 Requirements

```bash
pip install numpy matplotlib
```

---

## 🧠 Description

The Koch snowflake is a classic fractal constructed by recursively subdividing the sides of an equilateral triangle and inserting triangular "spikes".

The complexity increases exponentially with recursion depth.

---

## 🧩 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt


def koch_curve(p0, p1, depth):
    p0 = np.array(p0, dtype=float)
    p1 = np.array(p1, dtype=float)

    if depth == 0:
        return np.array([p0, p1])

    v = (p1 - p0) / 3.0
    a = p0 + v
    b = p0 + 2.0 * v

    angle = np.deg2rad(60)
    rot = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
    c = a + rot @ v

    p01 = koch_curve(p0, a, depth - 1)
    p12 = koch_curve(a, c, depth - 1)
    p23 = koch_curve(c, b, depth - 1)
    p34 = koch_curve(b, p1, depth - 1)

    return np.vstack([p01[:-1], p12[:-1], p23[:-1], p34])


def koch_snowflake(depth=4, scale=1.0, center=(0.0, 0.0)):
    cx, cy = center
    h = np.sqrt(3) / 2 * scale

    p0 = (cx - scale / 2, cy - h / 3)
    p1 = (cx + scale / 2, cy - h / 3)
    p2 = (cx,            cy + 2 * h / 3)

    s1 = koch_curve(p0, p1, depth)
    s2 = koch_curve(p1, p2, depth)
    s3 = koch_curve(p2, p0, depth)

    pts = np.vstack([s1[:-1], s2[:-1], s3[:-1], s1[:1]])
    return pts


def plot_snowflake(depth=4, scale=1.0):
    pts = koch_snowflake(depth=depth, scale=scale)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(pts[:, 0], pts[:, 1], lw=1.2, color="black")
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


# Run the snowflake
plot_snowflake(depth=4)
```

---

## ⚙️ Parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `depth`   | Recursion level (higher = more detailed) |
| `scale`   | Size of the snowflake                    |
| `center`  | Center coordinates                       |

---

## 🔬 Examples

Increase detail:

```python
plot_snowflake(depth=5)
```

Save to file:

```python
pts = koch_snowflake(depth=5)
plt.plot(pts[:, 0], pts[:, 1])
plt.savefig("snowflake.png", dpi=300)
```

---

## 📈 Growth of Complexity

Number of segments grows as:

[
3 \cdot 4^{depth}
]

Be careful with `depth > 6` — computation increases quickly.

---

