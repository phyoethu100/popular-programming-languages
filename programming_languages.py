#!/usr/bin/env python
# coding: utf-8

# ## Get the Data
# 
# Either use the provided .csv file or (optionally) get fresh (the freshest?) data from running an SQL query on StackExchange: 
# 
# Follow this link to run the query from [StackExchange](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com) to get your own .csv file
# 
# <code>
# select dateadd(month, datediff(month, 0, q.CreationDate), 0) m, TagName, count(*)
# from PostTags pt
# join Posts q on q.Id=pt.PostId
# join Tags t on t.Id=pt.TagId
# where TagName in ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi')
# and q.CreationDate < dateadd(month, datediff(month, 0, getdate()), 0)
# group by dateadd(month, datediff(month, 0, q.CreationDate), 0), TagName
# order by dateadd(month, datediff(month, 0, q.CreationDate), 0)
# </code>

# ## Import Statements

# In[67]:


import pandas as pd
import matplotlib.pyplot as plt 


# ## Data Exploration

# **Challenge**: Read the .csv file and store it in a Pandas dataframe

# In[68]:


df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)


# **Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe

# In[69]:


df.head()
df.tail()


# **Challenge:** Check how many rows and how many columns there are. 
# What are the dimensions of the dataframe?

# In[70]:


df.shape


# **Challenge**: Count the number of entries in each column of the dataframe

# In[71]:


df.count()


# **Challenge**: Calculate the total number of post per language.
# Which Programming language has had the highest total number of posts of all time?

# In[72]:


df.groupby('TAG').sum()


# Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.
# 
# **Challenge**: How many months of data exist per language? Which language had the fewest months with an entry? 
# 

# In[73]:


df.groupby('TAG').count()


# ## Data Cleaning
# 
# Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"

# In[74]:


df['DATE'][1]


# In[75]:


type(df['DATE'][1])


# In[76]:


print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))
df.DATE = pd.to_datetime(df.DATE)
df.head()


# ## Data Manipulation
# 
# 

# In[77]:


reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')


# **Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.

# In[78]:


reshaped_df.shape


# In[79]:


reshaped_df.columns


# In[80]:


reshaped_df.head()
reshaped_df.isna().values.any()


# **Challenge**: Count the number of entries per programming language. Why might the number of entries be different? 

# In[81]:


reshaped_df.count()


# In[82]:


reshaped_df.fillna(0, inplace=True)
reshaped_df = reshaped_df.fillna(0)


# In[83]:


reshaped_df.head()


# ## Data Visualisaton with with Matplotlib
# 

# **Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.

# In[84]:


plt.figure(figsize=(16,10))


# In[85]:


plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


# In[86]:


plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)


# **Challenge**: Show two line (e.g. for Java and Python) on the same chart.

# In[89]:


plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)


# # Smoothing out Time Series Data
# 
# Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html). 

# In[106]:


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


# In[111]:


reshaped_df.tail()


# In[ ]:




