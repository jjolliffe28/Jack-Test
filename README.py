import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define initial conditions for ball flight
ball_speed = 150    # mph
spin_rate = 3000    # rpm
launch_angle = 12   # degrees
side_spin = 0       # rpm
back_spin = 0       # rpm
ball_position = np.array([0, 0, 0])  # x, y, z coordinates in feet
ball_velocity = np.array([
    ball_speed * np.cos(np.radians(launch_angle)),  # x velocity in ft/s
    0,  # y velocity in ft/s (assume level ground)
    ball_speed * np.sin(np.radians(launch_angle))  # z velocity in ft/s
])
gravity = np.array([0, -32.2, 0])  # acceleration due to gravity in ft/s^2
time_step = 0.01  # time step for simulation in seconds
flight_time = 10  # total flight time in seconds

# Create an array of time values
time = np.arange(0, flight_time, time_step)

# Create arrays to store ball position and velocity at each time step
position = np.zeros((len(time), 3))
velocity = np.zeros((len(time), 3))
position[0] = ball_position
velocity[0] = ball_velocity

# Simulate the ball flight
for i in range(1, len(time)):
    # Calculate the total spin of the ball
    spin = np.sqrt(spin_rate**2 + side_spin**2 + back_spin**2)
    
    # Calculate the Magnus force on the ball due to spin
    magnus_force = 0.5 * np.pi * 0.225 * spin / 1000 * np.cross(velocity[i-1], [spin_rate, side_spin, back_spin])
    
    # Calculate the acceleration on the ball due to gravity and Magnus force
    acceleration = gravity + magnus_force / 0.04593
    
    # Update the ball velocity and position
    velocity[i] = velocity[i-1] + acceleration * time_step
    position[i] = position[i-1] + velocity[i] * time_step

# Plot the ball trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Ball Trajectory')
ax.set_xlabel('X Position (ft)')
ax.set_ylabel('Y Position (ft)')
ax.set_zlabel('Z Position (ft)')
plt.legend()
plt.show()
