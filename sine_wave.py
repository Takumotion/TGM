import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Moving Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")

# Initialize the line object and red dots
x = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(x, np.zeros_like(x), lw=2)  # Start with a flat line
dot_positions = np.linspace(0, 2 * np.pi, 20)  # Fixed x positions for red dots
dots, = ax.plot(dot_positions, np.zeros_like(dot_positions), 'ro')  # Red dots

# Animation update function
def update(frame):
    wave_length = np.pi  # Length of one sine wave
    wave_start = (frame / 50.0) % (2 * np.pi)  # Position of the start of the wave

    # Create a sine wave that starts at wave_start and ends at wave_start + wave_length
    y = np.zeros_like(x)
    mask = (x >= wave_start) & (x <= wave_start + wave_length)
    y[mask] = np.sin(2 * np.pi * (x[mask] - wave_start) / wave_length)
    
    # Update the line
    line.set_ydata(y)

    # Update red dots (vertical position only)
    dot_y = np.sin(2 * np.pi * (dot_positions - wave_start) / wave_length)
    dot_y[(dot_positions < wave_start) | (dot_positions > wave_start + wave_length)] = 0
    dots.set_data(dot_positions, dot_y)

    return line, dots

# Create the animation
ani = FuncAnimation(fig, update, frames=400, interval=50, blit=True)

# Display the animation
plt.show()
