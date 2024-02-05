# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:14:46 2024

@author: princ
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("movie_dataset.csv")

print(df)

df.columns = df.columns.str.replace(" ","")
df.dropna(thresh=5,axis=0)
df = df.reset_index(drop=True)

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
print(df.describe())
print(df['Rating'].max())

# order = df['Title'].sort_values()
# Question 1
highest_rated = df[df['Rating'].max()==df['Rating']]
print(f'The highest rated movie is {highest_rated}')

# Question 2
average_revenue = df['Revenue(Millions)'].mean()
print(average_revenue)

# Question 3
average_revenue =  df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
avg_rev = average_revenue['Revenue(Millions)'].mean()
print(avg_rev)

# Question 4
movies_released = df[df['Year']==2016].shape[0]
print(movies_released)

# Question 5
movies_directed_chris = len(df[df['Director']== 'Christopher Nolan'])
print(movies_directed_chris)

# Question 6
ratings_movie = len(df[df['Rating'] >= 8.0])
print(ratings_movie)

# Question 7
median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
print(median_rating)

# Question 8
year_rating = df.groupby('Year')['Rating'].mean().sort_values(ascending=False)
print(year_rating)

# Question 9
perc_incr = ((df[df['Year'] == 2016].shape[0] - df[df['Year'] == 2006].shape[0] / df[df['Year'] == 2006].shape[0]) * 100)
print(perc_incr)

# Question 10
actors = df['Actors'].str.split(', ').explode()
act_counts = actors.value_counts()
most_com_act = act_counts.idxmax()
print(most_com_act)

# Question 11
genres = df['Genre'].str.split(', ').explode()
uniq_gen = genres.nunique()
print(uniq_gen)

df.to_csv("clean_data/movie_data_cleaned.csv")


# Question 12
correlation_matrix = df[['Year', 'Runtime(Minutes)', 'Rating', 'Votes', 'Revenue(Millions)', 'Metascore']].corr()

correlation_matrix

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Movie Dataset')
plt.show()













