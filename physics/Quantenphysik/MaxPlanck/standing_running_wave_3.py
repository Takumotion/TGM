import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# x from 0 to π (half period)
x = np.linspace(0, np.pi, 500)
harmonics = [1, 2, 3, 4]
omega_base = 2 * np.pi  # base angular frequency

# Plot setup
fig, axs = plt.subplots(4, 1, figsize=(10, 8))
lines = []

for i, n in enumerate(harmonics):
    line, = axs[i].plot(x, np.zeros_like(x), label=f'{n}. Harmonische')
    lines.append(line)
    axs[i].set_ylim(-1.2, 1.2)
    axs[i].set_xlim(0, np.pi)
    axs[i].grid(True)

    # Calculate wavelength and frequency
    lambda_n = 2 * np.pi / n  # assuming λ₁ = 2π
    f_n = n  # f₁ = 1, f₂ = 2, etc.

    axs[i].legend(loc='upper right')
    axs[i].set_title(
        f"{n}. Harmonische einer stehenden Welle\n"
        f"Wellenlänge: λ = {lambda_n:.2f}, Frequenz: f = {f_n}"
    )

def animate(t):
    for i, n in enumerate(harmonics):
        y = np.sin(n * x) * np.cos(n * omega_base * t)  # frequency scales with n
        lines[i].set_ydata(y)
    return lines

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 200), interval=50, blit=True)
plt.tight_layout()
plt.show()
