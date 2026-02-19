# 🌊 Sea Ripples Simulation

A Python simulation of sea surface ripples using a discrete 2D wave equation and Matplotlib animation.

---

## 📦 Requirements

```bash
pip install numpy matplotlib pillow
```

---

## 🚀 Usage

```python
from sea_ripples import simulate_sea_ripples

simulate_sea_ripples(
    N=300,
    c=0.4,
    show=False,                # use False in non-interactive environments
    save_gif="sea_ripples.gif" # saves animation
)
```

---

## 🧠 Description

This simulation models ripples using a finite-difference approximation of the 2D wave equation:

[
u_{t+1} = 2u_t - u_{t-1} + c^2 \nabla^2 u_t
]

Where:

* `c` controls wave propagation speed
* `damping` controls energy dissipation
* Random droplets simulate rainfall

---

## 📜 Full Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def simulate_sea_ripples(
    N=220,
    c=0.35,
    damping=0.996,
    steps_per_frame=2,
    seed=0,
    rain_probability=0.16,
    show=True,
    save_gif=None,
):
    """
    Simulate sea surface ripples using a discrete 2D wave equation.

    Parameters
    ----------
    N : int
        Grid size (NxN).
    c : float
        Wave speed coefficient.
    damping : float
        Damping factor (<1 dissipates energy).
    steps_per_frame : int
        Simulation steps per animation frame.
    seed : int
        Random seed.
    rain_probability : float
        Probability of random droplet injection per step.
    show : bool
        If True, display animation window.
    save_gif : str or None
        If provided, save animation to this GIF file.

    Returns
    -------
    ani : matplotlib.animation.FuncAnimation
    """

    rng = np.random.default_rng(seed)

    u_prev = np.zeros((N, N), dtype=float)
    u = np.zeros((N, N), dtype=float)
    u_next = np.zeros((N, N), dtype=float)

    def laplacian(Z):
        return (
            np.roll(Z, 1, axis=0)
            + np.roll(Z, -1, axis=0)
            + np.roll(Z, 1, axis=1)
            + np.roll(Z, -1, axis=1)
            - 4 * Z
        )

    def inject_droplet(Z, x, y, amp=2.0, sigma=2.5):
        xs = np.arange(N)[:, None]
        ys = np.arange(N)[None, :]
        g = np.exp(-((xs - x) ** 2 + (ys - y) ** 2) / (2 * sigma**2))
        Z += amp * g

    def maybe_rain(Z):
        if rng.random() < rain_probability:
            x = rng.integers(10, N - 10)
            y = rng.integers(10, N - 10)
            inject_droplet(
                Z,
                x,
                y,
                amp=rng.uniform(1.0, 2.2),
                sigma=rng.uniform(1.5, 2.8),
            )

    inject_droplet(u, N // 2, N // 2)

    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(u, cmap="gray", vmin=-2.5, vmax=2.5, interpolation="bilinear")
    ax.axis("off")
    plt.tight_layout()

    state = {"u_prev": u_prev, "u": u, "u_next": u_next}

    def step():
        u_prev = state["u_prev"]
        u = state["u"]
        u_next = state["u_next"]

        u_next[:] = (2 * u - u_prev) + (c * c) * laplacian(u)
        u_next[:] *= damping

        u_next[0, :] = u_next[1, :]
        u_next[-1, :] = u_next[-2, :]
        u_next[:, 0] = u_next[:, 1]
        u_next[:, -1] = u_next[:, -2]

        state["u_prev"], state["u"], state["u_next"] = u, u_next, u_prev

    def update(_):
        for _ in range(steps_per_frame):
            maybe_rain(state["u"])
            step()
        im.set_data(state["u"])
        return (im,)

    ani = FuncAnimation(fig, update, interval=30, blit=True)

    if save_gif:
        ani.save(save_gif, writer="pillow", fps=30)
        print(f"Saved {save_gif}")

    if show:
        plt.show()

    return ani


if __name__ == "__main__":
    simulate_sea_ripples(show=True)
```

---

## ⚙️ Parameters Overview

| Parameter          | Description                  |
| ------------------ | ---------------------------- |
| `N`                | Grid resolution              |
| `c`                | Wave speed                   |
| `damping`          | Energy dissipation           |
| `rain_probability` | Frequency of random droplets |
| `save_gif`         | Output file name             |
| `show`             | Display live animation       |

---

## 💡 Notes

* In RStudio or non-interactive environments, use:

```python
simulate_sea_ripples(show=False, save_gif="sea_ripples.gif")
```

* Higher `N` → smoother but slower simulation
* Lower `damping` → longer-lasting waves
* Higher `rain_probability` → stormy sea

---
