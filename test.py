# Damped Harmonic Oscillator Visualization

import numpy as np
import matplotlib.pyplot as plt

# Constants and initial conditions
mass = 1.0
damping_coefficient = 0.5
spring_constant = 1.0

# Derived parameters
angular_frequency_0 = np.sqrt(spring_constant / mass)
damping_ratio = damping_coefficient / (2 * mass * angular_frequency_0)
damped_angular_frequency = angular_frequency_0 * np.sqrt(1 - damping_ratio**2)


time = np.linspace(0, 10, 1000)

# Initial conditions
A = 1.0
B = 1.0

#dho
displacement = np.exp(-damping_ratio * angular_frequency_0 * time) * (
    A * np.cos(damped_angular_frequency * time) + B * np.sin(damped_angular_frequency * time)
)


plt.figure(figsize=(8, 5))
plt.plot(time, displacement, label='Displacement $x(t)$')
plt.title('The Enchanting Damped Harmonic Oscillator')
plt.xlabel('Time $t$')
plt.ylabel('Displacement $x(t)$')
plt.legend()
plt.grid(True)
plt.show()
