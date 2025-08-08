import matplotlib.pyplot as plt
import numpy as np

# Define the temperature range and critical magnetic field equation
T = np.linspace(0, 0.1, 500)  # Normalized temperature T/Tc
Hc = 1 - 100* T**2  # Parabolic relationship

# Plot the figure
plt.figure(figsize=(6, 4))
plt.plot(T, Hc, label=r"$H_c(T) = H_c(0) [1 - (T/T_c)^2]$", color="black", linewidth=2)

plt.text(0.02, 0.4, "Superconducting State", fontsize=10, color="black")
plt.text(0.06, 0.8, "Normal State", fontsize=10, color="black")
plt.text(0.95, 0.05, r"$T_c$", fontsize=10, color="black")

# # Hide axis ticks
plt.xticks([0])
plt.yticks([0])

# Labels and title
plt.xlabel(r"Temperature $T$", fontsize=10)
plt.ylabel(r"Critical Magnetic Field $H_c$", fontsize=10)
plt.title("TCritical Magnetic Field for Type I Superconductors", fontsize=12)
plt.tight_layout()

plt.show()
