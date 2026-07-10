# Comparing Movie Genres 

A data analysis project that compares my favorite movie — **Harry Potter and the Chamber of Secrets** — to other Science Fiction & Fantasy movies using Rotten Tomatoes data. Built as part of a Girls Who Code "Talking Data" activity.

## What It Does

The program walks through a full mini data analysis, step by step:

1. **Loads the data** — reads a Rotten Tomatoes movie dataset with pandas.
2. **Investigates the data** — prints out the movie titles in the dataset.
3. **Filters the data** — finds my favorite movie's row and builds a subset of all movies in the **Science Fiction & Fantasy** genre.
4. **Describes the data** — calculates the min, max, mean, and median audience ratings for the genre and explains how my favorite movie compares.
5. **Visualizes the data** — displays two charts with matplotlib:
   - A **histogram** of audience ratings for Science Fiction & Fantasy movies
   - A **scatter plot** of audience rating vs. critic rating, showing a positive correlation between the two

The program is interactive — press **Enter** at each prompt to move on to the next section.

## Files

| File | Description |
| --- | --- |
| `main.py` | The analysis program |
| `Rotten Tomatoes Movie Data Spreadsheet - rotten_tomatoes_movies.csv` | The Rotten Tomatoes movie dataset |

> **Note:** `main.py` reads the dataset as `rotten_tomatoes_movies.csv`. If the CSV still has its longer download name, rename it to `rotten_tomatoes_movies.csv` first.

## Requirements

- Python 3
- pandas
- matplotlib

Install the libraries with:

```bash
pip install pandas matplotlib
```

## How to Run

```bash
python main.py
```

Follow the prompts in the terminal, and close each chart window to continue to the next one.

## Key Findings

- There are hundreds of Science Fiction & Fantasy movies in the dataset.
- Harry Potter and the Chamber of Secrets is rated **above both the mean and median** audience rating for its genre — 72 points above the lowest-rated movie and only 20 points below the highest.
- Most movies in the genre have medium-to-high audience ratings.
- Audience ratings and critic ratings show a **positive correlation** — movies audiences love, critics tend to like too (with a few outliers).
