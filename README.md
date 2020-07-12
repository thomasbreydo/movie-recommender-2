# movie-recommender-2
This project uses Python to build customized movie recommendation systems!

# How it works
## Step 1: Manually rate movies you've seen
## Step 2: Build a personal recommender model
## Step 3: Access your top predictions

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
df = movielens.load('ratings.csv', *args, **kwargs)
```
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
df = movielens.load('ratings.csv', *args, **kwargs)
```