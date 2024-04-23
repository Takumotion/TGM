import numpy as np
import matplotlib.pyplot as plt

def double_slit_experiment(num_slits, num_points, wavelength, slit_width, distance):
    # Calculate the positions of the slits
    slit_positions = np.linspace(-slit_width * (num_slits - 1) / 2, slit_width * (num_slits - 1) / 2, num_slits)

    # Calculate the positions on the screen
    screen_positions = np.linspace(-distance / 2, distance / 2, num_points)

    # Initialize the screen intensity
    screen_intensity = np.zeros_like(screen_positions)

    # Calculate the interference pattern
    for i, screen_pos in enumerate(screen_positions):
        for slit_pos in slit_positions:
            # Calculate the path difference
            path_difference = np.sqrt(slit_pos**2 + screen_pos**2)

            # Calculate the phase difference
            phase_difference = (2 * np.pi * path_difference) / wavelength

            # Calculate the intensity at the screen position
            intensity = np.cos(phase_difference) ** 2

            # Add the intensity contribution from each slit
            screen_intensity[i] += intensity

    # Normalize the intensity
    screen_intensity /= num_slits

    # Plot the interference pattern
    plt.plot(screen_positions, screen_intensity)
    plt.xlabel('Screen Position')
    plt.ylabel('Intensity')
    plt.title('Double Slit Interference Pattern')
    plt.show()

# Parameters
num_slits = 2
num_points = 1000
wavelength = 1e-3
slit_width = 1e-4
distance = 1

# Run the experiment
double_slit_experiment(num_slits, num_points, wavelength, slit_width, distance)