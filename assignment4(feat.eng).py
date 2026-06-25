#FEATURE ENGINEERING

#Exercise 1: Feature Scaling
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [18, 25, 40, 60],
    "Salary": [15000, 30000, 80000, 150000],
    "Experience": [0, 3, 10, 35]
}

df = pd.DataFrame(data)

std_scaler = StandardScaler()
std_scaled = std_scaler.fit_transform(df)

print("Standard Scaled Data:\n", std_scaled)

minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)

print("\nMinMax Scaled Data:\n", minmax_scaled)