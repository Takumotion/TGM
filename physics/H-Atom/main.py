from scipy.constants import physical_constants
import matplotlib.pyplot as plt
import scipy.special as sp
import seaborn as sns
import numpy as np

## 1. Describe a Normalized Radial Function Rₙₗ(r)
def radial_function(n, l, r, a0):
    """ Compute the normalized radial part of the wavefunction using
    Laguerre polynomials and an exponential decay factor.
    Args:
        n (int): principal quantum number
        l (int): azimuthal quantum number
        r (numpy.ndarray): radial coordinate
        a0 (float): scaled Bohr radius
    Returns:
        numpy.ndarray: wavefunction radial component
    """

    laguerre = sp.genlaguerre(n - l - 1, 2 * l + 1)
    p = 2 * r / (n * a0)

    constant_factor = np.sqrt(
        ((2 / n * a0) ** 3 * (sp.factorial(n - l - 1))) /
        (2 * n * (sp.factorial(n + l)))
    )
    return constant_factor * np.exp(-p / 2) * (p ** l) * laguerre(p)

"""The radial part of the wavefunction is constructed by the product of:

a) Constant factor: constant_factor
Normalizes the radial wavefunction.
b) Exponential decay factor: np.exp(-p / 2)
Reflects the decrease in probability of finding an electron as it moves away from the nucleus.
c) Power-law dependence on radial distance: p ** l
Introduces a dependency based on the azimuthal quantum number l, indicating different radial behaviors for different orbitals.
d) Laguerre polynomial: laguerre(p)
Captures oscillations in the electron density as a function of radial distance.
Laguerre polynomials describe how the electron density changes as the distance from the nucleus increases:
laguerre = sp.genlaguerre(n — l — 1, 2 * l + 1)

Normalized radial distance from the nucleus:
p = 2 * r / (n * a0)"""

## 2. Describe a Normalized Angular Function Yₗₘ(θ,φ)
def angular_function(m, l, theta, phi):
    """ Compute the normalized angular part of the wavefunction using
    Legendre polynomials and a phase-shifting exponential factor.
    Args:
        m (int): magnetic quantum number
        l (int): azimuthal quantum number
        theta (numpy.ndarray): polar angle
        phi (int): azimuthal angle
    Returns:
        numpy.ndarray: wavefunction angular component
    """

    legendre = sp.lpmv(m, l, np.cos(theta))

    constant_factor = ((-1) ** m) * np.sqrt(
        ((2 * l + 1) * sp.factorial(l - np.abs(m))) /
        (4 * np.pi * sp.factorial(l + np.abs(m)))
    )
    return constant_factor * legendre * np.real(np.exp(1.j * m * phi))
"""The angular part of the wavefunction is constructed by the product of:

a) Constant factor: constant_factor
Normalizes the angular wavefunction.
b) Legendre polynomial:
Describes the angular dependence of the wavefunction based on the quantum numbers. Providing insight into the orientation and shape of electron orbitals around the nucleus for given quantum numbers.
c) Exponential factor: np.real(np.exp(1.j * m * phi))
Introduces a phase shift dependent on the magnetic quantum number m and the azimuthal angle φ.
Legendre polynomials describe the spatial arrangement and directional characteristics of electron probability densities:
legendre = sp.lpmv(m, l, np.cos(theta))
"""

## 3. Compute the Normalized wavefunction ψₙₗₘ(r,θ,φ) as a product of

def compute_wavefunction(n, l, m, a0_scale_factor):
    """ Compute the normalized wavefunction as a product
    of its radial and angular components.
    Args:
        n (int): principal quantum number
        l (int): azimuthal quantum number
        m (int): magnetic quantum number
        a0_scale_factor (float): Bohr radius scale factor
    Returns:
        numpy.ndarray: wavefunction
    """

    # Scale Bohr radius for effective visualization
    a0 = a0_scale_factor * physical_constants['Bohr radius'][0] * 1e+12

    # x-y grid to represent electron spatial distribution
    grid_extent = 480
    grid_resolution = 680
    z = x = np.linspace(-grid_extent, grid_extent, grid_resolution)
    z, x = np.meshgrid(z, x)

    # Use epsilon to avoid division by zero during angle calculations
    eps = np.finfo(float).eps

    # Ψnlm(r,θ,φ) = Rnl(r).Ylm(θ,φ)
    psi = radial_function(
        n, l, np.sqrt((x ** 2 + z ** 2)), a0
    ) * angular_function(
        m, l, np.arctan(x / (z + eps)), 0
    )
    return psi

"""The Bohr radius sets the scale of the wavefunction and determines the size of the atom. By scaling it, we adapt the wavefunction’s spatial extent for effective visualization:
a0 = a0_scale_factor * physical_constants[‘Bohr radius’][0] * 1e+12

Next, we establish a grid in the x-y plane, allowing the wavefunction to assign a probability value to each point. This grid aids in visualizing the electron’s spatial distribution:
x, y = np.meshgrid(x, y)

Then we compute the wavefunction by multiplying the radial and angular parts. The radial part considers the distance from the nucleus, whereas the angular part looks into the spatial orientation. Together, they define the electron’s behavior in the atom’s vicinity:
psi = radial_function(...) * angular_function(...)

Finally, we return the computed wavefunction, which encapsulates the quantum state of an electron in a hydrogen atom. The wavefunction contains complex amplitudes that provide information about the quantum state’s magnitude and phase:
return psi"""

## 4. Compute the Probability density |ψ|²
def compute_probability_density(psi):
    """ Compute the probability density of a given wavefunction.
    Args:
        psi (numpy.ndarray): wavefunction
    Returns:
        numpy.ndarray: wavefunction probability density
    """
    return np.abs(psi) ** 2

