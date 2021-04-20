from os import path
from pathlib import Path
import glob
import numpy as np
import pandas as pd


def load_submission(path_to_submission):
    submission = pd.read_csv(path_to_submission, index_col="id")
    return submission


def get_submission_list(path_to_submission_directory):
    submission_list_path = path.join(path_to_submission_directory, "*_submission.csv")
    submission_list = glob.glob(submission_list_path)
    return submission_list


class Referee:
    def __init__(self, path_to_complete_dataset: str):
        self.path_to_complete_dataset = path_to_complete_dataset
        self.data = self.load_complete_dataset()

    def load_complete_dataset(self):
        data = pd.read_csv(self.path_to_complete_dataset, index_col="id")
        return data

    def get_training_length(self):
        total_length = len(self.data)
        training_proportion = 0.8
        training_length = round(total_length * training_proportion)
        return training_length

    def get_testing_length(self):
        total_length = len(self.data)
        training_length = self.get_training_length()
        testing_length = total_length - training_length
        return testing_length

    def get_training_dataset(self):
        training_length = self.get_training_length()
        train = self.data.head(training_length)
        return train

    def get_testing_dataset(self):
        testing_length = self.get_testing_length()
        test = self.data.iloc[-testing_length:, self.data.columns != "target"]
        return test

    def get_example_submission(self):
        testing_length = self.get_testing_length()
        example_submission = self.get_testing_dataset().copy()
        example_submission["target"] = np.random.rand(testing_length)
        example_submission = example_submission[["target"]]
        return example_submission

    def get_behind_the_wall_solution(self):
        testing_length = self.get_testing_length()
        solution = self.data[["target"]].tail(testing_length)
        return solution

    def get_training_path(self):
        directory = str(Path(self.path_to_complete_dataset).parents[0])
        training_path = path.join(directory, "train.csv")
        return training_path

    def get_testing_path(self):
        directory = str(Path(self.path_to_complete_dataset).parents[0])
        testing_path = path.join(directory, "test.csv")
        return testing_path

    def get_example_submission_path(self):
        directory = str(Path(self.path_to_complete_dataset).parents[0])
        example_submission_path = path.join(directory, "example_submission.csv")
        return example_submission_path

    def save_training_dataset(self):
        training_dataset = self.get_training_dataset()
        path_to_training = self.get_training_path()
        training_dataset.to_csv(path_to_training)

    def save_testing_dataset(self):
        testing_dataset = self.get_testing_dataset()
        path_to_testing = self.get_testing_path()
        testing_dataset.to_csv(path_to_testing)

    def save_example_submission(self):
        example_submission = self.get_example_submission()
        path_to_example_submission = self.get_example_submission_path()
        example_submission.to_csv(path_to_example_submission)

    def init(self):
        self.save_training_dataset()
        self.save_testing_dataset()
        self.save_example_submission()

    def get_mean_absolute_error(self, path_to_submission):
        solution = self.get_behind_the_wall_solution()
        submission = load_submission(path_to_submission)
        error = solution["target"] - submission["target"]
        mean_absolute_error = error.abs().mean()
        return mean_absolute_error

    def evaluate_single_submission(self, path_to_submission):
        mean_absolute_error = self.get_mean_absolute_error(path_to_submission)
        print(f"Submission: {path_to_submission}\nMean absolute error: {mean_absolute_error}")
