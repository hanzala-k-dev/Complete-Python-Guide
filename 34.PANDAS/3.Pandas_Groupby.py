import pandas as pd
import numpy as np

# This section shows how groupby helps split data into categories and summarize it.
movies = pd.read_csv("imdb-top-1000.csv")

# Output: first few rows of the dataset
print(movies.head())

genres = movies.groupby("Genre")

# Applying builtin aggregation functions on groupby objects.
# FIXED: Passed numeric_only=True to prevent calculating std on string columns.
# Output: standard deviation for numeric columns within each genre.
print(genres.std(numeric_only=True))

# Find the top 3 genres by total earning.
# FIXED: Passed numeric_only=True to .sum()
# Output: genres with the highest total gross income.
print(movies.groupby("Genre").sum(numeric_only=True)["Gross"].sort_values(ascending=False).head(3))

# Output: total gross earnings for each genre in descending order.
print(movies.groupby("Genre")["Gross"].sum().sort_values(ascending=False).head(3))

# Find the genre with the highest average IMDB rating.
# Output: the genre with the best average rating.
print(
    movies.groupby("Genre")["IMDB_Rating"].mean().sort_values(ascending=False).head(1)
)

# Find the director with the most popularity based on total votes.
# Output: the director with the highest total vote count.
print(
    movies.groupby("Director")["No_of_Votes"].sum().sort_values(ascending=False).head(1)
)

# Find the highest rated movie of each genre.
# Output: one movie per genre with the maximum rating.
# movies.groupby('Genre')['IMDB_Rating'].max()

# Find the number of movies done by each actor.
# Output: count of movies for each actor.
# movies['Star1'].value_counts()

# Output: number of movies by each leading actor.
print(movies.groupby("Star1")["Series_Title"].count().sort_values(ascending=False))

# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

# Output: total number of genre groups.
print(len(movies.groupby("Genre")))

# Output: number of unique genres.
print(movies["Genre"].nunique())

# Output: size of each genre group.
print(movies.groupby("Genre").size())

genres = movies.groupby("Genre")
# genres.first()
# genres.last()
# Output: the 7th row from each group.
print(genres.nth(6))

# Output: frequency of each genre in the dataset.
print(movies["Genre"].value_counts())

# Output: all rows belonging to the Fantasy genre.
print(genres.get_group("Fantasy"))

# Output: same result using filtering instead of get_group.
print(movies[movies["Genre"] == "Fantasy"])

# Output: dictionary showing group names and their row indexes.
print(genres.groups)

# Output: summary statistics for each genre group.
print(genres.describe())

# Output: two random rows from each group.
print(genres.sample(2, replace=True))

# Output: number of distinct values in each column for each group.
print(genres.nunique())

# agg method
# passing dict
# Output: aggregated values using different functions for different columns.
print(
    genres.agg(
        {
            "Runtime": "mean",
            "IMDB_Rating": "mean",
            "No_of_Votes": "sum",
            "Gross": "sum",
            "Metascore": "min",
        }
    )
)

# passing list
# FIXED: Explicitly selected only numeric columns before applying aggregate list.
# Output: multiple aggregate functions applied to each column.
numeric_cols = movies.select_dtypes(include=[np.number]).columns
print(movies.groupby("Genre")[numeric_cols].agg(["min", "max", "mean", "sum"]))

# Adding both the syntax
# Output: a mix of column-wise and function-wise aggregation.
print(
    genres.agg(
        {
            "Runtime": ["min", "mean"],
            "IMDB_Rating": "mean",
            "No_of_Votes": ["sum", "max"],
            "Gross": "sum",
            "Metascore": "min",
        }
    )
)

# looping on groups
# Output: one row per genre showing the movie with the highest rating.
# FIXED: Replaced .append() with list accumulation and pd.concat()
temp_list = []
for group, data in genres:
    temp_list.append(data[data["IMDB_Rating"] == data["IMDB_Rating"].max()])
df = pd.concat(temp_list, ignore_index=True)

print(df)

# split (apply) combine
# apply -> builtin function
# FIXED: Applied numeric selection to prevent using min() on string structures.
print(movies.groupby("Genre")[numeric_cols].apply(min))


# Find number of movies starting with A for each group.
# Output: count of movie titles starting with A in each genre.
def foo(group):
    return group["Series_Title"].str.startswith("A").sum()


print(genres.apply(foo))


# Find ranking of each movie in the group according to IMDB score.
# Output: a new column with rank inside each genre group.
def rank_movie(group):
    group["genre_rank"] = group["IMDB_Rating"].rank(ascending=False)
    return group


print(genres.apply(rank_movie))


# Find normalized IMDB rating group wise.
# Output: a normalized rating column for each group.
def normal(group):
    group["norm_rating"] = (group["IMDB_Rating"] - group["IMDB_Rating"].min()) / (
        group["IMDB_Rating"].max() - group["IMDB_Rating"].min()
    )
    return group


print(genres.apply(normal))

# groupby on multiple cols
# Output: grouping by both director and actor.
duo = movies.groupby(["Director", "Star1"])
print(duo)
# size
# Output: size of each director-actor group.
print(duo.size())
# get_group
# Output: all rows for the chosen director and actor pair.
print(duo.get_group(("Aamir Khan", "Amole Gupte")))

# Find the most earning actor->director combo.
# Output: the highest earning pair.
print(duo["Gross"].sum().sort_values(ascending=False).head(1))

# Find the best actor->genre combo in terms of average metascore.
# Output: the highest average metascore combination.
print(
    movies.groupby(["Star1", "Genre"])["Metascore"]
    .mean()
    .reset_index()
    .sort_values("Metascore", ascending=False)
    .head(1)
)

# agg on multiple groupby
# FIXED: Explicitly grouped only numeric columns to handle min/max/mean without exceptions.
print(movies.groupby(["Director", "Star1"])[numeric_cols].agg(["min", "max", "mean"]))

"""### Excercise"""

ipl = pd.read_csv("deliveries.csv")
# Output: first few rows of the IPL deliveries data.
print(ipl.head())

# Output: shape of the deliveries dataset.
print(ipl.shape)

# Find the top 10 batsman in terms of runs.
# Output: top 10 batsmen by total runs scored.
print(
    ipl.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False).head(10)
)

# Find the batsman with max no of sixes.
# Output: the batsman with the highest number of sixes.
six = ipl[ipl["batsman_runs"] == 6]

print(
    six.groupby("batsman")["batsman"]
    .count()
    .sort_values(ascending=False)
    .head(1)
    .index[0]
)

# Find batsman with most number of 4's and 6's in last 5 overs.
# Output: the batsman with the highest count of boundaries in the last overs.
temp_df = ipl[ipl["over"] > 15]
temp_df = temp_df[(temp_df["batsman_runs"] == 4) | (temp_df["batsman_runs"] == 6)]
print(
    temp_df.groupby("batsman")["batsman"]
    .count()
    .sort_values(ascending=False)
    .head(1)
    .index[0]
)

# Find V Kohli's record against all teams.
# Output: runs scored by Kohli against each bowling team.
temp_df = ipl[ipl["batsman"] == "V Kohli"]

print(temp_df.groupby("bowling_team")["batsman_runs"].sum().reset_index())

# Create a function that can return the highest score of any batsman.
# Output: highest single-match score for the given batsman.
temp_df = ipl[ipl["batsman"] == "V Kohli"]
print(
    temp_df.groupby("match_id")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(1)
    .values[0]
)


def highest(batsman):
    temp_df = ipl[ipl["batsman"] == batsman]
    return (
        temp_df.groupby("match_id")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
        .values[0]
    )


print(highest("DA Warner"))