'''YOU ARE IN THE WRONG PLACE. THIS FILE EXISTS JUST TO PROVIDE 
recommend.ipynb SOME OTHERWISE INACCESSIBLE FUNCTIONS.'''

import random
import sys
import os
_BASEPATH = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(
    _BASEPATH, '..', '..', 'movie-recommender-2'))
import dataset  # noqa
import posters  # noqa
from rate_movies import load_preferences  # noqa


def load_rated(user):
    pref = load_preferences(user)
    return pref.dropna()
