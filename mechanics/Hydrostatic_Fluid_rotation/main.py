from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

# Erstellen Sie eine Figur für den Plot.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definieren Sie den Bereich und das Gitter für r und T.
r0 = 1.5
r = np.linspace(0, r0, 100)  # Radiuswerte von 0 bis 1.5
T = np.linspace(0, 2 * np.pi, 100)  # Theta von 0 bis 2*pi
r, T = np.meshgrid(r, T)

# Parametrisieren Sie X, Y nach den polaren Koordinaten.
X = r * np.cos(T)
Y = r * np.sin(T)

# Setzen Sie omega und g.
omega = 2  # Winkelgeschwindigkeit, anpassbar
g = 9.81  # Erdbeschleunigung in m/s^2

# Berechnen Sie Z basierend auf der gegebenen Formel für die rotierende Flüssigkeit.
Z = (omega ** 2 * r ** 2) / (2 * g)

# Erstellen Sie die Oberfläche.
surf = ax.plot_surface(X, Y, Z, alpha=0.9, rstride=5, cstride=5, linewidth=0.5, cmap='summer')

b=1.2 # Contour offset
# Projektionen auf die Ebenen:
# Konturlinien auf der XY-Ebene
ax.contour(X, Y, Z, zdir='z', offset=-0.2, cmap='summer')
# Konturlinien auf der XZ-Ebene
ax.contour(X, Y, Z, zdir='y', offset=-1.5*b, cmap='summer')
# Konturlinien auf der YZ-Ebene
ax.contour(X, Y, Z, zdir='x', offset=-1.5*b, cmap='summer')


# Achsenlimits festlegen
ax.set_xlim(-r0*b, r0*b)
ax.set_ylim(-r0*b, r0*b)
ax.set_zlim(-0.2, 1.0)

# Achsenbeschriftungen.
ax.set_xlabel('X Koordinate')
ax.set_ylabel('Y Koordinate')
ax.set_zlabel('Höhe der Flüssigkeit (Z)')

# Titel hinzufügen.
ax.set_title('3D Plot der parabolischen Flüssigkeitsoberfläche bei Rotation')

# Zeigen Sie den Plot.
plt.show()
