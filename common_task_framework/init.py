import pandas as pd


def load_dataset(path_to_complete_dataset: str):
    data = pd.read_csv(path_to_complete_dataset)
    return data


def get_trainig_length(data: pd.DataFrame):
    total_length = len(data)
    trainig_length = round(total_length * 0.8)
    return trainig_length


def get_testing_length(data: pd.DataFrame):
    total_length = len(data)
    testing_length = total_length - get_trainig_length(data)
    return testing_length
