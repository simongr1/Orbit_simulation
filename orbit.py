import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # mass of the sun (kg)
dt = 24 * 3600  # time step (1 day in seconds)
num_steps = 365 * 5  # simulate for 5 years
tolerance = 1e-6  # tolerance for Newton's method convergence
max_iters = 10  # maximum iterations for Newton's method

# Function to calculate gravitational force
def gravitational_force(r):
    distance = np.linalg.norm(r)
    force_magnitude = G * M_sun / distance**2
    force_direction = -r / distance  # force is in the direction towards the Sun
    return force_magnitude * force_direction

# Function to perform Newton's method iteration
def newtons_method_for_position_and_velocity(r, v):
    for i in range(max_iters):
        # Compute acceleration based on the current guess for position
        acc = gravitational_force(r)
        
        # Update velocity using implicit Euler equation
        v_new = v + acc * dt
        
        # Update position using implicit Euler equation
        r_new = r + v_new * dt
        
        # Check for convergence (if position difference is small)
        if np.linalg.norm(r_new - r) < tolerance:
            return r_new, v_new
        
        # Update the guess for the next iteration
        r = r_new
        v = v_new

    return r, v  # return the final values after iterations

# Initialize position and velocity (Earth around Sun)
pos = np.array([1.496e11, 0])  # 1 AU in meters
vel = np.array([0, 29.78e3])  # initial velocity (Earth's speed in m/s)

# Lists to store position for plotting
x_positions = []
y_positions = []

# Time evolution (True Implicit Euler method using Newton's method)
for step in range(num_steps):
    # Save positions for plotting
    x_positions.append(pos[0])
    y_positions.append(pos[1])

    # Perform Newton's method to compute the next position and velocity
    pos, vel = newtons_method_for_position_and_velocity(pos, vel)

# Plot the orbit
plt.plot(x_positions, y_positions)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Orbit of a Planet around the Sun (Verlet Method)')
plt.scatter(0, 0, color='yellow', s=300, label='Sun', edgecolor='black')  # 's' controls the size of the Sun
plt.gca().set_aspect('equal', adjustable='box')  # Set equal scaling for x and y axes
plt.show()
