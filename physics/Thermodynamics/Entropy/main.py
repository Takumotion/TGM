import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Simulation parameters
num_particles = 6  # Total number of particles
chamber_size = 10  # Size of the chamber
door_open_time = 5  # Time in seconds before the door opens
simulation_time = 100  # Total simulation time in seconds
fps = 30  # Frames per second

# Temperature determines particle speed
temperature = 300  # Starting temperature (arbitrary units)
particle_speed = 10  # Adjusted speed for visibility

# Initialize particles with random positions and velocities
particles = {
    'x': np.concatenate([
        np.random.uniform(0, chamber_size / 2, num_particles // 2),  # Left chamber
        np.random.uniform(chamber_size / 2, chamber_size, num_particles // 2)  # Right chamber
    ]),
    'y': np.random.uniform(0, chamber_size, num_particles),
    'vx': np.random.uniform(-1, 1, num_particles) * particle_speed,
    'vy': np.random.uniform(-1, 1, num_particles) * particle_speed
}

# Create figure and axes
fig, (ax, ax_hist) = plt.subplots(2, 1, figsize=(6, 10))
ax.set_xlim(0, chamber_size)
ax.set_ylim(0, chamber_size)
ax.axvline(x=chamber_size / 2, color='black', linestyle='--', linewidth=1)

particle_plot, = ax.plot([], [], 'bo', label='Particles')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
entropy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
temperature_text = ax.text(0.02, 0.85, '', transform=ax.transAxes)

door_open = False
time_elapsed = 0

# Prepare histogram
distribution_counts = {}
for left in range(num_particles + 1):
    right = num_particles - left
    distribution = f"{left} left - {right} right"
    distribution_counts[distribution] = 0

distributions = list(distribution_counts.keys())
hist_data = np.zeros(len(distributions))

# Function to initialize the animation
def init():
    particle_plot.set_data([], [])
    time_text.set_text('')
    entropy_text.set_text('')
    temperature_text.set_text('')
    return particle_plot, time_text, entropy_text, temperature_text

# Function to update particle positions
def update_positions():
    for i in range(num_particles):
        # Update positions based on velocity
        particles['x'][i] += particles['vx'][i] / fps
        particles['y'][i] += particles['vy'][i] / fps

        # Handle collisions with walls
        if particles['x'][i] <= 0 or particles['x'][i] >= chamber_size:
            particles['vx'][i] *= -1
        if particles['y'][i] <= 0 or particles['y'][i] >= chamber_size:
            particles['vy'][i] *= -1

        # Handle collisions with closed door
        if not door_open:
            if particles['x'][i] > chamber_size / 2:
                particles['vx'][i] *= -1

# Function to compute entropy
def calculate_entropy():
    left_count = sum(1 for x in particles['x'] if x < chamber_size / 2)
    right_count = num_particles - left_count
    if left_count == 0 or right_count == 0:
        return 0
    p_left = left_count / num_particles
    p_right = right_count / num_particles
    return - (p_left * np.log2(p_left) + p_right * np.log2(p_right))

# Function to update histogram (starts only when door is open)
def update_histogram():
    if door_open:
        left_count = sum(1 for x in particles['x'] if x < chamber_size / 2)
        right_count = num_particles - left_count
        distribution = f"{left_count} left - {right_count} right"
        distribution_counts[distribution] += 1

        # Update histogram data
        for i, dist in enumerate(distributions):
            hist_data[i] = distribution_counts[dist]

        # Plot histogram
        ax_hist.clear()
        ax_hist.bar(distributions, hist_data, color='skyblue')
        ax_hist.set_title('Particle Distribution Histogram (After Door Opens)')
        ax_hist.set_xlabel('Distribution')
        ax_hist.set_ylabel('Count')
        ax_hist.set_xticklabels(distributions, rotation=45, ha='right')

# Animation update function
def update(frame):
    global door_open, time_elapsed
    time_elapsed += 1 / fps
    if time_elapsed >= door_open_time:
        door_open = True

    update_positions()
    update_histogram()

    # Update particle positions
    particle_plot.set_data(particles['x'], particles['y'])
    
    # Update time, entropy, and temperature text
    time_text.set_text(f'Time: {time_elapsed:.1f}s')
    entropy_text.set_text(f'Entropy: {calculate_entropy():.2f}')
    temperature_text.set_text(f'Temperature: {temperature}K')

    return particle_plot, time_text, entropy_text, temperature_text

# Run animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=int(simulation_time * fps), interval=1000 / fps, blit=False)
plt.tight_layout()
plt.legend()
plt.title('Entropy Simulation: Two Chambers with Particles')
plt.show()
