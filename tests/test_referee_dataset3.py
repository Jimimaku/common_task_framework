from ..common_task_framework import get_submission_list, load_submission, Referee
import pandas as pd
import pytest

path_to_complete_dataset = "tests/test_dataset3/complete_dataset.csv"

def test_exceptions_raised_when_no_values():
    with pytest.raises(
        ValueError, match="^There is a record with no values for any explanatory variable$"
    ):
        ctf = Referee(path_to_complete_dataset)
        ctf.load_complete_dataset()
