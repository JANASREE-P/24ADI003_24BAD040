print("JANASREE P 24BAD040")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\janas\\Downloads\\diabetes (1).csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[cols] = df[cols].replace(0, pd.NA)

print(df.isnull().sum())

plt.hist(df["Glucose"].dropna(), bins=20)
plt.show()

plt.boxplot(df["Age"])
plt.show()
