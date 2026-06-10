import matplotlib.pyplot as plt
import numpy as np

def dessiner_serpent_matplotlib():
    """Dessine un serpent stylisé en utilisant matplotlib"""

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_facecolor('white')

    # Coordonnées du corps en forme de S
    t = np.linspace(0, 4 * np.pi, 500)
    x = np.sin(t) * 3 + 2
    y = np.cos(t) * 2

    # Corps du serpent
    ax.plot(x, y, color='darkgreen', linewidth=15)
    ax.fill(x, y, color='green', alpha=0.7)

    # Texture de scales
    for i in range(20):
        scale_x = x[i*20] + np.sin(np.linspace(0, np.pi, 10)) * 0.3
        scale_y = y[i*20] + np.cos(np.linspace(0, np.pi, 10)) * 0.2
        ax.plot(scale_x, scale_y, color='darkgreen', linewidth=1, alpha=0.5)

    # Tête
    head_x, head_y = x[-1] + 0.5, y[-1]
    ax.fill([head_x, head_x + 1.2, head_x + 0.8],
            [head_y - 0.8, head_y, head_y + 0.8],
            color='darkgreen', alpha=0.9)

    # Yeux blancs + points noirs
    ax.plot(head_x + 0.8, head_y - 0.2, 'o', color='white', markersize=12)
    ax.plot(head_x + 0.8, head_y + 0.2, 'o', color='white', markersize=12)
    ax.plot(head_x + 0.9, head_y - 0.2, 'o', color='black', markersize=6)
    ax.plot(head_x + 0.9, head_y + 0.2, 'o', color='black', markersize=6)

    # Langue fourchue rouge
    ax.plot([head_x + 1.2, head_x + 1.8], [head_y, head_y - 0.4], color='red', linewidth=3)
    ax.plot([head_x + 1.8, head_x + 1.9], [head_y - 0.4, head_y - 0.3], color='red', linewidth=3)
    ax.plot([head_x + 1.2, head_x + 1.8], [head_y, head_y + 0.4], color='red', linewidth=3)
    ax.plot([head_x + 1.8, head_x + 1.9], [head_y + 0.4, head_y + 0.3], color='red', linewidth=3)

    ax.set_xlim(-3, 7)
    ax.set_ylim(-4, 4)
    ax.axis('off')
    ax.set_title('Serpent en Python', fontsize=16, fontweight='bold')

    plt.savefig('serpent.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.show()

dessiner_serpent_matplotlib()
