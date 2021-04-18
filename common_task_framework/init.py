import pandas as pd


def init(path_to_complete_dataset: str):
    data = pd.read_csv(path_to_complete_dataset)
    return data
