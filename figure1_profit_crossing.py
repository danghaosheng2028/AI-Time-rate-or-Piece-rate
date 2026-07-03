"""
Figure 1: Corporate Profit Comparison
Time-rate vs Piece-rate Contract under AI-Augmented Production
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
h      = 2.0
theta  = 1.5
C      = 1.0
k      = 1.0
a0     = 1.0
U_bar  = 1.0
r      = 1.0
sigma2 = 1.0
F      = 1.5

A_space = np.linspace(0, 3, 600)

def H_tilde(A):
    return h + theta * A * C

def Pi_T(A):
    return a0 * H_tilde(A) - U_bar - 0.5 * k * a0**2

def Pi_P(A):
    Ht = H_tilde(A)
    return Ht**4 / (2 * k * (Ht**2 + r * k * sigma2)) - U_bar - F

def find_crossing(diff_arr):
    idx = np.argwhere(np.diff(np.sign(diff_arr))).flatten()
    return idx[0] if len(idx) > 0 else None

pit  = Pi_T(A_space)
pip  = Pi_P(A_space)
diff = pip - pit

cross_idx = find_crossing(diff)
A_star = A_space[cross_idx] if cross_idx is not None else None

slope = np.gradient(pit, A_space)
print("Slope min:", round(slope.min(), 6), "max:", round(slope.max(), 6))
print("Theory slope a0*theta*C =", a0 * theta * C)
if A_star is not None:
    print("A* =", round(A_star, 4))
else:
    print("WARNING: no crossing found")

fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

ax.plot(A_space, pit,
        color='gray', linestyle='--', linewidth=2,
        label='Time-rate Contract $\\Pi_T(A)$')

ax.plot(A_space, pip,
        color='steelblue', linewidth=2.5,
        label='Piece-rate Contract $\\Pi_P^*(A)$')

if A_star is not None:
    y_cross = float(np.interp(A_star, A_space, pit))
    ax.axvline(A_star, color='red', linestyle=':', alpha=0.7)
    ax.scatter(A_star, y_cross, color='red', zorder=5, s=70)
    ax.text(A_star - 0.38, y_cross + 0.4,
            '$A^* \\approx ' + str(round(A_star, 2)) + '$',
            color='red', fontsize=12, fontweight='bold')

ax.set_title('Corporate Profit: Time-rate vs. Piece-rate Contract',
             fontsize=13)
ax.set_xlabel('AI Utilization Intensity $A$', fontsize=12)
ax.set_ylabel('Expected Corporate Profit $\\Pi$', fontsize=12)
ax.legend(fontsize=11, loc='upper left')
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('figure1_profit_crossing.png', dpi=300, bbox_inches='tight')
print("Saved: figure1_profit_crossing.png")
plt.show()
