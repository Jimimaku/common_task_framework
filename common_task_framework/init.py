from os import path
from pathlib import Path
import numpy as np
import pandas as pd


def load_complete_dataset(path_to_complete_dataset: str):
    data = pd.read_csv(path_to_complete_dataset)
    return data


def get_training_length(data: pd.DataFrame):
    total_length = len(data)
    training_proportion = 0.8
    training_length = round(total_length * training_proportion)
    return training_length


def get_testing_length(data: pd.DataFrame):
    total_length = len(data)
    training_length = get_training_length(data)
    testing_length = total_length - training_length
    return testing_length


def get_training_dataset(data: pd.DataFrame):
    training_length = get_training_length(data)
    train = data.head(training_length)
    return train


def get_testing_dataset(data: pd.DataFrame):
    testing_length = get_testing_length(data)
    test = data.iloc[-testing_length:, data.columns != "target"]
    return test


def get_example_submission(data: pd.DataFrame):
    testing_length = get_testing_length(data)
    example_submission = data.iloc[-testing_length:, data.columns == "id"]
    example_submission["target"] = np.random.rand(testing_length)
    return example_submission


def get_behind_the_wall_solution(data: pd.DataFrame):
    testing_length = get_testing_length(data)
    solution = data[["id", "target"]].tail(testing_length)
    return solution


def get_training_path(path_to_complete_dataset: str):
    directory = str(Path(path_to_complete_dataset).parents[0])
    training_path = path.join(directory, "train.csv")
    return training_path


def get_testing_path(path_to_complete_dataset: str):
    directory = str(Path(path_to_complete_dataset).parents[0])
    testing_path = path.join(directory, "test.csv")
    return testing_path


def get_example_submission_path(path_to_complete_dataset: str):
    directory = str(Path(path_to_complete_dataset).parents[0])
    example_submission_path = path.join(directory, "example_submission.csv")
    return example_submission_path


def save_training_dataset(data: pd.DataFrame, path_to_complete_dataset: str):
    training_dataset = get_training_dataset(data)
    path_to_training = get_training_path(path_to_complete_dataset)
    training_dataset.to_csv(path_to_training, index=False)


def save_testing_dataset(data: pd.DataFrame, path_to_complete_dataset: str):
    testing_dataset = get_testing_dataset(data)
    path_to_testing = get_testing_path(path_to_complete_dataset)
    testing_dataset.to_csv(path_to_testing, index=False)


def save_example_submission(data: pd.DataFrame, path_to_complete_dataset: str):
    example_submission = get_example_submission(data)
    path_to_example_submission = get_example_submission_path(path_to_complete_dataset)
    example_submission.to_csv(path_to_example_submission, index=False)


def init(path_to_complete_dataset: str):
    data = load_complete_dataset(path_to_complete_dataset)
    save_training_dataset(data, path_to_complete_dataset)
    save_testing_dataset(data, path_to_complete_dataset)
    save_example_submission(data, path_to_complete_dataset)
