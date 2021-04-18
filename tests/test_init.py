import common_task_framework as ctf

path_to_complete_dataset = "tests/test_data/complete_dataset.csv"


def test_load_complete_dataset():
    data = ctf.load_complete_dataset(path_to_complete_dataset)
    obtained_length = len(data)
    expected_length = 27
    assert expected_length == obtained_length


def test_get_trainig_length():
    data = ctf.load_complete_dataset(path_to_complete_dataset)
    obtained_length = ctf.get_trainig_length(data)
    expected_length = round(27 * 0.8)
    assert expected_length == obtained_length


def test_get_testing_length():
    data = ctf.load_complete_dataset(path_to_complete_dataset)
    obtained_length = ctf.get_testing_length(data)
    expected_length = round(27 * 0.2)
    assert expected_length == obtained_length
