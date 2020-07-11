import os
import pandas as pd

_BASEPATH = os.path.dirname(__file__)


def _get_full_path_to_local_file(fname):
    return os.path.join(_BASEPATH, fname)


def get_full_path_to_dataset_file(fname, dataset_dir='ml-latest-small'):
    return os.path.join(_get_full_path_to_local_file(dataset_dir), fname)


def load(fname, *pd_args, **pd_kwargs):
    fullpath = get_full_path_to_dataset_file(fname)
    return pd.read_csv(fullpath, *pd_args, **pd_kwargs)
