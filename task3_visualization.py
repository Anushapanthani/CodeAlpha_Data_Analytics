import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# Chart 1
plt.figure(figsize=(7, 5))
plt.scatter(df["Study_Hours"], df["Final_Score"])
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.grid(True)
plt.savefig("chart1_study_hours.png")
plt.close()

# Chart 2
plt.figure(figsize=(7, 5))
plt.scatter(df["Attendance"], df["Final_Score"])
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.grid(True)
plt.savefig("chart2_attendance.png")
plt.close()

# Chart 3
gender = df.groupby("Gender")["Final_Score"].mean()

plt.figure(figsize=(7, 5))
plt.bar(gender.index, gender.values)
plt.title("Average Final Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Final Score")
plt.savefig("chart3_gender.png")
plt.close()

# Chart 4
plt.figure(figsize=(7, 5))
plt.hist(df["Final_Score"], bins=6, edgecolor="black")
plt.title("Final Score Distribution")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.savefig("chart4_distribution.png")
plt.close()

print("All 4 charts created successfully!")