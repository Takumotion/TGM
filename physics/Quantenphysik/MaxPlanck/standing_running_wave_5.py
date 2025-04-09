import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Hohlraumgröße
L = 1.0
x = np.linspace(0, L, 1000)

# Moden
modes = [1, 2, 3, 4, 5]
frequencies = [1, 2, 3, 4, 5]  # jede Mode hat andere Frequenz
amplitude = 0.08
spacing = 0.15

# Farben für die einzelnen Wellen
colors = ['red', 'orange', 'yellow', 'cyan', 'magenta']

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")

# Rahmen (Kasten)
rect = plt.Rectangle((0, 0), 1, 1, linewidth=10, edgecolor='red', facecolor='black')
ax.add_patch(rect)

# Loch rechts
hole = plt.Rectangle((1, 0.45), 0.05, 0.1, color='black', zorder=10)
ax.add_patch(hole)

# Erzeuge Linien für jede stehende Welle mit eigener Farbe
wave_lines = []
for color in colors:
    line, = ax.plot([], [], color=color, linewidth=2, alpha=0.9)
    wave_lines.append(line)

# Achsenformatierung
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
ax.set_title("Animation: stehende Wellen im Schwarzen Körper", color='white', fontsize=14)

# Animationsfunktion
def animate(t):
    for i, n in enumerate(modes):
        omega = 2 * np.pi * frequencies[i]
        y_center = 0.85 - i * spacing
        y = amplitude * np.sin(n * np.pi * x / L) * np.cos(omega * t) + y_center
        wave_lines[i].set_data(x, y)
    return wave_lines

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 200), interval=50, blit=True)
plt.tight_layout()
plt.show()
