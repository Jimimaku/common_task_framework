from ..common_task_framework import get_submission_list, load_submission, Referee
import os
import pandas as pd

path_to_submission_directory = "tests/test_dataset_incomplete_submission/"
path_to_complete_dataset = path_to_submission_directory + "complete_dataset.csv"
path_to_submission = path_to_submission_directory + "incomplete_submission.csv"
ctf = Referee(path_to_complete_dataset)


def test_load_complete_dataset():
    data = ctf.load_complete_dataset()
    obtained_length = len(data)
    expected_length = 27
    assert expected_length == obtained_length


def test_get_testing_length():
    obtained_length = ctf.get_testing_length()
    expected_length = round(27 * 0.2)
    assert expected_length == obtained_length


def test_get_testing_dataset():
    test = ctf.get_testing_dataset()
    obtained_rows = len(test)
    expected_rows = ctf.get_testing_length()
    assert expected_rows == obtained_rows
    obtained_column_names = list(test.columns)
    expected_column_names = ["x"]
    assert obtained_column_names == expected_column_names


def test_get_example_submission():
    example_submission = ctf.get_example_submission()
    obtained_rows = len(example_submission)
    expected_rows = ctf.get_testing_length()
    assert expected_rows == obtained_rows
    obtained_column_names = list(example_submission.columns)
    expected_column_names = ["target"]
    assert expected_column_names == obtained_column_names
    obtained_example_target = example_submission["target"].iloc[0]
    assert obtained_example_target >= 0


def test_get_behind_the_wall_solution():
    solution = ctf.get_behind_the_wall_solution()
    obtained_rows = len(solution)
    expected_rows = ctf.get_testing_length()
    assert expected_rows == obtained_rows
    obtained_column_names = list(solution.columns)
    expected_column_names = ["target"]
    assert expected_column_names == obtained_column_names
    obtained_solution_target = solution["target"].iloc[0]
    expected_solution_target = ctf.data["target"].iloc[ctf.get_training_length()]
    assert expected_solution_target == obtained_solution_target


def test_save_testing_dataset():
    path_to_testing = ctf.get_testing_path()
    if os.path.exists(path_to_testing):
        os.remove(path_to_testing)
    ctf.save_testing_dataset()
    assert os.path.exists(path_to_testing)
    obtained_first_column = pd.read_csv(path_to_testing).columns[0]
    expected_first_column = "id"
    assert expected_first_column == obtained_first_column
    os.remove(path_to_testing)


def test_save_example_submission():
    path_to_example_submission = ctf.get_example_submission_path()
    if os.path.exists(path_to_example_submission):
        os.remove(path_to_example_submission)
    ctf.save_example_submission()
    assert os.path.exists(path_to_example_submission)
    obtained_first_column = pd.read_csv(path_to_example_submission).columns[0]
    expected_first_column = "id"
    assert expected_first_column == obtained_first_column
    os.remove(path_to_example_submission)


def test_load_submission():
    submission = load_submission(path_to_submission)
    obtained_length = len(submission)
    expected_length = ctf.get_testing_length()
    assert expected_length == obtained_length


def test_get_submission_list():
    obtained_submission_list = get_submission_list(path_to_submission_directory)
    expected_submission_list = [
        path_to_submission_directory + "incomplete_submission.csv",
        path_to_submission_directory + "overfull_submission.csv",
        path_to_submission_directory + "unexpected_submission.csv",
    ]
    assert sorted(expected_submission_list) == sorted(obtained_submission_list)
