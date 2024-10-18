import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
c = 1  # wave speed
L = 10  # spatial domain size
T = 20  # time duration
nx = 100  # number of spatial points
nt = 200  # number of time points

# Spatial and temporal discretization
x = np.linspace(-L, L, nx)
y = np.linspace(-L, L, nx)
t = np.linspace(0, T, nt)
X, Y = np.meshgrid(x, y)

# Initial conditions
def initial_wave(X, Y):
    return np.exp(-0.1 * (X**2 + Y**2))

# Analytic solution of the wave equation
def wave_solution(X, Y, t, c):
    r = np.sqrt(X**2 + Y**2)
    return initial_wave(X, Y) * np.cos(c * r - t)

# Create a figure and axis
fig, ax = plt.subplots()
cax = ax.imshow(wave_solution(X, Y, 0, c), extent=[-L, L, -L, L], origin='lower', cmap='viridis')
fig.colorbar(cax)

# Animation function
def animate(i):
    ax.clear()
    cax = ax.imshow(wave_solution(X, Y, t[i], c), extent=[-L, L, -L, L], origin='lower', cmap='viridis')
    return cax,

# Create animation
ani = FuncAnimation(fig, animate, frames=nt, interval=50, blit=False)

plt.show()