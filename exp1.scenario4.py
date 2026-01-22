print("JANASREE P 24BAD040")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\janas\\Downloads\\marketing_campaign.csv", sep="\t")

print(df.info())
print(df.isnull().sum())

df['Age'] = 2025 - df['Year_Birth']

sns.histplot(df['Age'], bins=20)
plt.show()

sns.boxplot(x=df['Income'])
plt.show()

sns.boxplot(data=df[['MntWines','MntMeatProducts','MntGoldProds']])
plt.show()
