print("JANASREE P 24BAD040")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\janas\\Downloads\\Housing.csv")

print(df.isnull().sum())

plt.scatter(df["area"], df["price"])
plt.show()
sns.heatmap(df.select_dtypes("number").corr(), annot=True)
plt.show()
