"""
Gera a figura do Mapa de Lucro (curvas de nivel) usada no relatorio.

Reproduz a mesma funcao de lucro do sistema para o cenario da persona
(cafeteria) e marca o ponto otimo P*(9,00; 8,75).

Uso:
    pip install matplotlib numpy
    python gerar_grafico.py
Gera: mapa-lucro.png
"""

import matplotlib
matplotlib.use("Agg")  # backend sem janela (apenas salva o arquivo)
import matplotlib.pyplot as plt
import numpy as np

# Parametros do cenario da persona (cafeteria)
a1, b1, m1 = 120, 12, 3.0      # Cafe especial
a2, b2, m2 = 90, 10, 2.5       # Cappuccino
g, F = 4, 50

# Ponto otimo (calculado analiticamente pelo sistema)
p1_star, p2_star, lucro_star = 9.00, 8.75, 472.62


def lucro(p1, p2):
    q1 = a1 - b1 * p1 + g * p2
    q2 = a2 - b2 * p2 + g * p1
    return (p1 - m1) * q1 + (p2 - m2) * q2 - F


# Malha de precos em torno do otimo
p1 = np.linspace(3.0, 15.0, 400)
p2 = np.linspace(3.0, 14.5, 400)
P1, P2 = np.meshgrid(p1, p2)
Z = lucro(P1, P2)

fig, ax = plt.subplots(figsize=(8, 6))

# Preenchimento + linhas de nivel
cf = ax.contourf(P1, P2, Z, levels=30, cmap="YlOrBr")
cs = ax.contour(P1, P2, Z, levels=12, colors="#6f4e37", linewidths=0.6, alpha=0.6)
ax.clabel(cs, inline=True, fontsize=7, fmt="%.0f")

# Ponto otimo
ax.plot(p1_star, p2_star, marker="*", markersize=22,
        markerfacecolor="#d32f2f", markeredgecolor="white", markeredgewidth=1.5,
        linestyle="None", zorder=5)
ax.annotate(
    f"P*({p1_star:.2f}; {p2_star:.2f})\nLucro = R$ {lucro_star:.2f}/dia",
    xy=(p1_star, p2_star), xytext=(3.4, 12.8),
    fontsize=9, fontweight="bold", color="#7a1f1a",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.9,
              edgecolor="#7a1f1a"),
    arrowprops=dict(arrowstyle="->", color="#7a1f1a", linewidth=1.2),
)

cbar = fig.colorbar(cf, ax=ax)
cbar.set_label("Lucro (R$/dia)")

ax.set_xlabel("Preço — Café especial  (R$)")
ax.set_ylabel("Preço — Cappuccino  (R$)")
ax.set_title("Mapa de lucro — curvas de nível de π(p₁, p₂)")

fig.tight_layout()
fig.savefig("mapa-lucro.png", dpi=150)
print("Figura salva em mapa-lucro.png")
