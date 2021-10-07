from ..common_task_framework import get_submission_list, load_submission, Referee
import os
import pandas as pd

path_to_complete_dataset = "tests/test_dataset2/complete_dataset.csv"
ctf = Referee(path_to_complete_dataset)
path_to_submission = "tests/test_dataset2/test_submission.csv"
path_to_submission_directory = "tests/test_dataset2"


def test_load_complete_dataset():
    data = ctf.load_complete_dataset()
    obtained_length = len(data)
    expected_length = 10
    assert expected_length == obtained_length


def test_get_training_length():
    obtained_length = ctf.get_training_length()
    expected_length = round(10 * 0.8)
    assert expected_length == obtained_length


def test_get_testing_length():
    obtained_length = ctf.get_testing_length()
    expected_length = round(10 * 0.2)
    assert expected_length == obtained_length


def test_get_testing_dataset():
    test = ctf.get_testing_dataset()
    obtained_rows = len(test)
    expected_rows = ctf.get_testing_length()
    assert expected_rows == obtained_rows
    obtained_column_names = list(test.columns)
    expected_column_names = [
        "Peso",
        "Longitud_tarso",
        "Longitud_ala",
        "Longitud_pico",
        "Longitud_pluma_interior_de_la_cola",
        "Longitud_pluma_exterior_de_la_cola",
    ]
    assert obtained_column_names == expected_column_names


def test_get_training_path():
    obtained_path = ctf.get_training_path()
    expected_path = "tests/test_dataset2/train.csv"
    assert expected_path == obtained_path


def test_get_testing_path():
    obtained_path = ctf.get_testing_path()
    expected_path = "tests/test_dataset2/test.csv"
    assert expected_path == obtained_path


def test_get_example_submission_path():
    obtained_path = ctf.get_example_submission_path()
    expected_path = "tests/test_dataset2/example_submission.csv"
    assert expected_path == obtained_path


def test_load_submission():
    submission = load_submission(path_to_submission)
    obtained_length = len(submission)
    expected_length = ctf.get_testing_length()
    assert expected_length == obtained_length


def test_get_mean_absolute_error():
    obtained_mean_absolute_error = round(ctf.get_mean_absolute_error(path_to_submission), 16)
    expected_mean_absolute_error = 9.5
    assert expected_mean_absolute_error == obtained_mean_absolute_error


def test_get_submission_list():
    obtained_submission_list = get_submission_list(path_to_submission_directory)
    expected_submission_list = [
        "tests/test_dataset2/test_submission.csv",
        "tests/test_dataset2/test2_submission.csv",
    ]
    assert sorted(expected_submission_list) == sorted(obtained_submission_list)


def test_get_mean_absolute_error_list():
    obtained_mean_absolute_error_list = ctf.get_mean_absolute_error_list(
        path_to_submission_directory
    )
    expected_mean_absolute_error_list = pd.DataFrame(columns=["submission", "mean_absolute_error"])
    expected_mean_absolute_error_list = expected_mean_absolute_error_list.append(
        {"submission": "tests/test_dataset2/test_submission.csv", "mean_absolute_error": 9.5},
        ignore_index=True,
    )
    expected_mean_absolute_error_list = expected_mean_absolute_error_list.append(
        {"submission": "tests/test_dataset2/test2_submission.csv", "mean_absolute_error": 20.5},
        ignore_index=True,
    )
    pd.testing.assert_frame_equal(
        expected_mean_absolute_error_list.reset_index(drop=True),
        obtained_mean_absolute_error_list.reset_index(drop=True),
    )
