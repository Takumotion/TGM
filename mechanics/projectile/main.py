import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def formula(v_1, v_2):
    # setting
    x_1 = v_1*t
    y_1 = -g * t**2 / 2 + h

    x_2 = v_2*t
    y_2 = -g * t**2 / 2 + h

    return y_1,y_2,x_1,x_2

# general variable and constant values
t = np.linspace(0, 100, 10000)
g = 9.81 #m/s**2
v_1 = 10 #m/s
v_2 = 5 #m/s
h=10

y_1,y_2,x_1,x_2 = formula(v_1, v_2)

fig, ax = plt.subplots()
scat_1 = ax.scatter(x_1[0], y_1[0], c="b", s=5, label=f'v0 = {v_1} m/s')
scat_2 = ax.scatter(x_2[0], y_2[0], c="g", s=5, label=f'v0 = {v_2} m/s')

# line2 = ax.plot(t[0], y_2[0], label=f'v0 = {v_2} m/s')[0]


ax.set(xlim=[0, 20], ylim=[-4, 11], xlabel='Path [m]', ylabel='H [m]')
ax.legend()

def update(frame):
    # for each frame, update the data stored on each artist.
    x1 = x_1[:frame]
    y1 = y_1[:frame]
    # update the scatter plot:
    data1 = np.stack([x1, y1]).T
    scat_1.set_offsets(data1)

    # for each frame, update the data stored on each artist.
    x2 = x_2[:frame]
    y2 = y_2[:frame]
    # update the scatter plot:
    data2 = np.stack([x2, y2]).T
    scat_2.set_offsets(data2)

    # update the line plot:
    # line2.set_xdata(t[:frame])
    # line2.set_ydata(y_2[:frame])
    return (scat_1, scat_2)

ani = animation.FuncAnimation(fig=fig, func=update, frames=200, interval=10)
plt.show()