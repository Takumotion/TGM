import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Wellenparameter
A = 1
λ = 5
k = 2 * np.pi / λ
v = 2
omega = k * v

x = np.linspace(0, 20, 1000)

fig, axs = plt.subplots(4, 1, figsize=(10, 10))

# Einzelne Linien für jede Animation
line_right = axs[0].plot(x, np.zeros_like(x), color='red')[0]
line_left = axs[1].plot(x, np.zeros_like(x), color='green')[0]

# Zwei Wellen in einem Plot (rot und grün)
line_right3 = axs[2].plot(x, np.zeros_like(x), color='red', label='→')[0]
line_left3 = axs[2].plot(x, np.zeros_like(x), color='green', label='←')[0]

# Superposition der beiden (stehende Welle)
line_super = axs[3].plot(x, np.zeros_like(x), color='black')[0]

# Titel & Layout
titles = [
    "1. Laufende Welle nach rechts (→, red)",
    "2. Laufende Welle nach links (←, green)",
    "3. Beide Wellen separat (→ rot, ← green)",
    "4. Resultierende stehende Welle (black)"
]

for ax, title in zip(axs, titles):
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlim(0, 20)
    ax.set_title(title)
    ax.grid(True)

axs[2].legend(loc="upper right")

def animate(t):
    y_right = A * np.sin(k * x - omega * t)    # nach rechts
    y_left = A * np.sin(k * x + omega * t)     # nach links
    y_super = y_right + y_left                 # stehende Welle

    # Einzelplots
    line_right.set_ydata(y_right)
    line_left.set_ydata(y_left)

    # Zwei Wellen farbig im selben Plot (3)
    line_right3.set_ydata(y_right)
    line_left3.set_ydata(y_left)

    # Superposition (stehende Welle)
    line_super.set_ydata(2 * A * np.sin(k * x) * np.cos(omega * t))

    return line_right, line_left, line_right3, line_left3, line_super

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 4, 200), interval=50, blit=True)
plt.tight_layout()
plt.show()
