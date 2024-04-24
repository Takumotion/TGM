import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def formula(v_1, v_2, angle_1, angle_2):
    # Convert angle to radians
    angle_1_rad = np.radians(angle_1)
    angle_2_rad = np.radians(angle_2)
    # Calculate the x and y components of the velocities
    vx_1 = v_1 * np.cos(angle_1_rad)
    vy_1 = v_1 * np.sin(angle_1_rad)
    vx_2 = v_2 * np.cos(angle_2_rad)
    vy_2 = v_2 * np.sin(angle_2_rad)
    
    # Update the equations with the velocity components
    x_1 = vx_1 * t
    y_1 = vy_1 * t - 0.5 * g * t**2 + h

    x_2 = vx_2 * t
    y_2 = vy_2 * t - 0.5 * g * t**2 + h

    return y_1, y_2, x_1, x_2

# General variable and constant values
t = np.linspace(0, 10, 1000)  # Adjusted for realistic time frame
g = 9.81  # acceleration due to gravity in m/s^2
v_1 = 20  # initial velocity in m/s
v_2 = 0   # initial velocity in m/s
h = 5    # initial height in meters
angle_1 = 30  # angle in degrees
angle_2 = 0  # angle in degrees

y_1, y_2, x_1, x_2 = formula(v_1, v_2, angle_1, angle_2)

fig, ax = plt.subplots()
scat_1 = ax.scatter(x_1[0], y_1[0], c="b", s=5, label=f'v0 = {v_1} m/s')
scat_2 = ax.scatter(x_2[0], y_2[0], c="g", s=5, label=f'v0 = {v_2} m/s')

# Automatically adjust axes limits
max_x = max(x_1.max(), x_2.max())
max_y = max(y_1.max(), y_2.max())
ax.set(xlim=[0, max_x * 0.5], ylim=[0, max_y * 1.1], xlabel='Path [m]', ylabel='Height [m]')
ax.legend()

def update(frame):
    # Update the scatter plots with new positions
    scat_1.set_offsets(np.stack([x_1[:frame], y_1[:frame]]).T)
    scat_2.set_offsets(np.stack([x_2[:frame], y_2[:frame]]).T)
    return (scat_1, scat_2)

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=10)
plt.show()