"""Here we return the square magnitude of the wavefunction, encapsulating the probability of the electron’s presence in different regions of the atom:
return np.abs(psi) ** 2"""

## 5. Plot the Probability Density

def plot_wf_probability_density(n, l, m, a0_scale_factor, dark_theme=False, colormap='rocket'):
    """ Plot the probability density of the hydrogen
    atom's wavefunction for a given quantum state (n,l,m).
    Args:
        n (int): principal quantum number, determines the energy level and size of the orbital
        l (int): azimuthal quantum number, defines the shape of the orbital
        m (int): magnetic quantum number, defines the orientation of the orbital
        a0_scale_factor (float): Bohr radius scale factor
        dark_theme (bool): If True, uses a dark background for the plot, defaults to False
        colormap (str): Seaborn plot colormap, defaults to 'rocket'
    """

    # Quantum numbers validation
    if not isinstance(n, int) or n < 1:
        raise ValueError('n should be an integer satisfying the condition: n >= 1')
    if not isinstance(l, int) or not (0 <= l < n):
        raise ValueError('l should be an integer satisfying the condition: 0 <= l < n')
    if not isinstance(m, int) or not (-l <= m <= l):
        raise ValueError('m should be an integer satisfying the condition: -l <= m <= l')

    # Colormap validation
    try:
        sns.color_palette(colormap)
    except ValueError:
        raise ValueError(f'{colormap} is not a recognized Seaborn colormap.')

    # Configure plot aesthetics using matplotlib rcParams settings
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['xtick.major.width'] = 4
    plt.rcParams['ytick.major.width'] = 4
    plt.rcParams['xtick.major.size'] = 15
    plt.rcParams['ytick.major.size'] = 15
    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30
    plt.rcParams['axes.linewidth'] = 4

    fig, ax = plt.subplots(figsize=(16, 16.5))
    plt.subplots_adjust(top=0.82)
    plt.subplots_adjust(right=0.905)
    plt.subplots_adjust(left=-0.1)

    # Compute and visualize the wavefunction probability density
    psi = compute_wavefunction(n, l, m, a0_scale_factor)
    prob_density = compute_probability_density(psi)
    
    # Here we transpose the array to align the calculated z-x plane with Matplotlib's y-x imshow display
    im = ax.imshow(np.sqrt(prob_density).T, cmap=sns.color_palette(colormap, as_cmap=True))

    cbar = plt.colorbar(im, fraction=0.046, pad=0.03)
    cbar.set_ticks([])

    # Apply dark theme parameters
    if dark_theme:
        theme = 'dt'
        background_color = sorted(
            sns.color_palette(colormap, n_colors=100),
            key=lambda color: 0.2126 * color[0] + 0.7152 * color[1] + 0.0722 * color[2]
        )[0]
        plt.rcParams['text.color'] = '#dfdfdf'
        title_color = '#dfdfdf'
        fig.patch.set_facecolor(background_color)
        cbar.outline.set_visible(False)
        ax.tick_params(axis='x', colors='#c4c4c4')
        ax.tick_params(axis='y', colors='#c4c4c4')
        for spine in ax.spines.values():
            spine.set_color('#c4c4c4')

    else:  # Apply light theme parameters
        theme = 'lt'
        plt.rcParams['text.color'] = '#000000'
        title_color = '#000000'
        ax.tick_params(axis='x', colors='#000000')
        ax.tick_params(axis='y', colors='#000000')

    ax.set_title('Hydrogen Atom - Wavefunction Electron Density', 
                 pad=130, fontsize=44, loc='left', color=title_color)
    ax.text(0, 722, (
        r'$|\psi_{n \ell m}(r, \theta, \varphi)|^{2} ='
        r' |R_{n\ell}(r) Y_{\ell}^{m}(\theta, \varphi)|^2$'
    ), fontsize=36)
    ax.text(30, 615, r'$({0}, {1}, {2})$'.format(n, l, m), color='#dfdfdf', fontsize=42)
    ax.text(770, 140, 'Electron probability distribution', rotation='vertical', fontsize=40)
    ax.text(705, 700, 'Higher\nprobability', fontsize=24)
    ax.text(705, -60, 'Lower\nprobability', fontsize=24)
    ax.text(775, 590, '+', fontsize=34)
    ax.text(769, 82, '−', fontsize=34, rotation='vertical')
    ax.invert_yaxis()

    # Save and display the plot
    plt.savefig(f'({n},{l},{m})[{theme}].png')
    plt.show()

    """In this code snippet, you’ll notice that a significant portion is dedicated to styling, thematics and data validation. The core functionality that computes and visualizes the electron probability distribution is encapsulated in just a few lines. Specifically, the key steps involve:

a) Computing the wavefunction
psi = compute_wavefunction(n, l, m, a0_scale_factor)
b) Computing the probability density
prob_density = compute_probability_density(psi)
c) Plotting the data
im = ax.imshow(np.sqrt(prob_density), cmap=sns.color_palette(...))"""

plot_wf_probability_density(4, 3, -1, 0.3, True)

"""The plot depicts the electron probability density for a hydrogen atom in the quantum state n=3, l=2, and m=1. This corresponds to a 3d orbital, displaying a clover-shaped distribution pattern with two lobes, indicating regions of higher electron probability, as shown by the bright spots.

The m=1 indicates the orbital is oriented in a particular manner in space, not symmetric about the nucleus like m=0 would be. This state is an excited state but lower in energy than a 4f state."""

## plot_wf_probability_density(4, 3, 0, 0.2, dark_theme=True, colormap='magma')
## plot_wf_probability_density(4, 3, 1, 0.2, dark_theme=True, colormap='mako')
## plot_wf_probability_density(9, 6, 1, 0.04, True, colormap='mako')