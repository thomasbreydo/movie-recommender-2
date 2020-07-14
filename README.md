# movie-recommender-2
This project uses `scikit-surprise` to build customized movie recommendation systems in Python!

# Usage

## Step 1: Manually rate movies you've seen

- Go to the [`rate_movies/rate_movies.ipynb`](rate_movies/rate_movies.ipynb) notebook.

- Change the `USER` variable in the top cell to your name.

- Run all of the cells in the notebook. The most important one is the last one, in which you will
rate around 200 movies. 

    - Your preferences will automatically be saved to `rate_movies/preferences/[your username]_pref.csv`.

## Step 2: Build a personal recommender model

- Go to the [`recommend/recommend.ipynb`](recommend/recommend.ipynb) notebook.

- Change the `USER` variable in the top cell to your name. (Make sure it's identical to the `USER` variable in [Step 1](#step-1-manually-rate-movies-youve-seen))

- Run all of the cells in the notebook. Your recommended movies will display. 

    - At the end of the notebook, you will also see movies for which your estimated rating differs the most from the average rating.

# Further exploring the data by yourself

## How to load parts of the dataset
I've created an interface for you to access the CSV files in the MovieLens dataset.
Add the following to the top of your file (the number of `..` traversals depends on the location of your file) 
```python
import sys
import os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'movie-recommender-2'))
import dataset  # noqa
```

You can then do the following:

```python
# args, kwargs go to read_csv
df = dataset.load('ratings.csv', *args, **kwargs)
```
