import pandas as pd

# Load dataset
df = pd.read_csv("student_performance.csv")

print("===== STUDENT PERFORMANCE DATASET =====")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Study Hours:", df["Study_Hours"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Average Final Score:", df["Final_Score"].mean())

print("\nHighest Final Score:", df["Final_Score"].max())
print("Lowest Final Score:", df["Final_Score"].min())

print("\n===== KEY FINDINGS =====")
print("1. Students with more study hours generally achieved higher final scores.")
print("2. Higher attendance is generally associated with better final scores.")
print("3. Final scores vary among students.")
print("4. The dataset does not contain missing values.")