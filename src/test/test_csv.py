import pandas as pd 


ratings = pd.read_csv("../data/rating.csv")
g_scores = pd.read_csv("../data/genome_scores.csv")
g_tags = pd.read_csv("../data/genome_tags.csv")
links = pd.read_csv("../data/link.csv")
movies = pd.read_csv("../data/movie.csv")
tags = pd.read_csv("../data/tag.csv")

print(ratings.head(3))
print(g_scores.head())
print(g_tags.head())
print(links.head())
print(movies.head())
print(tags.head())