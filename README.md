# naturamorph

**naturamorph** is a Python package for generating **geometrical and morphogenetic shapes inspired by natural systems**.

The goal of the project is to provide **simple, reproducible, and extensible tools** to model, simulate, and visualize natural forms using **geometry, stochastic processes, and generative algorithms**.

---

## Philosophy

Natural shapes such as ferns, shells, snowflakes, fire fronts, or ink-like patterns often emerge from **simple rules applied iteratively**.

`naturamorph` focuses on:

* **Geometry-driven models**
* **Procedural and generative approaches**
* **Seeded reproducibility**
* **Minimal dependencies**
* **Readable, research-friendly code**

Rather than aiming for photorealism, the package emphasizes **structural and morphological realism**.

---

## Scope

The package is designed to grow and will include generators and simulations such as:

* 🌿 **Plant-like structures**

  * Ferns (IFS, L-systems)
  * Branching and phyllotaxis
* 🐚 **Shells and spirals**

  * Logarithmic spirals
  * Nautilus-like growth models
* ❄️ **Crystalline and fractal forms**

  * Snowflakes
  * Diffusion-limited aggregation
* 🔥 **Spatial processes**

  * Fire spread
  * Cellular automata
  * Percolation-like models
* 🖋️ **Organic marks and symbols**

  * Ink rings
  * Calligraphic, noise-driven shapes

All generators are **fully parametric** and **seeded**, allowing controlled exploration of form and complexity.

---

## Design principles

* **Pure Python**
* **Explicit parameters**
* **Reproducible randomness**
* **Modular structure**
* **Minimal plotting assumptions** (matplotlib-based by default)

Each function is intended to:

* return data when possible
* optionally visualize results
* be easy to integrate into research workflows

---

## Current status

The repository is **under active development**.
At the moment, it contains only a small number of functions, but the goal is to expand it into a **catalogue of natural geometric morphologies**.

The API may change as the package evolves.

---

## Installation (development)

```bash
git clone https://github.com/ducciorocchini/naturamorph.git
cd naturamorph
pip install -e .
```

Dependencies are intentionally kept minimal (typically `numpy` and `matplotlib`).

---

## Intended audience

* Researchers exploring **natural patterns**
* Educators teaching **geometry and emergence**
* Artists and designers interested in **generative forms**
* Anyone curious about **how simple rules create complex shapes**

---

## License

This project is released under an open-source license (see `LICENSE`).

---

## Author

**Duccio Rocchini**
