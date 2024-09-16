import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # mass of the sun (kg)
dt = 24 * 3600  # time step (1 day in seconds)
num_steps = 365 * 5  # simulate for 5 years

# Function to calculate gravitational force
def gravitational_force(r):
    distance = np.linalg.norm(r)
    force_magnitude = G * M_sun / distance**2
    force_direction = -r / distance  # force is in the direction towards the Sun
    return force_magnitude * force_direction

# Initialize position and velocity (Earth around Sun)
pos = np.array([1.496e11, 0])  # 1 AU in meters
vel = np.array([0, 29.78e3])  # initial velocity (Earth's speed in m/s)

# Lists to store position for plotting
x_positions = []
y_positions = []

# Time evolution (Explicit Euler method)
for step in range(num_steps):
    # Calculate gravitational force and acceleration
    force = gravitational_force(pos)
    acc = force  # no need to divide by mass since we're assuming unit mass

    # Save positions for plotting
    x_positions.append(pos[0])
    y_positions.append(pos[1])

    # Update position and velocity using Explicit Euler
    pos += vel * dt  # r(t+dt) = r(t) + v(t) * dt
    vel += acc * dt  # v(t+dt) = v(t) + a(t) * dt

# Plot the orbit
plt.plot(x_positions, y_positions)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Orbit of a Planet around the Sun (Explicit Euler Method)')
plt.scatter(0, 0, color='yellow', s=300, label='Sun', edgecolor='black')  # 's' controls the size of the Sun
plt.gca().set_aspect('equal', adjustable='box')  # Set equal scaling for x and y axes
plt.show()
