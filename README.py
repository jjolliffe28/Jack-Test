import matplotlib.pyplot as plt
import math

# Constants
GRAVITY = 9.81
RHO = 1.225 # Air density at 70 degrees Fahrenheit and sea level pressure
DRAG_COEFFICIENT = 0.2
BALL_RADIUS = 0.02135 # meters

# Inputs
ball_speed = 80 # mph
spin_rate = 3000 # rpm
launch_angle = 12 # degrees
ball_mass = 0.04593 # kg
initial_position = (0, 0) # x, y coordinates in meters
wind_speed = 0 # mph

# Convert inputs to SI units
ball_speed_mps = ball_speed * 0.44704 # mph to m/s
spin_rate_rps = spin_rate / 60 # rpm to rps
launch_angle_rad = math.radians(launch_angle) # degrees to radians
wind_speed_mps = wind_speed * 0.44704 # mph to m/s

# Calculate initial velocity components
launch_speed_mps = ball_speed_mps * math.cos(launch_angle_rad)
launch_direction_rad = math.atan2(ball_speed_mps * math.sin(launch_angle_rad), launch_speed_mps)
launch_direction_deg = math.degrees(launch_direction_rad)

# Calculate air resistance and spin decay coefficients
cross_sectional_area = math.pi * BALL_RADIUS**2 # Assume spherical ball
air_resistance_coef = (0.5 * RHO * DRAG_COEFFICIENT * cross_sectional_area) / ball_mass
spin_decay_coef = (0.5 * RHO * cross_sectional_area * BALL_RADIUS**3) / (2/5 * ball_mass)

# Simulation time step and duration
delta_t = 0.001 # seconds
t = 0
t_end = 10 # seconds

# Simulation variables
position = initial_position
velocity = (launch_speed_mps * math.cos(launch_direction_rad) + wind_speed_mps, launch_speed_mps * math.sin(launch_direction_rad))
spin = spin_rate_rps * math.pi / 30 # rps to rad/s
total_spin = spin

# Lists to store trajectory data
x = [position[0]]
y = [position[1]]

# Run simulation until ball hits the ground or reaches end of simulation time
while position[1] >= 0 and t < t_end:
    # Calculate acceleration due to gravity and air resistance
    g = -GRAVITY
    air_resistance = air_resistance_coef * velocity[0]**2
    acceleration = (g + air_resistance) * math.sin(launch_direction_rad), (g + air_resistance) * math.cos(launch_direction_rad)
    
    # Update velocity and position
    velocity = velocity[0] + acceleration[0] * delta_t, velocity[1] + acceleration[1] * delta_t
    position = position[0] + velocity[0] * delta_t, position[1] + velocity[1] * delta_t
    
    # Update spin and spin direction
    spin_decay = spin_decay_coef * velocity[0]**2 * delta_t
    spin = spin - spin_decay
    total_spin = total_spin - spin_decay
    spin_direction_rad = math.atan2(total_spin, velocity[0])
    spin_direction_deg = math.degrees(spin_direction_rad)
    
    # Append position to trajectory lists
    x.append(position[0])
    y.append(position[1])
    
    # Increment simulation time
    t += delta_t

# Create plot of trajectory
plt.plot(x, y)
plt.title("Golf Shot")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.gca().set_aspect('equal', adjustable='box')
plt.annotate("Ball speed: {} mph".format(round(ball_speed)), xy=(0.05, 0.95), xycoords='axes fraction')
plt.annotate("Spin rate: {} rpm".format(round(spin_rate)), xy=(0.05, 0.9), xycoords='axes fraction')
plt.annotate("Launch angle: {} degrees".format(round(launch_angle)), xy=(0.05, 0.85), xycoords='axes fraction')
plt.annotate("Total distance: {:.1f} m".format(x[-1]), xy=(0.05, 0.8), xycoords='axes fraction')
plt.annotate("Total hang time: {:.1f} s".format(t), xy=(0.05, 0.75), xycoords='axes fraction')
plt.annotate("Max height: {:.1f} m".format(max(y)), xy=(0.05, 0.7), xycoords='axes fraction')
plt.annotate("Wind speed: {} mph".format(wind_speed), xy=(0.05, 0.65), xycoords='axes fraction')
plt.annotate("Launch direction: {} degrees".format(round(launch_direction_deg)), xy=(0.05, 0.6), xycoords='axes fraction')
plt.annotate("Spin direction: {} degrees".format(round(spin_direction_deg)), xy=(0.05, 0.55), xycoords='axes fraction')
plt.show()

