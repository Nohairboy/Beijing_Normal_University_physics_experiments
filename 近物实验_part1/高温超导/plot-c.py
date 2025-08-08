import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data provided
data = {
    "T": [
        180.228269, 175.759742, 171.220286, 166.775402, 161.337512, 158.216636,
        151.78574, 147.222641, 144.385481, 141.973895, 139.987883, 136.299575,
        131.854691, 126.842375, 121.569986, 117.550676, 114.004226, 111.025208,
        108.306263, 105.847391, 103.246661, 100.504073, 98.730848, 98.447132,
        98.139773, 97.714199, 97.217696, 96.69755, 96.390191, 96.201047,
        96.011903, 95.917331, 95.846402, 95.775473, 95.75183, 95.680901,
        95.633615, 95.5154, 95.491757, 95.444471, 95.373542, 95.302613,
        95.255327, 95.160755, 95.089826, 95.018897, 94.924325, 94.829753,
        94.758824, 94.687895, 94.56968, 94.475108, 94.451465, 94.427822
    ],
    "R": [
        0.053, 0.052, 0.051, 0.05, 0.049, 0.048, 0.047, 0.046, 0.045, 0.044,
        0.043, 0.042, 0.041, 0.04, 0.039, 0.038, 0.037, 0.036, 0.035, 0.034,
        0.033, 0.032, 0.031, 0.03, 0.029, 0.028, 0.027, 0.026, 0.025, 0.024,
        0.023, 0.022, 0.021, 0.02, 0.019, 0.018, 0.017, 0.016, 0.015, 0.014,
        0.013, 0.012, 0.011, 0.01, 0.009, 0.008, 0.007, 0.006, 0.005, 0.004,
        0.003, 0.002, 0.001, 0
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Redefine Tc_onset and Tc0 based on provided values
Tc_onset = 98.730  # Provided onset temperature
Tc0 = 94.427822    # Provided zero-resistance temperature

# Calculate Tc as the midpoint of the resistance transition
transition_data = df[(df["T"] <= Tc_onset) & (df["T"] >= Tc0)]
Tc = transition_data["T"].mean()  # Midpoint in the transition region

# Replot the curve with updated annotations
plt.figure(figsize=(10, 6))
# plt.plot(df["T"], df["R"], marker="x", linestyle="-", label="Resistance vs Temperature")

plt.plot(df["T"], df["R"], label="Resistance vs Temperature", color='red', linewidth=2)
plt.scatter(df["T"], df["R"], color='black', s=5, alpha=0.7,marker="x")

plt.xlabel("Temperature (T) [K]")
plt.ylabel("Resistance (R) [Ω]")
plt.title("Superconducting Transition Curve")
plt.grid()
plt.legend()

# Add new lines for Tc_onset, Tc, and Tc0
plt.axvline(x=Tc_onset, color="red", linestyle="--", label=f"Tc_onset = {Tc_onset:.2f} K")
plt.axvline(x=Tc, color="green", linestyle="--", label=f"Tc = {Tc:.2f} K")
plt.axvline(x=Tc0, color="blue", linestyle="--", label=f"Tc0 = {Tc0:.2f} K")
plt.legend()

plt.show()