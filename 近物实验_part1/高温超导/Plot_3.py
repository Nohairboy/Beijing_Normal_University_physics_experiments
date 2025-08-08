import matplotlib.pyplot as plt
import numpy as np

# Define temperature and resistance relationship
T = np.linspace(0, 80, 500)
R = 50* 0.01 * (T / 225)**2  # Simulating the resistance relationship at low temperatures
print(50* 0.01 * (75 / 225)**2)

# Plot the figure
plt.figure(figsize=(6, 4))
plt.plot(T, R, color="black", linewidth=2, label="Platinum Resistance")

# Add annotation for Debye temperature
Theta_D = 225
plt.axvline(x=Theta_D/3, color="black", linestyle="--", label=r"$\Theta_D/3$")
plt.text(65, 0.055, r"$\Theta_D/3$", fontsize=10, color="black")

# Labels and title
plt.xlabel(r"Temperature $T$ (K)", fontsize=10)
plt.ylabel(r"Resistance $R$ $(\Omega)$", fontsize=10)
plt.title("Temperature Dependence of Platinum Resistance", fontsize=12)

plt.yticks([0.055/2,0.055],[5,10])

# Add a note for R(0°C)
plt.text(10, 0.055, r"Platinum $R(0^\circ C) = 50\ \Omega$", fontsize=10)


plt.show()
