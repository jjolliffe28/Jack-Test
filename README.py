import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input data
ball_speed = 150  # mph
launch_angle = 10  # degrees
backspin = 3000  # rpm
side_spin = 500  # rpm
carry_distance = 200  # yards
offline = -10  # yards
wind_speed = 5  # mph
wind_direction = 90  # degrees

# Constants
g = 32.2  # ft/s^2
rho = 0.00238  # lb/ft^3
d = 1.68  # in
m = 0.0459  # lb
cd = 0.25  # coefficient of drag
cl = 0.15  # coefficient of lift
S = np.pi * (d/2)**2  # ft^2
theta = np.radians(launch_angle)
vx0 = ball_speed * np.cos(theta)
vy0 = ball_speed * np.sin(theta)
vz0 = 0
wx0 = side_spin * np.pi / 30
wy0 = backspin * np.pi / 30
wz0 = 0
vxw0 = wind_speed * np.cos(np.radians(wind_direction))
vyw0 = wind_speed * np.sin(np.radians(wind_direction))
vzw0 = 0

# Simulation
tmax = 10  # seconds
dt = 0.01  # seconds
t = np.arange(0, tmax, dt)
x = np.zeros_like(t)
y = np.zeros_like(t)
z = np.zeros_like(t)
vx = np.full_like(t, vx0)
vy = np.full_like(t, vy0)
vz = np.full_like(t, vz0)
wx = np.full_like(t, wx0)
wy = np.full_like(t, wy0)
wz = np.full_like(t, wz0)
vxw = np.full_like(t, vxw0)
vyw = np.full_like(t, vyw0)
vzw = np.full_like(t, vzw0)

for i in range(1, len(t)):
    # Velocity due to spin
    v_spin = np.sqrt(wx[i-1]**2 + wy[i-1]**2 + wz[i-1]**2) * d/2
    drag = 0.5 * rho * v_spin**2 * cd * S
    lift = 0.5 * rho * v_spin**2 * cl * S
    fx_spin = -lift * wy[i-1] - drag * wx[i-1]
    fy_spin = lift * wx[i-1] - drag * wy[i-1]
    fz_spin = 0
    # Velocity due to wind
    fx_wind = -0.5 * rho * S * cd * (vx[i-1] - vxw[i-1])**2
    fy_wind = -0.5 * rho * S * cd * (vy[i-1] - vyw[i-1])**2
    fz_wind = -0.5 * rho * S * cd * (vz[i-1] - vzw[i-1])**2
    # Acceleration
    ax = (fx_spin + fx_wind) / m
    ay = (fy_spin + fy_wind) / m
    az = -g + fz_spin



    # Update velocity
    vx[i] = vx[i-1] + ax * dt
    vy[i] = vy[i-1] + ay * dt
    vz[i] = vz[i-1] + az * dt
    # Update position
    x[i] = x[i-1] + vx[i] * dt
    y[i] = y[i-1] + vy[i] * dt
    z[i] = z[i-1] + vz[i] * dt

# Plot 3D trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x/3, y/3, z/3, 'b-', linewidth=2)
ax.set_xlabel('X (yards)')
ax.set_ylabel('Y (yards)')
ax.set_zlabel('Z (yards)')
ax.set_xlim(0, 500)
ax.set_ylim(-250, 250)
ax.set_zlim(0, 150)
plt.show()




    # Update velocity
    vx[i] = vx[i-1] + ax * dt
    vy[i] = vy[i-1] + ay * dt
    vz[i] = vz[i-1] + az * dt
    # Update position
    x[i] = x[i-1] + vx[i] * dt
    y[i] = y[i-1] + vy[i] * dt
    z[i] = z[i-1] + vz[i] * dt

# Plot 3D trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x/3, y/3, z/3, 'b-', linewidth=2)
ax.set_xlabel('X (yards)')
ax.set_ylabel('Y (yards)')
ax.set_zlabel('Z (yards)')
ax.set_xlim(0, 500)
ax.set_ylim(-250, 250)
ax.set_zlim(0, 150)
plt.show()




import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input data
ball_speed = 150  # mph
launch_angle = 10  # degrees
backspin = 3000  # rpm
side_spin = 500  # rpm
carry_distance = 200  # yards
offline = -10  # yards
wind_speed = 5  # mph
wind_direction = 90  # degrees

# Constants
g = 32.2  # ft/s^2
rho = 0.00238  # lb/ft^3
d = 1.68  # in
m = 0.0459  # lb
cd = 0.25  # coefficient of drag
cl = 0.15  # coefficient of lift
S = np.pi * (d/2)**2  # ft^2
theta = np.radians(launch_angle)
vx0 = ball_speed * np.cos(theta)
vy0 = ball_speed * np.sin(theta)
vz0 = 0
wx0 = side_spin * np.pi / 30
wy0 = backspin * np.pi / 30
wz0 = 0
vxw0 = wind_speed * np.cos(np.radians(wind_direction))
vyw0 = wind_speed * np.sin(np.radians(wind_direction))
vzw0 = 0

# Simulation
tmax = 10  # seconds
dt = 0.01  # seconds
t = np.arange(0, tmax, dt)
x = np.zeros_like(t)
y = np.zeros_like(t)
z = np.zeros_like(t)
vx = np.full_like(t, vx0)
vy = np.full_like(t, vy0)
vz = np.full_like(t, vz0)
wx = np.full_like(t, wx0)
wy = np.full_like(t, wy0)
wz = np.full_like(t, wz0)
vxw = np.full_like(t, vxw0)
vyw = np.full_like(t, vyw0)
vzw = np.full_like(t, vzw0)

for i in range(1, len(t)):
    # Velocity due to spin
    v_spin = np.sqrt(wx[i-1]**2 + wy[i-1]**2 + wz[i-1]**2) * d/2
    drag = 0.5 * rho * v_spin**2 * cd * S
    lift = 0.5 * rho * v_spin**2 * cl * S
    fx_spin = -lift * wy[i-1] - drag * wx[i-1]
    fy_spin = lift * wx[i-1] - drag * wy[i-1]
    fz_spin = 0
    # Velocity due to wind
    fx_wind = -0.5 * rho * S * cd * (vx[i-1] - vxw[i-1])**2
    fy_wind = -0.5 * rho * S * cd * (vy[i-1] - vyw[i-1])**2
    fz_wind = -0.5 * rho * S * cd * (vz[i-1] - vzw[i-1])**2
    # Acceleration
    ax = (fx_spin + fx_wind) / m
    ay = (fy_spin + fy_wind) / m
    az = -g + fz_spin + fz_wind
    # Velocity
    vx[i] = vx[i-1] + ax * dt
