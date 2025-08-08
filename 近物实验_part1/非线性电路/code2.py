import numpy as np
import matplotlib.pyplot as plt

# Revised data based on provided image
U_data_corrected = np.array([
    -12.2813, -11.6906, -11.4096, -10.9302, -10.7310, -10.3346, -10.3083, -10.1226, 
    -9.6989, -9.3008, -8.7214, -8.4511, -7.7059, -7.2711, -6.8283, -6.3327, -5.7177, 
    -5.3178, -4.8578, -4.3522, -3.7637, -3.2507, -2.6982, -2.2702, -1.9208, -1.3833, 
    -1.0777, -0.6334, -0.3662, -0.1161, 0.1161, 0.3662, 0.6334, 1.0777, 1.3833, 
    1.9208, 2.2702, 2.6982, 3.2507, 3.7637, 4.3522, 4.8578, 5.3178, 5.7177, 
    6.3327, 6.8283, 7.2711, 7.7059, 8.4511, 8.7214, 9.3008, 9.6989, 10.1226, 
    10.3083, 10.3346, 10.7310, 10.9302, 11.4096, 11.6906, 12.0257, 12.2813
])
I_data_corrected = np.array([
    0.3820, 0.9961, 1.5336, 1.8029, 2.4805, 2.9427, 3.1668, 3.6387, 
    4.1203, 4.5212, 4.8670, 4.9044, 4.6878, 4.5212, 4.1609, 3.8475, 
    3.6641, 3.4777, 3.0110, 2.6507, 2.4392, 2.1939, 1.9730, 1.7523, 
    1.5750, 1.2582, 0.9485, 0.5474, 0.3208, 0.1196, -0.1196, -0.3208, 
    -0.5474, -0.9485, -1.2582, -1.5750, -1.7523, -1.9730, -2.1939, -2.4392, 
    -2.6507, -3.0110, -3.2693, -3.4777, -3.6641, -3.8475, -4.1609, -4.5212, 
    -4.6878, -4.9044, -4.8670, -4.5212, -4.1203, -3.6387, -3.1668, -2.9427, 
    -2.4805, -1.8029, -1.5336, -0.9961, -0.3820
])

# Define intervals for linear fitting
intervals = [
    (-12.2813, -10.3083),
    (-10.1226, -1.38),
    (-1.38, 1.38),
    (1.38, 10.1226),
    (10.3083, 12.2813)
]

# Function to perform linear fitting in each interval
fit_results = []
for interval in intervals:
    U_interval = U_data_corrected[(U_data_corrected >= interval[0]) & (U_data_corrected <= interval[1])]
    I_interval = I_data_corrected[(U_data_corrected >= interval[0]) & (U_data_corrected <= interval[1])]
    slope, intercept = np.polyfit(U_interval, I_interval, 1)
    fit_results.append((interval, slope, intercept))

# Visualize the combined data with linear fits for each segment
plt.figure(figsize=(10, 7))
# plt.plot(U_data_corrected, I_data_corrected, 'k--', label="Measured Data")
plt.scatter(U_data_corrected, I_data_corrected, marker='o', color='r')
plt.title("Nonlinear Negative Resistance I-U Characteristic with Segmented Linear Fits")
plt.xlabel("Voltage U (V)")
plt.ylabel("Current I (mA)")
plt.grid(True)

# Plot linear fit for each segment
for interval, slope, intercept in fit_results:
    U_fit = np.linspace(interval[0], interval[1], 100)
    I_fit = slope * U_fit + intercept
    plt.plot(U_fit, I_fit, label=f"Fit for U in [{interval[0]}, {interval[1]}]: y = {slope:.2f}x + {intercept:.2f}")

plt.legend()
plt.show()

# Display the fit results
fit_results
