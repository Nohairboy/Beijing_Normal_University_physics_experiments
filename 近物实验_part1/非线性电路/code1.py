import pandas as pd

# Manually cleaned data based on the OCR output and the image content
data = {
    "U (V)": [
        0.1161, 0.3662, 0.6334, 1.0777, 1.3833, 1.9208, 2.2702, 2.6982, 3.2507, 3.7637, 
        4.3522, 4.8578, 5.3178, 5.7177, 6.3327, 6.8283, 7.2711, 7.7059, 8.4511, 8.7214, 
        9.3008, 9.6989, 10.1226, 10.3083, 10.3346, 10.7310, 10.9302, 11.1252, 11.2179, 
        11.4096, 11.6906, 11.8026, 12.0257, 12.2813
    ],
    "I (mA)": [
        0.1196, 0.3208, 0.5474, 0.9485, 1.2582, 1.4304, 1.5750, 1.7523, 1.9730, 2.1939, 
        2.4392, 2.6507, 2.8431, 3.0110, 3.2693, 3.4777, 3.6641, 3.8475, 4.1609, 4.2724, 
        4.5212, 4.6878, 4.8670, 4.9044, 4.5946, 4.1203, 3.6387, 3.1668, 2.9427, 2.4805, 
        1.8029, 1.5336, 0.9961, 0.3820
    ]
}

# Convert to DataFrame
df_data = pd.DataFrame(data)



import numpy as np

# Original data provided in the form (U, I) based on extracted data.
U_data = np.array(df_data["U (V)"])
I_data = np.array(df_data["I (mA)"])

# Step 1: Transform data to the second quadrant by flipping U values and keeping I the same.
U_second_quadrant = -U_data
I_second_quadrant = I_data

# Step 2: Rotate second quadrant data by 180 degrees to simulate moving to the fourth quadrant.
U_fourth_quadrant = -U_second_quadrant
I_fourth_quadrant = -I_second_quadrant

# Combine second and fourth quadrant data to simulate the full characteristic curve.
U_combined = np.concatenate([U_second_quadrant, U_fourth_quadrant])
I_combined = np.concatenate([I_second_quadrant, I_fourth_quadrant])



import matplotlib.pyplot as plt

# Plot U-I curve for the nonlinear circuit experiment
plt.figure(figsize=(8, 6))

# # figure1
# plt.scatter(U_data, I_data, marker='o', color='r')

# # figure2
plt.scatter(U_combined, I_combined, marker='o' , color='r')

# # figure3
# plt.scatter(U_combined, I_combined, marker='x', s=20, color='black')
# # Define intervals for linear fitting
# intervals = [
#     (-12.2813, -10.3083),
#     (-10.1226, -1.38),
#     (-1.38, 1.38),
#     (1.38, 10.1226),
#     (10.3083, 12.2813)
# ]

# # Function to perform linear fitting in each interval
# fit_results = []
# for interval in intervals:
#     U_interval = U_combined[(U_combined >= interval[0]) & (U_combined <= interval[1])]
#     I_interval = I_combined[(U_combined >= interval[0]) & (U_combined <= interval[1])]
#     slope, intercept = np.polyfit(U_interval, I_interval, 1)
#     fit_results.append((interval, slope, intercept))

# # Plot linear fit for each segment
# for interval, slope, intercept in fit_results:
#     U_fit = np.linspace(interval[0], interval[1], 100)
#     I_fit = slope * U_fit + intercept
#     plt.plot(U_fit, I_fit, label=f"Fit for U in [{interval[0]}, {interval[1]}]: y = {slope:.2f}x + {intercept:.2f}")


plt.xlabel("U (V)")
plt.ylabel("I (mA)")
plt.grid(True)
plt.legend()
plt.show()
