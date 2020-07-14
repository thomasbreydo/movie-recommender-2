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
import surprise.dump  # noqa


def _conv_relative_to_abs_fname(relative_fname):
    return os.path.abspath(os.path.join(_BASEPATH, relative_fname))


def _get_path_to_model(user):
    return _conv_relative_to_abs_fname(
        os.path.join('models', f'{user}_model.pickle'))


def save_model(user, model):
    surprise.dump.dump(_get_path_to_model(user), algo=model)


def load_model(user):
    return surprise.dump.load(_get_path_to_model(user))[1]


def load_rated(user):
    pref = load_preferences(user)
    return pref.dropna()


def conv_to_user_item_rating_order(ratings_df):
    '''Make sure columns are in `'user item rating'` order for `surprise`'''
    return ratings_df[['userId', 'movieId', 'rating']]
