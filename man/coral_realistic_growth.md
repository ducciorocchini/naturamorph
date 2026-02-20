# 🪸 Coral Realistic Growth Model

## 🌊 Overview

`coral_realistic_growth()` simulates coral-like branching morphogenesis using a stochastic tip-based growth model.

The model captures key structural features of reef-building corals:

- 🌿 Tip-driven extension  
- 🌱 Branching (polyp budding)  
- ☀️ Phototropic bias (light-driven growth)  
- 🌬 Flow-influenced asymmetry  
- 🧱 Spatial competition (self-avoidance)  
- 🎲 Stochastic variability  

This is a **morphological analogue model**, not a full physiological simulator.

---

## 🧬 Biological Interpretation

Real coral colonies grow through:

- 🧫 Polyp budding at active tips  
- 🪨 Calcium carbonate skeletal deposition  
- ☀️ Light-enhanced growth (via symbiotic zooxanthellae)  
- 🌊 Flow-mediated nutrient transport  
- 🏁 Local competition for space  

The model abstracts these processes into:

| 🧬 Biological Process        | ⚙️ Model Component            |
|-----------------------------|------------------------------|
| Polyp budding               | `branch_rate`                |
| Phototropism                | `light_weight`               |
| Hydrodynamic forcing        | `flow_weight`                |
| Competition for space       | `min_dist`                   |
| Environmental variability   | `temperature`, `noise_weight` |
| Local mortality             | `death_rate`                 |

---

## 📐 Mathematical Structure

Growth proceeds from a set of **active tips**.

At each iteration:

1. 🎯 A tip \( i \) is selected.
2. 🔎 Candidate neighboring positions \( (x_j, y_j) \) are evaluated.
3. 📊 A score function is computed:

\[
S_j =
w_L (\mathbf{u}_j \cdot \mathbf{L}) +
w_F (\mathbf{u}_j \cdot \mathbf{F}) +
w_T (1 - |\mathbf{u}_j \cdot \mathbf{L}|) +
w_N \xi
\]

Where:

- \( \mathbf{u}_j \) = normalized direction of candidate move  
- \( \mathbf{L} \) = normalized light direction  
- \( \mathbf{F} \) = normalized flow direction  
- \( \xi \sim U(0,1) \) random noise  
- \( w_L, w_F, w_T, w_N \) are model weights  

Candidate selection uses a softmax:

\[
P_j = \frac{e^{\tau S_j}}{\sum_k e^{\tau S_k}}
\]

Where:

- 🌡 \( \tau \) = `temperature`  
- Higher \( \tau \) → more exploratory growth  

After selecting a move:

- 🪨 The skeleton grows at that location.
- 🌿 With probability `branch_rate`, a new tip is created.
- ✂️ With probability `death_rate`, a tip becomes inactive.

Spatial competition enforces:

\[
\min_{p \in \text{skeleton}} \|x - p\| \ge d
\]

Where \( d \) is `min_dist`.

---

## 🎛 Model Parameters

| Parameter        | 🪸 Effect on Morphology |
|-----------------|--------------------------|
| `branch_rate`   | Higher → more ramified colonies |
| `light_weight`  | Higher → vertical growth |
| `flow_weight`   | Higher → directional asymmetry |
| `lateral_weight`| Higher → bushy morphology |
| `min_dist`      | Higher → open branching structure |
| `temperature`   | Higher → stochastic irregularity |
| `death_rate`    | Higher → fragmented colony |

---

## 🚀 Example Usage

```python
from coral_growth import coral_realistic_growth
import matplotlib.pyplot as plt

pts = coral_realistic_growth(
    n_steps=12000,
    grid_size=451,
    branch_rate=0.10,
    lateral_weight=0.45,
    temperature=2.3
)

x = pts[:,0]
y = pts[:,1]

plt.figure(figsize=(7,7))
plt.scatter(x, y, s=0.6)
plt.gca().invert_yaxis()
plt.axis("off")
plt.show()
