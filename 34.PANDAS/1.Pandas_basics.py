import numpy as np
import pandas as pd
import sys

# Pandas is used for data analysis and manipulation with labeled data.
# A Series is a one-dimensional labeled array that can hold values of any type.

# Series from lists
# A simple way to create a Series is from a Python list.

# Create a Series from a list of strings
country = ["Pakistan", "India", "USA", "Nepal", "Srilanka"]
# Output: a Series created from a list of strings.
print("--- Series from list of strings ---")
print(pd.Series(country))

# Create a Series from a list of integers
runs = [13, 24, 56, 78, 100]
runs_ser = pd.Series(runs)

# Create a Series with a custom index for each value
marks = [67, 57, 89, 100]
subjects = ["maths", "english", "science", "hindi"]

# Output: a Series with custom labels for each value.
print("\n--- Series with custom index ---")
print(pd.Series(marks, index=subjects))

# Give the Series a meaningful name
marks_ser = pd.Series(marks, index=subjects, name="Hanzala marks")
# Output: a Series with a meaningful name.
print("\n--- Named Series ---")
print(marks_ser)

# Series from dict
# A dictionary can also be used to build a Series easily.

marks_dict = {"maths": 67, "english": 57, "science": 89, "hindi": 100}
marks_series = pd.Series(marks_dict, name="Hanzala marks")
# Output: a Series created from a dictionary.
print("\n--- Series from Dict ---")
print(marks_series)

# Series attributes

# Output: useful properties of a Series such as size, dtype, and index.
print("\n--- Series Attributes ---")
print(f"Size: {marks_series.size}")
print(f"Dtype: {marks_series.dtype}")
print(f"Name: {marks_series.name}")
print(f"Is Unique (marks): {marks_series.is_unique}")
print(f"Is Unique (duplicates): {pd.Series([1, 1, 2, 3, 4, 5]).is_unique}")
print(f"Index: {marks_series.index}")
print(f"Runs Index: {runs_ser.index}")
print(f"Values: {marks_series.values}")

# Series using read_csv
# Reading data from CSV files is a common way to create Series objects.
print("\n--- Loading CSVs (and squeezing to Series) ---")
subs = pd.read_csv("subs - subs.csv").squeeze("columns")
# Output: first few rows from the subscriptions Series.
print(subs.head())

vk = pd.read_csv("kohli_ipl.csv", index_col="match_no").squeeze("columns")
# Output: first few rows from the Kohli scores Series.
print(vk.head())

movies = pd.read_csv("bollywood - bollywood.csv", index_col="movie").squeeze("columns")
# Output: first few rows from the movie Series.
print(movies.head())

# Series methods
print("\n--- Head, Tail, and Samples ---")
# Output: first few rows of the subscriptions data.
print(subs.head())
# Output: first three rows of the Kohli data.
print(vk.head(3))
# Output: last ten rows of the Kohli data.
print(vk.tail(10))
# Output: a few random rows from the movie Series.
print(movies.sample(5))

# Output: frequency of each movie value in the Series.
print("\n--- Value Counts ---")
print(movies.value_counts())

# Output: sorted values in descending order.
print("\n--- Sorting ---")
print(f"Highest value in vk: {vk.sort_values(ascending=False).iloc[0]}")
print(vk.sort_values(ascending=False))

# sort_index inplace
movies_sorted = movies.copy()
movies_sorted.sort_index(ascending=False, inplace=True)
print(movies_sorted)

vk_sorted = vk.copy()
vk_sorted.sort_values(inplace=True)
print(vk_sorted)

# Series maths methods
# Useful maths operations can be applied directly to a Series.
print("\n--- Descriptive Stats ---")
# Output: count of non-null values in the Kohli scores.
print(f"Count: {vk.count()}")
# Output: total of the subscriptions values.
print(f"Sum: {subs.sum()}")
# Output: average subscription value.
print(f"Mean: {subs.mean()}")
# Output: median score in the Kohli data.
print(f"Median: {vk.median()}")
# Output: most frequent value in the movie Series.
print(f"Mode:\n{movies.mode()}")
# Output: standard deviation for the subscriptions Series.
print(f"Std Dev: {subs.std()}")
# Output: variance of the Kohli scores.
print(f"Variance: {vk.var()}")
# Output: maximum value in the subscriptions Series.
print(f"Max: {subs.max()}")
# Output: a summary of key statistics.
print("\n--- Describe Summary ---")
print(subs.describe())

