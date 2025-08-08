# plot_2

import matplotlib.pyplot as plt
import numpy as np

# Define the temperature range
T = np.linspace(0, 1, 500)  # Normalized temperature T/Tc

# Define the critical magnetic field equations
Hc1 = 0.2 * (1 - T**2)  # Lower critical field
Hc2 = 1 - T**2  # Upper critical field

# Plot the figure
plt.figure(figsize=(6, 4))
plt.plot(T, Hc1, label=r"$H_{c1}(T)$", color="black", linewidth=2)
plt.plot(T, Hc2, label=r"$H_{c2}(T)$", color="black", linewidth=2)

# Add annotations for different states
plt.fill_between(T, Hc1, Hc2, color="gray", alpha=0.3, label="Mixed State")
plt.text(0.3, 0.4, "Mixed State", fontsize=10, color="black")
plt.text(0.2, 0.05, "Superconducting State", fontsize=10, color="black")
plt.text(0.5, 0.85, "Normal State", fontsize=10, color="black")

# Axes labels and title
plt.xlabel(r"Temperature $T$", fontsize=12)
plt.ylabel(r"Magnetic Field $H$", fontsize=12)
plt.title("Critical Magnetic Fields of Type II Superconductors", fontsize=12)

# Hide axis ticks
plt.xticks([])
plt.yticks([])

# Add grid for better readability
plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

plt.show()
