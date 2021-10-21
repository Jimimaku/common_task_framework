from ..common_task_framework import get_submission_list, load_submission, Referee
import pandas as pd
import pytest

path_to_complete_dataset = "tests/test_dataset3/complete_dataset.csv"
ctf = Referee(path_to_complete_dataset)


def test_load_complete_dataset():
    with pytest.raises(ValueError, match="^There is a record with no values for any explanatory variable$"):
        ctf.load_complete_dataset()
