# Created with Jupyter Notebook

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

df.head()
df.tail()

df.shape

df.count()

df.groupby('TAG').sum()

df.groupby('TAG').count()

df['DATE'][1]

type(df['DATE'][1])

print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))
df.DATE = pd.to_datetime(df.DATE)
df.head()

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

reshaped_df.shape

reshaped_df.columns

reshaped_df.head()
reshaped_df.isna().values.any()

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)
reshaped_df = reshaped_df.fillna(0)

reshaped_df.head()

plt.figure(figsize=(16,10))

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Years', fontsize=16)
plt.ylabel('Number of Posts', fontsize=16)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(reshaped_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)

plt.title('Popularity of Different Programming Languages', fontsize=20)
plt.legend(fontsize=14)

reshaped_df.tail()
