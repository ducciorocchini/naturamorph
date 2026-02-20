import numpy as np
import matplotlib.pyplot as plt
import math


def coral_realistic_growth(
    n_steps=15000,
    grid_size=1001,
    seed=42,
    light_dir=(0.0, -1.0),
    flow_dir=(0.5, 0.0),
    light_weight=0.5,
    flow_weight=0.2,
    lateral_weight=0.4,
    noise_weight=0.3,
    branch_rate=0.1,
    death_rate=0.002,
    min_dist=2,
    crowding_max=4,     # <-- NUOVO: quanta “densità” tollerare nel vicinato
    temperature=2.0,
    max_tips=5000
):
    rng = np.random.default_rng(seed)
    grid = np.zeros((grid_size, grid_size), dtype=np.uint8)

    def normalize(v):
        vx, vy = v
        n = math.hypot(vx, vy)
        return (vx/n, vy/n) if n > 0 else (0.0, 0.0)

    Lx, Ly = normalize(light_dir)
    Fx, Fy = normalize(flow_dir)

    cx = grid_size // 2
    cy = int(grid_size * 0.85)
    grid[cy, cx] = 1

    tips = [(cx, cy)]
    history = [(cx, cy)]

    moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    def in_bounds(x, y):
        return min_dist < x < grid_size-min_dist and min_dist < y < grid_size-min_dist

    def too_crowded(nx, ny):
        """
        If the neighborhood within radius min_dist already contains
        too many occupied cells, we forbid growth there.
        """
        d = min_dist
        block = grid[ny-d:ny+d+1, nx-d:nx+d+1]
        occ = int(block.sum())
        return occ > crowding_max

    for _ in range(n_steps):
        if not tips:
            break

        i = rng.integers(0, len(tips))
        x, y = tips[i]

        candidates = []
        scores = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if not in_bounds(nx, ny):
                continue
            if grid[ny, nx] == 1:
                continue
            if too_crowded(nx, ny):
                continue

            n = math.hypot(dx, dy)
            ux, uy = dx/n, dy/n

            align_light = ux*Lx + uy*Ly
            align_flow  = ux*Fx + uy*Fy
            lateral     = 1 - abs(align_light)
            noise       = rng.random()

            score = (
                light_weight * align_light +
                flow_weight  * align_flow +
                lateral_weight * lateral +
                noise_weight * noise
            )

            candidates.append((nx, ny))
            scores.append(score)

        if not candidates:
            tips.pop(i)
            continue

        s = np.array(scores, dtype=float)
        s = (s - s.max()) * temperature
        p = np.exp(s)
        p /= p.sum()

        nx, ny = candidates[rng.choice(len(candidates), p=p)]

        grid[ny, nx] = 1
        history.append((nx, ny))

        if rng.random() < branch_rate and len(tips) < max_tips:
            tips.append((nx, ny))
        else:
            tips[i] = (nx, ny)

        if rng.random() < death_rate and len(tips) > 1:
            tips.pop(rng.integers(0, len(tips)))

    return np.array(history)

