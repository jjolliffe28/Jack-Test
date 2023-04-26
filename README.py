import math

# Define constants
DRAG_COEFFICIENT = 0.295
BALL_DIAMETER = 0.04267 # meters
BALL_MASS = 0.04593 # kg
GRAVITY = 9.81 # m/s^2
TEMPERATURE = 21.11 # Celsius
ALTITUDE = 192 # meters

# Define input variables
club_head_speed = float(input("Enter club head speed (m/s): "))
ball_speed = float(input("Enter ball speed (m/s): "))
spin_rate = float(input("Enter spin rate (rpm): "))
launch_angle = float(input("Enter launch angle (degrees): "))

# Calculate variables
ball_area = math.pi * (BALL_DIAMETER/2)**2
ball_velocity = ball_speed * 0.44704 # convert to m/s
air_density = 1.2929 * ((273.15 + TEMPERATURE - 0.0065 * ALTITUDE) / 273.15)**(-5.256)
spin_ratio = spin_rate / ball_speed
ball_mass = BALL_MASS
time_of_flight = (2 * ball_velocity * math.sin(math.radians(launch_angle))) / GRAVITY

# Calculate distance
distance = 0
delta_t = 0.01
x = 0
y = 0
vx = ball_velocity * math.cos(math.radians(launch_angle))
vy = ball_velocity * math.sin(math.radians(launch_angle))

while y >= 0:
    delta_v = air_density * ball_area * (vx**2 + vy**2) * DRAG_COEFFICIENT / (2 * ball_mass)
    delta_vx = -delta_v * vx / math.sqrt(vx**2 + vy**2)
    delta_vy = -delta_v * vy / math.sqrt(vx**2 + vy**2)
    delta_vy += spin_ratio * delta_t
    vx += delta_vx * delta_t
    vy += (delta_vy - GRAVITY) * delta_t
    x += vx * delta_t
    y += vy * delta_t
    distance = x

# Print result
print("The golf ball will travel approximately {:.2f} yards".format(distance * 1.09361))