# Series indexing
print("\n--- Indexing and Slicing ---")
x = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])
print(x)

# negative indexing (using iloc to prevent index confusion)
print(f"Last element of x: {x.iloc[-1]}")
print(f"Last element of vk: {vk.iloc[-1]}")
print(f"Last element of marks_series: {marks_series.iloc[-1]}")

# slicing
print(vk.iloc[5:16])
print(vk.iloc[-5:])
print(movies.iloc[::2])

# fancy indexing
print(vk.iloc[[1, 3, 4, 5]])
print(movies["2 States (2014 film)"])

# Editing series
# Values in a Series can be updated using labels or positions.
print("\n--- Editing Series ---")
# Using .iloc for safe positional assignment
marks_series.iloc[1] = 100
# Output: the Series after replacing one value.
print(marks_series)

# Adding a completely new label
marks_series["evs"] = 100
# Output: the Series after adding a new label.
print(marks_series)

# slicing
runs_ser.iloc[2:4] = [100, 100]
# Output: the Series after changing a slice of values.
print(runs_ser)

# fancy indexing
runs_ser.iloc[[0, 3, 4]] = [0, 0, 0]
# Output: the Series after updating specific positions.
print(runs_ser)

# updating via label index
movies_edited = movies.copy()
movies_edited["2 States (2014 film)"] = "Alia Bhatt"
# Output: the updated value for a specific movie label.
print(movies_edited["2 States (2014 film)"])

# Series with Python functionalities
print("\n--- Python Built-ins on Series ---")
print(len(subs))
print(type(subs))
print(min(subs))
print(max(subs))

# Type conversion
print(list(marks_series))
print(dict(marks_series))

# Membership operators
print("2 States (2014 film)" in movies)
print("Alia Bhatt" in movies.values)

# Arithmetic Operators (Broadcasting)
print(100 + marks_series)

# Relational Operators
print(vk >= 50)

# Boolean indexing on series
# Filtering values using conditions makes data exploration easier.
print("\n--- Boolean Indexing ---")
# Output: number of scores greater than or equal to 50.
print(f"No of 50s and 100s by Kohli: {vk[vk >= 50].size}")
# Output: number of zero scores in the Kohli data.
print(f"No of Ducks by Kohli: {vk[vk == 0].size}")
# Output: number of days with more than 200 subscribers.
print(f"Days with >200 subs: {subs[subs > 200].size}")

num_movies = movies.value_counts()
print("\nActors with more than 20 movies:")
print(num_movies[num_movies > 20])

# Some important series methods
# These methods help with data cleaning and transformation.
print("\n--- Advanced Series Methods ---")

# astype
print(f"Original vk memory size: {sys.getsizeof(vk)} bytes")
print(f"Downcasted (int16) memory size: {sys.getsizeof(vk.astype('int16'))} bytes")

# between
print(f"Matches score between 51 and 99: {vk[vk.between(51, 99)].size}")

# clip
print(subs.clip(100, 200))

# drop_duplicates
temp = pd.Series([1, 1, 2, 2, 3, 3, 4, 4])
print(temp.drop_duplicates(keep="last"))
print(f"Duplicates count: {temp.duplicated().sum()}")

# Handling Nulls
temp_nulls = pd.Series([1, 2, 3, np.nan, 5, 6, np.nan, 8, np.nan, 10])
print(f"Nulls count: {temp_nulls.isnull().sum()}")
print("Dropped Nulls:")
print(temp_nulls.dropna())
print("Filled Nulls:")
print(temp_nulls.fillna(temp_nulls.mean()))

# isin
print("Kohli scores of exactly 49 or 99:")
print(vk[vk.isin([49, 99])])

# apply
print("First word of movie actor uppercase:")
print(movies.apply(lambda x: str(x).split()[0].upper()).head())

# Copy vs View safety
print("\n--- Copy vs View behavior ---")
new_view = vk.head()
# making changes to a copy to avoid SettingWithCopyWarning:
new_copy = vk.head().copy()
new_copy.iloc[0] = 100

print("New Copy (Modified):")
print(new_copy)
print("Original vk (Unchanged):")
print(vk.head())
