"""
Figure 2: Contract Transformation Threshold Surface A*(r, sigma2)
3D Comparative Statics Visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
h      = 2.0
theta  = 1.5
C      = 1.0
k      = 1.0
a0     = 1.0
U_bar  = 1.0
F      = 1.5

A_space = np.linspace(0, 3, 600)

def H_tilde(A):
    return h + theta * A * C

def Pi_T(A):
    return a0 * H_tilde(A) - U_bar - 0.5 * k * a0**2

def Pi_P(A, r_val, sigma2_val):
    Ht = H_tilde(A)
    return Ht**4 / (2 * k * (Ht**2 + r_val * k * sigma2_val)) - U_bar - F

def solve_A_star(r_val, sigma2_val):
    diff = Pi_P(A_space, r_val, sigma2_val) - Pi_T(A_space)
    idx = np.argwhere(np.diff(np.sign(diff))).flatten()
    if len(idx) > 0:
        return A_space[idx[0]]
    return np.nan

r_vec     = np.linspace(0.1, 2.0, 40)
sigma_vec = np.linspace(0.1, 2.0, 40)
R_grid, S_grid = np.meshgrid(r_vec, sigma_vec)
A_surf = np.zeros_like(R_grid)

print("Computing 40x40 grid...")
for i in range(R_grid.shape[0]):
    for j in range(R_grid.shape[1]):
        A_surf[i, j] = solve_A_star(R_grid[i, j], S_grid[i, j])

print("NaN count:", np.sum(np.isnan(A_surf)), "/", R_grid.size)
print("A* range: [", round(float(np.nanmin(A_surf)), 4),
      ",", round(float(np.nanmax(A_surf)), 4), "]")

fig = plt.figure(figsize=(11, 7), dpi=300)
ax  = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(R_grid, S_grid, A_surf,
                       cmap='viridis',
                       edgecolor='none',
                       alpha=0.92)

ax.set_title('Contract Transformation Threshold $A^*(r, \\sigma^2)$',
             fontsize=13, pad=18)
ax.set_xlabel('Risk Aversion $r$',    fontsize=11, labelpad=10)
ax.set_ylabel('Output Noise $\\sigma^2$', fontsize=11, labelpad=10)
ax.set_zlabel('Threshold $A^*$',      fontsize=11, labelpad=10)
ax.view_init(elev=25, azim=-50)

cbar = fig.colorbar(surf, shrink=0.45, aspect=12, pad=0.12)
cbar.set_label('Threshold $A^*$', fontsize=10)

fig.tight_layout()
fig.savefig('figure2_threshold_surface.png', dpi=300, bbox_inches='tight')
print("Saved: figure2_threshold_surface.png")
plt.show()
