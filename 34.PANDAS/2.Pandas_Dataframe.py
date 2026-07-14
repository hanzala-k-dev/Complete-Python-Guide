import numpy as np
import pandas as pd

# Creating a DataFrame from different sources.

# using lists
# Output: a table with rows of student data and named columns.
student_data = [[100, 80, 10], [90, 70, 7], [120, 100, 14], [80, 50, 2]]

print(pd.DataFrame(student_data, columns=["iq", "marks", "package"]))

# using dicts
# Output: a DataFrame created from a dictionary with student details.

student_dict = {
    "name": ["Hanzala", "Saad", "Meer", "Haris", "Mursaleen", "Ateeq"],
    "iq": [100, 90, 120, 80, 0, 0],
    "marks": [80, 70, 100, 50, 0, 0],
    "package": [10, 7, 14, 2, 0, 0],
}

students = pd.DataFrame(student_dict)
students.set_index("name", inplace=True)
print(students)

# using read_csv
# Output: tables loaded from CSV files into DataFrames.
movies = pd.read_csv("movies.csv")
print(movies)

ipl = pd.read_csv("ipl-matches.csv")
print(ipl)

# Exploring DataFrame attributes and methods.

# shape
# Output: the number of rows and columns in each DataFrame.
print(movies.shape)
print(ipl.shape)

# dtypes
# Output: the data type of each column.
print(movies.dtypes)
print(ipl.dtypes)

# index
# Output: the row labels for each DataFrame.
print(movies.index)
print(ipl.index)

# columns
# Output: the column names present in each DataFrame.
print(movies.columns)
print(ipl.columns)
print(students.columns)

# values
# Output: the underlying data values as a NumPy array.
print(students.values)
print(ipl.values)

# head and tail
# Output: the first and last few rows of the data.
print(movies.head(2))

print(ipl.tail(2))

# sample
# Output: a random sample of rows from the DataFrame.
print(ipl.sample(5))

# info
# Output: a summary of the DataFrame structure and memory usage.
movies.info()

ipl.info()

# describe
# Output: basic statistics for numeric columns.
print(movies.describe())

print(ipl.describe())

# isnull
# Output: the number of missing values in each column.
print(movies.isnull().sum())

# duplicated
# Output: the number of duplicate rows found.
print(movies.duplicated().sum())

print(students.duplicated().sum())

# rename
# Output: renamed columns after the change.
print(students)

students.rename(columns={"marks": "percent", "package": "lpa"}, inplace=True)
print(students)

# Using basic math methods on DataFrame values.

# sum -> axis argument
# Output: the sum of each column or row depending on the axis.
print(students.sum(axis=0))

print(students.mean(axis=1))

print(students.var())


# Selecting columns from a DataFrame.

# single cols
# Output: a single column returned as a Series.
print(movies["title_x"])

print(ipl["Venue"])

# multiple cols
# Output: a DataFrame containing only the selected columns.
print(movies[["year_of_release", "actors", "title_x"]])

print(ipl[["Team1", "Team2", "WinningTeam"]])

# Selecting rows from a DataFrame.

# single row
# Output: one row selected by position using iloc.
print(movies.iloc[5])

# multiple row
# Output: several rows selected together by position.
print(movies.iloc[:5])

# fancy indexing
# Output: rows selected using a custom list of positions.
print(movies.iloc[[0, 4, 5]])

# loc
# Output: rows selected using index labels instead of positions.
print(students)

print(students.loc["Hanzala"])

print(students.loc["Hanzala":"Saad":2])

print(students.loc[["Hanzala", "Haris", "Meer"]])

print(students.iloc[[0, 3, 4]])

# Selecting both rows and columns together.

print(movies.iloc[0:3, 0:3])

print(movies.loc[0:2, "title_x":"poster_path"])

# Filtering rows with conditions.

print(ipl.head(2))

# find all the final winners
# Output: the season and winning team for all final matches.
mask = ipl["MatchNumber"] == "Final"
new_df = ipl[mask]
print(new_df[["Season", "WinningTeam"]])

print(ipl[ipl["MatchNumber"] == "Final"][["Season", "WinningTeam"]])

# how many super over finishes have occured
# Output: the count of matches that ended in a super over.
print(ipl[ipl["SuperOver"] == "Y"].shape[0])

# how many matches has csk won in kolkata
# Output: the number of Kolkata matches won by Chennai Super Kings.
print(
    ipl[
        (ipl["City"] == "Kolkata") & (ipl["WinningTeam"] == "Chennai Super Kings")
    ].shape[0]
)

# toss winner is match winner in percentage
# Output: the percentage of matches where the toss winner also won the match.
print((ipl[ipl["TossWinner"] == ipl["WinningTeam"]].shape[0] / ipl.shape[0]) * 100)

# movies with rating higher than 8 and votes>10000
# Output: the count of movies meeting both conditions.
print(movies[(movies["imdb_rating"] > 8.5) & (movies["imdb_votes"] > 10000)].shape[0])

# Action movies with rating higher than 7.5
# Output: all action movies that also meet the rating condition.
# mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask1 = movies["genres"].str.contains("Action")
mask2 = movies["imdb_rating"] > 7.5

print(movies[mask1 & mask2])

# write a function that can return the track record of 2 teams against each other

# Adding new columns to a DataFrame.

# completely new
# Output: the new DataFrame with an added Country column.
movies["Country"] = "India"
print(movies.head())

# from existing ones
# Output: a new column created from the first actor in the actors field.
movies.dropna(inplace=True)

movies["lead actor"] = movies["actors"].str.split("|").apply(lambda x: x[0])
print(movies.head())

movies.info()

# Important DataFrame functions for cleaning and conversion.

# astype
# Output: the updated column type after conversion.
ipl.info()

ipl["ID"] = ipl["ID"].astype("int32")

ipl.info()

# ipl['Season'] = ipl['Season'].astype('category')
ipl["Team1"] = ipl["Team1"].astype("category")
ipl["Team2"] = ipl["Team2"].astype("category")

ipl.info()


