"""Basic Matplotlib examples for beginners."""

# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use the default style so the plots look clean and simple.
# Output: the plots will appear with a clean default look.
plt.style.use("default")

# Description: this section shows how to create and customize line plots.
# Output: each example will display a chart and print useful values in the console.

# # plotting a simple function
# # Description: a line plot shows how values change over time.
# # Output: the values will be printed first, and then a line chart will appear.
price = [48000, 54000, 57000, 49000, 47000, 45000]
year = [2015, 2016, 2017, 2018, 2019, 2020]
print("Year values:", year, "Price values:", price)

plt.plot(year, price)
plt.show()

# from a pandas dataframe
# Description: this reads data from a CSV file and plots one column against another.
# Output: the first rows of the DataFrame will be printed in the console.
batsman = pd.read_csv("sharma-kohli.csv")
print("DataFrame preview:\n", batsman.head())

plt.plot(batsman["index"], batsman["V Kohli"])
plt.show()

# plotting multiple plots
# Two lines on the same chart help compare two data series.
plt.plot(batsman["index"], batsman["V Kohli"])
plt.plot(batsman["index"], batsman["RG Sharma"])
plt.show()

# labels title
# These lines add labels so the chart is easier to understand.
plt.plot(batsman["index"], batsman["V Kohli"])
plt.plot(batsman["index"], batsman["RG Sharma"])

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.show()

# colors(hex) and line(width and style) and marker(size)
plt.plot(batsman["index"], batsman["V Kohli"], color="#D9F10F")
plt.plot(batsman["index"], batsman["RG Sharma"], color="#FC00D6")

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.show()

plt.plot(batsman["index"], batsman["V Kohli"], color="#D9F10F", linestyle="solid", linewidth=3)

plt.plot(batsman["index"], batsman["RG Sharma"], color="#FC00D6", linestyle="dashdot", linewidth=2)

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.show()

plt.plot(batsman["index"], batsman["V Kohli"], color="#D9F10F", linestyle="solid", linewidth=3, marker="D", markersize=10)

plt.plot(batsman["index"], batsman["RG Sharma"], color="#FC00D6", linestyle="dashdot", linewidth=2, marker="o")

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.show()

# legend -> location
# A legend explains which line belongs to which player.
plt.plot(batsman["index"], batsman["V Kohli"], color="#D9F10F", linestyle="solid", linewidth=3, marker="D", markersize=10, label="Virat")

plt.plot(batsman["index"], batsman["RG Sharma"], color="#FC00D6", linestyle="dashdot", linewidth=2, marker="o", label="Rohit")

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")

plt.legend(loc="upper right")
plt.show()

# limiting axes
price = [48000, 54000, 57000, 49000, 47000, 45000, 4500000]
year = [2015, 2016, 2017, 2018, 2019, 2020, 2021]

plt.plot(year, price)
plt.ylim(0, 75000)
plt.xlim(2017, 2019)
plt.show()

# grid
plt.plot(batsman["index"], batsman["V Kohli"], color="#D9F10F", linestyle="solid", linewidth=3, marker="D", markersize=10)

plt.plot(batsman["index"], batsman["RG Sharma"], color="#FC00D6", linestyle="dashdot", linewidth=2, marker="o")

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")

plt.grid()
plt.show()

# show
plt.plot(batsman["index"], batsman["V Kohli"], color="#D9F10F", linestyle="solid", linewidth=3, marker="D", markersize=10)

plt.plot(batsman["index"], batsman["RG Sharma"], color="#FC00D6", linestyle="dashdot", linewidth=2, marker="o")

plt.title("Rohit Sharma Vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")

plt.grid()

plt.show()

"""# Scatter Plots
- Bivariate Analysis
- numerical vs numerical
- Use case - Finding correlation
"""

# Description: this section demonstrates how scatter plots show relationships between two variables.
# Output: the sample values are printed and then the scatter chart is displayed.

# plt.scatter simple function
# Description: scatter plots help show the relationship between two numeric values.
# Output: sample values will be printed before the scatter plot appears.
x = np.linspace(-10, 10, 50)

y = 10 * x + 3 + np.random.randint(0, 300, 50)
print("Sample x values:", x[:5], "Sample y values:", y[:5])

plt.scatter(x, y)
plt.show()

# plt.scatter on pandas data
df = pd.read_csv("batter.csv")
df = df.head(50)
df

plt.scatter(df["avg"], df["strike_rate"], color="red", marker="+")
plt.title("Avg and SR analysis of Top 50 Batsman")
plt.xlabel("Average")
plt.ylabel("SR")
plt.show()

