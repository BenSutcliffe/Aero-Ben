import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("FlightProfileDataClone.xlsx")

time_array = np.array(df.iloc[:, 0])
x_array = np.array(df.iloc[:, 1])
y_array = np.array(df.iloc[:, 2])
z_array = np.array(df.iloc[:, 3])
vx_array = np.array(df.iloc[:, 4])
vy_array = np.array(df.iloc[:, 5])
vz_array = np.array(df.iloc[:, 6])
ax_array = np.array(df.iloc[:, 7])
ay_array = np.array(df.iloc[:, 8])
az_array = np.array(df.iloc[:, 9])
e0_array = np.array(df.iloc[:, 10])
e1_array = np.array(df.iloc[:, 11])
e2_array = np.array(df.iloc[:, 12])
e3_array = np.array(df.iloc[:, 13])
mach_array = np.array(df.iloc[:, 14])
q_array = np.array(df.iloc[:, 15])
pressure_array = np.array(df.iloc[:, 16])
density_array = np.array(df.iloc[:, 17])