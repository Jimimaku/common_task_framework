import common_task_framework as ctf


def test_nothing():
    data = ctf.init("tests/test_data/complete_dataset.csv")
    obtained_length = len(data)
    expected_length = 27
    assert expected_length == obtained_length
