from tqdm import tqdm
import numpy as np
import pandas as pd
import movieposters
import sys
import os

_BASEPATH = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(_BASEPATH, '..', '..'))
import dataset  # noqa


def _get_full_path(relative_path):
    return os.path.join(_BASEPATH, relative_path)


def get_finished_movie_ids(relative_path='poster_links.csv'):
    fullpath = _get_full_path(relative_path)
    return pd.read_csv(fullpath, index_col=['movieId'],
                       usecols=['movieId', 'poster'])


def _only_unfinished(ids):
    try:
        return ids[~ids.index.isin(get_finished_movie_ids().index)]
    except FileNotFoundError:
        return ids


def save_poster_links(posters, savepath='poster_links.csv'):
    write_a_header = not os.path.exists(savepath)
    posters.to_csv(savepath, mode='a', header=write_a_header)


def download_poster_links(save_every=20, pbar=True):
    ids = dataset.load('links.csv', usecols=[
        'movieId', 'imdbId'], index_col='movieId')
    ids = _only_unfinished(ids)
    posters = pd.DataFrame()
    posters.index.name = 'movieId'

    iterator = enumerate(ids.iterrows())
    if pbar:
        iterator = tqdm(iterator, total=len(ids.index))

    for i, row in iterator:
        movieId, (imdbId,) = row
        try:
            link = movieposters.get_poster(id=imdbId)
        except (movieposters.MovieNotFound, movieposters.PosterNotFound):
            link = np.nan
        posters.at[movieId, 'poster'] = link
        if (i + 1) % save_every == 0:
            save_poster_links(posters)
            # once saved, not clearing the df will result in dupes saved later
            posters = posters.iloc[0:0]


def main():
    download_poster_links()


if __name__ == "__main__":
    main()
