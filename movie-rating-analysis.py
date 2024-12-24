#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
print(df)


# In[2]:


print("First few rows of the dataset:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)


# In[3]:


print("\nFirst 10 rows of the dataset:")
print(df.head(10))
df.dropna(subset=['Genre', 'Director', 'Rating'], inplace=True)
print(df)


# In[4]:


df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.year
df_genres = df['Genre'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
df_genres = pd.DataFrame(df_genres, columns=['Genre'])
df_genres['Title'] = df.loc[df_genres.index, 'Title']
df_genres['Rating'] = df.loc[df_genres.index, 'Rating']
genre_avg_rating = df_genres.groupby('Genre')['Rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
genre_avg_rating.plot(kind='bar', color='skyblue')
plt.title('Average IMDB Rating per Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.show()


# In[5]:


plt.figure(figsize=(10, 6))
df_genres.boxplot(column='Rating', by='Genre', vert=False, patch_artist=True)
plt.title('Rating Distribution by Genre')
plt.suptitle('')
plt.xlabel('Rating')
plt.show()


# In[6]:


director_avg_rating = df.groupby('Director')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
director_avg_rating.head(10).plot(kind='bar', color='salmon')
plt.title('Top 10 Directors by Average Rating')
plt.xlabel('Director')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()


# In[7]:


year_avg_rating = df.groupby('Year')['Rating'].mean()
plt.figure(figsize=(12, 6))
year_avg_rating.plot(kind='line', marker='o', color='green')
plt.title('Average IMDB Rating by Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.grid()
plt.show()


# In[ ]:




