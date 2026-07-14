"""### Why Seaborn?

- provides a layer of abstraction hence simpler to use
- better aesthetics
- more graphs included

### Seaborn Roadmap

Types of Functions

- Figure Level
- Axis Level

Main Classification

- Relational Plot
- Distribution Plot
- Categorical Plot
- Regression Plot
- Matrix Plot
- Multiplots

### 1. Relational Plot

- to see the statistical relation between 2 or more variables.
- Bivariate Analysis

Plots under this section

- scatterplot
- lineplot
"""

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips = sns.load_dataset('tips')
tips

# scatter plot -> axes level function
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='time', size='size')
plt.show()

# relplot -> figure level -> square shape
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', hue='sex', style='time', size='size')
plt.show()

# scatter using relplot -> size and hue

# style semantics

# line plot
gap = px.data.gapminder()
temp_df = gap[gap['country'] == 'India']
temp_df

# axes level function
sns.lineplot(data=temp_df, x='year', y='lifeExp')
plt.show()

# using relpplot
sns.relplot(data=temp_df, x='year', y='lifeExp', kind='line')
plt.show()

# hue -> style
temp_df = gap[gap['country'].isin(['India','Brazil','Germany'])]
temp_df

sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country', style='continent', size='continent')
plt.show()

sns.lineplot(data=temp_df, x='year', y='lifeExp', hue='country')
plt.show()

# facet plot -> figure level function -> work with relplot
# it will not work with scatterplot and lineplot
sns.relplot(data=tips, x='total_bill', y='tip', kind='line', col='sex', row='day')
plt.show()

# col wrap
sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=3)
plt.show()

# FIXED: Changed from sns.scatterplot to sns.relplot because 'col' and 'row' parameters are only supported in figure-level functions
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', col='sex', row='day')
plt.show()

"""### 2. Distribution Plots

- used for univariate analysis
- used to find out the distribution
- Range of the observation
- Central Tendency
- is the data bimodal?
- Are there outliers?

Plots under distribution plot

- histplot
- kdeplot
- rugplot
"""

# figure level -> displot
# axes level -> histplot -> kdeplot -> rugplot

# plotting univariate histogram
sns.histplot(data=tips, x='total_bill')
plt.show()

sns.displot(data=tips, x='total_bill', kind='hist')
plt.show()

# bins parameter
sns.displot(data=tips, x='total_bill', kind='hist', bins=2)
plt.show()

# It’s also possible to visualize the distribution of a categorical variable using the logic of a histogram.
# Discrete bins are automatically set for categorical variables

# countplot
sns.displot(data=tips, x='day', kind='hist')
plt.show()

# hue parameter
sns.displot(data=tips, x='tip', kind='hist', hue='sex')
plt.show()

# element -> step
sns.displot(data=tips, x='tip', kind='hist', hue='sex', element='step')
plt.show()

titanic = sns.load_dataset('titanic')
titanic

sns.displot(data=titanic, x='age', kind='hist', element='step', hue='sex')
plt.show()

# faceting using col and row -> not work on histplot function
sns.displot(data=tips, x='tip', kind='hist', col='sex', element='step')
plt.show()

# kdeplot
# Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate
sns.kdeplot(data=tips, x='total_bill')
plt.show()

sns.displot(data=tips, x='total_bill', kind='kde')
plt.show()

# hue -> fill
sns.displot(data=tips, x='total_bill', kind='kde', hue='sex', fill=True, height=10, aspect=2)
plt.show()

# Rugplot

# Plot marginal distributions by drawing ticks along the x and y axes.

# This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.
sns.kdeplot(data=tips, x='total_bill')
sns.rugplot(data=tips, x='total_bill')
plt.show()

# Bivariate histogram
# A bivariate histogram bins the data within rectangles that tile the plot
# and then shows the count of observations within each rectangle with the fill color

# sns.histplot(data=tips, x='total_bill', y='tip')
sns.displot(data=tips, x='total_bill', y='tip', kind='hist')
plt.show()

# Bivariate Kdeplot
# a bivariate KDE plot smoothes the (x, y) observations with a 2D Gaussian
sns.kdeplot(data=tips, x='total_bill', y='tip')
plt.show()

"""### 2. Matrix Plot

- Heatmap
- Clustermap
"""

# Heatmap

# Plot rectangular data as a color-encoded matrix
temp_df = gap.pivot(index='country', columns='year', values='lifeExp')

# axes level function
plt.figure(figsize=(15, 15))
sns.heatmap(temp_df)
plt.show()

# annot
temp_df = gap[gap['continent'] == 'Europe'].pivot(index='country', columns='year', values='lifeExp')

plt.figure(figsize=(15, 15))
sns.heatmap(temp_df, annot=True, linewidth=0.5, cmap='summer')
plt.show()

# linewidth

# cmap

# Clustermap

# Plot a matrix dataset as a hierarchically-clustered heatmap.

# This function requires scipy to be available.

iris = px.data.iris()
iris

sns.clustermap(iris.iloc[:, [0, 1, 2, 3]])
plt.show()