# marker

# size
tips = sns.load_dataset("tips")


# slower
plt.scatter(tips["total_bill"], tips["tip"], s=tips["size"] * 20)
plt.show()

# scatterplot using plt.plot
# faster
plt.plot(tips["total_bill"], tips["tip"], "o")
plt.show()

# plt.plot vs plt.scatter

"""### Bar chart
- Bivariate Analysis
- Numerical vs Categorical
- Use case - Aggregate analysis of groups
"""

# Description: this section shows how bar charts are used to compare categories.
# Output: the chart will be displayed after the values are printed.

# simple bar chart
# Description: bar charts compare values across categories using rectangular bars.
# Output: the category names and values will be printed before the chart is shown.
children = [10, 20, 40, 10, 30]
colors = ["red", "blue", "green", "yellow", "pink"]
print("Bar categories:", colors, "Bar values:", children)

plt.bar(colors, children, color="black")
plt.show()

# bar chart using data

# horizontal bar chart
plt.barh(colors, children, color="black")
plt.show()

# color and label
df = pd.read_csv("batsman_season_record.csv")
df

plt.bar(np.arange(df.shape[0]) - 0.2, df["2015"], width=0.2, color="yellow")
plt.bar(np.arange(df.shape[0]), df["2016"], width=0.2, color="red")
plt.bar(np.arange(df.shape[0]) + 0.2, df["2017"], width=0.2, color="blue")

plt.xticks(np.arange(df.shape[0]), df["batsman"])

plt.show()

np.arange(df.shape[0])

# Multiple Bar charts

# xticks

# a problem
children = [10, 20, 40, 10, 30]
colors = [
    "red red red red red red",
    "blue blue blue blue",
    "green green green green green",
    "yellow yellow yellow yellow ",
    "pink pinkpinkpink",
]

plt.bar(colors, children, color="black")
plt.xticks(rotation="vertical")
plt.show()

# Stacked Bar chart
plt.bar(df["batsman"], df["2017"], label="2017")
plt.bar(df["batsman"], df["2016"], bottom=df["2017"], label="2016")
plt.bar(df["batsman"], df["2015"], bottom=(df["2016"] + df["2017"]), label="2015")

plt.legend()
plt.show()

"""### Histogram
- Univariate Analysis
- Numerical col
- Use case - Frequency Count
"""

# Description: this section explains how histograms show the distribution of values.
# Output: the histogram will be displayed after the sample data is printed.

# simple data
# Description: a histogram shows how often values fall into different ranges.
# Output: the data values will be printed and then a histogram will appear.
data = [32, 45, 56, 10, 15, 27, 61]
print("Histogram values:", data)

plt.hist(data, bins=[10, 25, 40, 55, 70])
plt.show()

# on some data
df = pd.read_csv("vk.csv")
df

plt.hist(
    df["batsman_runs"], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
)
plt.show()

# handling bins

# logarithmic scale
arr = np.load("big-array.npy")
plt.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70], log=True)
plt.show()

"""### Pie Chart
- Univariate/Bivariate Analysis
- Categorical vs numerical
- Use case - To find contribution on a standard scale
"""

# Description: this section demonstrates how pie charts represent parts of a whole.
# Output: the chart will be displayed after the labels and values are printed.

# simple data
# Description: a pie chart shows the share of each category in a whole.
# Output: the values and labels will be printed before the pie chart is shown.
data = [23, 45, 100, 20, 49]
subjects = ["eng", "science", "maths", "sst", "hindi"]
print("Pie chart values:", data, "Pie chart labels:", subjects)
plt.pie(data, labels=subjects)

plt.show()

# dataset
df = pd.read_csv("gayle-175.csv")
df

plt.pie(df["batsman_runs"], labels=df["batsman"], autopct="%0.1f%%")
plt.show()

# percentage and colors
plt.pie(
    df["batsman_runs"],
    labels=df["batsman"],
    autopct="%0.1f%%",
    colors=["blue", "green", "yellow", "pink", "cyan", "brown"],
)
plt.show()

# explode shadow
plt.pie(df["batsman_runs"], labels=df["batsman"], autopct="%0.1f%%", explode=[0.3, 0, 0, 0, 0, 0.1], shadow=True)

plt.show()

"""### Changing styles"""

plt.style.available

plt.style.use("dark_background")

arr = np.load("big-array.npy")
plt.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70], log=True)
plt.show()

"""### Save figure"""

arr = np.load("big-array.npy")
plt.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70], log=True)

plt.savefig("sample.png")
plt.show()