import pandas as pd


def load_complete_dataset(path_to_complete_dataset: str):
    data = pd.read_csv(path_to_complete_dataset)
    return data


def get_trainig_length(data: pd.DataFrame):
    total_length = len(data)
    training_proportion = 0.8
    trainig_length = round(total_length * training_proportion)
    return trainig_length


def get_testing_length(data: pd.DataFrame):
    total_length = len(data)
    training_length = get_trainig_length(data)
    testing_length = total_length - training_length
    return testing_length
