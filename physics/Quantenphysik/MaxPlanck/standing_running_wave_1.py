import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Wellenparameter
A = 1                           # Amplitude
λ = 5                           # Wellenlänge
k = 2 * np.pi / λ              # Wellenzahl
v = 2                           # Geschwindigkeit
omega = k * v                  # Kreisfrequenz

x = np.linspace(0, 20, 1000)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
line1, = ax1.plot(x, np.zeros_like(x), label='Laufende Welle')
line2, = ax2.plot(x, np.zeros_like(x), label='Stehende Welle')

# Achsen-Einstellungen
for ax in [ax1, ax2]:
    ax.set_ylim(-2, 2)
    ax.set_xlim(0, 20)
    ax.grid(True)
    ax.legend()

def animate(t):
    y_moving = A * np.sin(k * x - omega * t)  # Laufende Welle nach rechts
    y_standing = 2 * A * np.sin(k * x) * np.cos(omega * t)  # Stehende Welle
    line1.set_ydata(y_moving)
    line2.set_ydata(y_standing)
    return line1, line2

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 4, 200), interval=50, blit=True)
plt.tight_layout()
plt.show()
