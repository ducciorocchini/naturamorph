import numpy as np
import matplotlib.pyplot as plt
import math


def coral_realistic_growth(
    n_steps=12000,
    grid_size=401,
    seed=42
):
    rng = np.random.default_rng(seed)
    grid = np.zeros((grid_size, grid_size), dtype=np.uint8)

    cx = grid_size // 2
    cy = int(grid_size * 0.8)

    grid[cy, cx] = 1
    tips = [(cx, cy)]
    history = [(cx, cy)]

    moves = [(1,0),(-1,0),(0,1),(0,-1),
             (1,1),(1,-1),(-1,1),(-1,-1)]

    light_dir = (0, -1)

    for _ in range(n_steps):

        if not tips:
            break

        i = rng.integers(0, len(tips))
        x, y = tips[i]

        candidates = []

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 2 < nx < grid_size-2 and 2 < ny < grid_size-2:
                if grid[ny, nx] == 0:

                    # distanza minima semplice (evita muri)
                    block = grid[ny-1:ny+2, nx-1:nx+2]
                    if (block == 1).sum() > 2:
                        continue

                    norm = math.sqrt(dx*dx + dy*dy)
                    ux, uy = dx/norm, dy/norm
                    align = ux*light_dir[0] + uy*light_dir[1]

                    score = align + 0.8*rng.random()
                    candidates.append((score, nx, ny))

        if not candidates:
            tips.pop(i)
            continue

        candidates.sort(reverse=True)
        _, nx, ny = candidates[0]

        grid[ny, nx] = 1
        history.append((nx, ny))

        # branching più forte
        if rng.random() < 0.12:
            tips.append((nx, ny))
        else:
            tips[i] = (nx, ny)

    return np.array(history)
  
