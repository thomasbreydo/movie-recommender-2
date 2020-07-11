import os
import pandas as pd

DATASETPATH = os.path.join(os.path.dirname(__file__), 'ml-latest-small')


def get_full_path_to_dataset_file(fname):
    return os.path.join(DATASETPATH, fname)


def load(fname, *pd_args, **pd_kwargs):
    fullpath = get_full_path_to_dataset_file(fname)
    return pd.read_csv(fullpath, *pd_args, **pd_kwargs)
