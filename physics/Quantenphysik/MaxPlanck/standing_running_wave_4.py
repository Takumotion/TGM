import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# x-Werte über einen größeren Bereich für Bewegung
x = np.linspace(0, 4 * np.pi, 1000)
harmonics = [1, 2, 3, 4]
k0 = 1     # Basis-Wellenzahl
omega0 = 2 * np.pi  # Basis-Kreisfrequenz

x0 = 2 * np.pi  # Fester Beobachtungspunkt (in der Mitte des Plots)

# Plot setup
fig, axs = plt.subplots(4, 1, figsize=(10, 8))
wave_lines = []
dot_points = []

for i, n in enumerate(harmonics):
    wave_line, = axs[i].plot(x, np.zeros_like(x), label=f'{n}. Harmonische')
    red_dot, = axs[i].plot([], [], 'ro')
    wave_lines.append(wave_line)
    dot_points.append(red_dot)

    axs[i].set_ylim(-1.2, 1.2)
    axs[i].set_xlim(x[0], x[-1])
    axs[i].grid(True)

    wavelength = 2 * np.pi / (k0 * n)
    frequency = n

    axs[i].legend(loc='upper right')
    axs[i].set_title(
        f"{n}. Harmonische einer laufenden Welle\n"
        f"Wellenlänge: λ = {wavelength:.2f}, Frequenz: f = {frequency}"
    )

def animate(t):
    for i, n in enumerate(harmonics):
        k = k0 * n
        omega = omega0 * n
        y = np.sin(k * x - omega * t)
        wave_lines[i].set_ydata(y)

        y0 = np.sin(k * x0 - omega * t)
        dot_points[i].set_data(x0, y0)
    return wave_lines + dot_points

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 200), interval=50, blit=True)
plt.tight_layout()
plt.show()
