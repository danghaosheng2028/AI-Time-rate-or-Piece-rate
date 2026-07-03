"""
Figure 3: Minimum Wage Constraint Counterfactual
Shift in Contract Transformation Threshold from A* to A*_MW
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
W_min  = 0.5

A_space = np.linspace(0, 3, 600)

def H_tilde(A):
    return h + theta * A * C

def gamma_star(A):
    Ht = H_tilde(A)
    return Ht**2 / (Ht**2 + r * k * sigma2)

def Pi_T(A):
    return a0 * H_tilde(A) - U_bar - 0.5 * k * a0**2

def Pi_P(A):
    Ht = H_tilde(A)
    return Ht**4 / (2 * k * (Ht**2 + r * k * sigma2)) - U_bar - F

def Pi_P_MW(A, w_min=W_min):
    Ht    = H_tilde(A)
    gs    = gamma_star(A)
    alpha_raw = (U_bar
                 + 0.5 * r * gs**2 * sigma2
                 - (Ht**2 / (2 * k)) * gs**2)
    alpha  = np.maximum(alpha_raw, w_min)
    a_star = gs * Ht / k
    return (1 - gs) * a_star * Ht - alpha - F

def find_A_star(diff_arr):
    idx = np.argwhere(np.diff(np.sign(diff_arr))).flatten()
    return float(A_space[idx[0]]) if len(idx) > 0 else np.nan

diff_no = Pi_P(A_space)    - Pi_T(A_space)
diff_mw = Pi_P_MW(A_space) - Pi_T(A_space)

A_star_no = find_A_star(diff_no)
A_star_mw = find_A_star(diff_mw)

print("A* (no MW)  =", round(A_star_no, 4))
print("A* (with MW)=", round(A_star_mw, 4))

if not (np.isnan(A_star_no) or np.isnan(A_star_mw)):
    delay = A_star_mw - A_star_no
    print("Regulatory delay dA =", round(delay, 4))
else:
    print("WARNING: crossing not found -- lower W_min and retry")

fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

ax.plot(A_space, diff_no,
        color='steelblue', linewidth=2,
        label='Without minimum wage constraint')

ax.plot(A_space, diff_mw,
        color='darkorange', linewidth=2,
        label='With minimum wage $\\underline{W} = ' + str(W_min) + '$')

ax.axhline(0, color='gray', linestyle='--', alpha=0.6, linewidth=1)

if not np.isnan(A_star_no):
    ax.axvline(A_star_no, color='steelblue', linestyle=':', alpha=0.7)
    ax.text(A_star_no + 0.05, 0.4,
            '$A^* \\approx ' + str(round(A_star_no, 2)) + '$',
            color='steelblue', fontsize=11, fontweight='bold')

if not np.isnan(A_star_mw):
    ax.axvline(A_star_mw, color='darkorange', linestyle=':', alpha=0.7)
    ax.text(A_star_mw + 0.05, 0.4,
            '$A^*_{MW} \\approx ' + str(round(A_star_mw, 2)) + '$',
            color='darkorange', fontsize=11, fontweight='bold')

ax.set_title(
    'Minimum Wage Constraint: Regulatory Delay of Contract Transformation',
    fontsize=13)
ax.set_xlabel('AI Utilization Intensity $A$', fontsize=12)
ax.set_ylabel('Profit Difference $G(A) = \\Pi_P^* - \\Pi_T$', fontsize=12)
ax.legend(fontsize=11, loc='upper left')
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('figure3_minwage_counterfactual.png', dpi=300, bbox_inches='tight')
print("Saved: figure3_minwage_counterfactual.png")
plt.show()
