# Loading datasets

Add the following to the top of your file (the number of `..` traversals depends on the location of your file) 
```python
import sys
import os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'dataset'))
import movielens  # noqa
```

You can then do the following:

```python
# args, kwargs go to read_csv
df = movielens.load('ratings.csv', *args, **kwargs)
```