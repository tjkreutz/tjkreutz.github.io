---
thumbnail: '/img/thumbnails/thumbnail-8.png'
keywords: ['td', 'th', 'tr', 'plt', 'read']
layout: post
date: 2026-01-08 20:00:00 +0100
title: "Visualising my Goodreads data"
---

# Visualising my Goodreads data

I had to push quite hard to reach my Goodreads reading goal for 2025. I finished Circe by Madeline Miller, my 40th book 
of the year, on the 27th of December. You can download your personal Goodreads data in 
[your profile](https://www.goodreads.com/review/import). Let's analyze mine.

## Inspection

Install pandas.

```python
%pip install pandas
```

Load the data.

```python
import pandas as pd

goodreads_data = pd.read_csv("goodreads_library_export.csv", parse_dates=["Date Added", "Date Read"])
```

Show information about "Circe".

```python
circe_info = goodreads_data[goodreads_data["Title"] == "Circe"]
info_subset = ["Title", "Author", "My Rating", "Date Added", "Date Read"]
circe_info[info_subset]

```
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Author</th>
      <th>My Rating</th>
      <th>Date Added</th>
      <th>Date Read</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Circe</td>
      <td>Madeline Miller</td>
      <td>3</td>
      <td>2025-12-22</td>
      <td>2025-12-27</td>
    </tr>
  </tbody>
</table>
</div>

See how many books I've read in total.

```python
goodreads_data['Exclusive Shelf'].value_counts()
```

    Exclusive Shelf
    read                 349
    to-read                6
    currently-reading      1
    Name: count, dtype: int64

See how many books I've read in 2025.

```python
books_read = goodreads_data[goodreads_data["Exclusive Shelf"] == "read"]
book_read_2025 =books_read[books_read["Date Read"].dt.year == 2025]
len(book_read_2025.index)
```

    40

## Visualising reading behaviour

Install matplotlib. Import numpy and matplotlib

```python
%pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
```

Show how many books per year I've read and the linear trend.

```python
books_per_year = (
    books_read.groupby(books_read["Date Read"].dt.year)
    .size()
)
# Fill missing years with 0
books_per_year = books_per_year.reindex(range(int(books_per_year.index.min()), int(books_per_year.index.max()) + 1), fill_value=0)

# fit a linear trend
books_per_year_z = np.polyfit(books_per_year.index, books_per_year.values, 1)
books_per_year_p = np.poly1d(books_per_year_z)

plt.figure(figsize=(6, 3))
plt.plot(books_per_year.index, books_per_year.values, marker="o")
plt.plot(books_per_year.index, books_per_year_p(books_per_year.index), "r--", alpha=0.8, label="Trend")

plt.title("Books read per year")
plt.xlabel("Year")
plt.ylabel("Books read")
plt.xticks(books_per_year.index, rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

![Books read per year]({{ "/img/goodreads-1.png" | prepend: site.baseurl }})
    
Nice! Looks like the number of books I read per year is trending upwards. Critical thinking: does reading more books automatically mean that I read more words? Maybe it's more fair to plot the number of pages per year.

```python
pages_per_year = (
    books_read.groupby(books_read["Date Read"].dt.year)["Number of Pages"]
    .sum(min_count=1)
    .sort_index()
)

# fill missing years with 0
pages_per_year = pages_per_year.reindex(range(int(pages_per_year.index.min()), int(pages_per_year.index.max()) + 1), fill_value=0)

pages_per_year_z = np.polyfit(pages_per_year.index, pages_per_year.values, 1)
pages_per_year_p = np.poly1d(pages_per_year_z)

plt.figure(figsize=(6, 3))
plt.plot(pages_per_year.index, pages_per_year.values, marker="o")
plt.plot(pages_per_year.index, pages_per_year_p(pages_per_year.index), "r--", alpha=0.8, label="Trend")
plt.title("Pages read per year")
plt.xlabel("Year")
plt.ylabel("Pages read")
plt.xticks(pages_per_year.index, rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```
 
![Pages reads per year]({{ "/img/goodreads-2.png" | prepend: site.baseurl }})

```python
book_slope, pages_slope = books_per_year_z[0], pages_per_year_z[0]
book_mean, pages_mean = books_per_year.mean(), pages_per_year.mean()
book_normalized_slope, pages_normalized_slope = book_slope / book_mean, pages_slope / pages_mean

print(f"Books slope: {book_slope:.2f} books/year")
print(f"Pages slope: {pages_slope:.2f} pages/year")
print(f"Books normalized slope: {book_normalized_slope:.4f} (books/year/mean)")
print(f"Pages normalized slope: {pages_normalized_slope:.4f} (pages/year/mean)")
```
    Books slope: 3.18 books/year
    Pages slope: 1005.24 pages/year
    Books normalized slope: 0.1477 (books/year/mean)
    Pages normalized slope: 0.1249 (pages/year/mean)

The number of read books increases by 3.18 on average per year. The number of read pages increases by 1005.24 on average per year. The number of books increases more on average (14.77% of mean) than the number of pages (12.49% of mean). I can confirm this anecdotally, since having a Goodreads goal has caused me to pick
up a few shorter reads in more recent years. 

For our final visualisation let's see which reading goals were met. This data is not present in the library export, but
I can add it here by hand:

```python
from io import StringIO

reading_goals_raw = """
Year:Goal
2012:0
2013:0
2014:0
2015:0
2016:0
2017:20
2018:25
2019:25
2020:25
2021:25
2022:35
2023:40
2024:40
2025:40
2026:40
"""
reading_goals = pd.read_csv(StringIO(reading_goals_raw), sep=":")
reading_goals
```
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Goal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017</td>
      <td>20</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018</td>
      <td>25</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019</td>
      <td>25</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2020</td>
      <td>25</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021</td>
      <td>25</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2022</td>
      <td>35</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2023</td>
      <td>40</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024</td>
      <td>40</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2025</td>
      <td>40</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2026</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>

I had reading goals defined since 2017. I'll set the reading goal in preceding years to 0.

```python
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

reading_goals["Books Read"] = reading_goals["Year"].map(books_per_year).fillna(0).astype(int)
reading_goals["Goal Met"] = reading_goals["Books Read"] >= reading_goals["Goal"]
colors = np.where(reading_goals["Goal Met"], "tab:green", "tab:red")

plt.figure(figsize=(6, 3))
plt.bar(reading_goals["Year"], reading_goals["Books Read"], color=colors, alpha=0.85)
plt.plot(reading_goals["Year"], reading_goals["Goal"], color="black", linestyle="--", marker="o")

legend_handles = [
    Patch(facecolor="tab:green", edgecolor="none", label="Goal met"),
    Patch(facecolor="tab:red", edgecolor="none", label="Goal not met"),
    Line2D([0], [0], color="black", linestyle="--", marker="o", label="Goal"),
]
plt.legend(handles=legend_handles)

plt.title("Reading goals vs books read")
plt.xlabel("Year")
plt.ylabel("Books")
plt.xticks(reading_goals["Year"], rotation=45)
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

![Reading goals vs books read]({{ "/img/goodreads-3.png" | prepend: site.baseurl }})

Analysing my own "goal-picking" behaviour, it looks like I've increased my target almost every year after I hit a target. The exceptions are 2012-2016, during which I wasn't actually using Goodreads yet, so this is more of an administrative issue than a reading issue, and this year (2026), because I only just made it to 40 books, and I actively sought out a couple of shorter books to get there.
