#shellcheck shell=sh
Describe "geci-ctf"
  clean() { \
            rm --force tests/test_data/example_submission.csv; \
            rm --force tests/test_data/test.csv; \
            rm --force tests/test_data/train.csv; \
            }
  Before "clean"
  After "clean"

  It "partitions the complete dataset"
    When call geci-ctf init tests/test_data/complete_dataset.csv
    The file "tests/test_data/example_submission.csv" should be exist
    The file "tests/test_data/test.csv" should be exist
    The file "tests/test_data/train.csv" should be exist
  End

  It "evaluates a submission"
    When call geci-ctf evaluate tests/test_data/complete_dataset.csv tests/test_data/test_submission.csv
    The first line of output should equal "Submission: tests/test_data/test_submission.csv"
    The second line of output should include "Mean absolute error: 0.4246"
  End
  
  It "evaluates a directory"
    When call geci-ctf evaluate tests/test_data/complete_dataset.csv tests/test_data --directory
    The first line of output should equal "| submission                           |   mean_absolute_error |"
    The fourth line of output should include "| tests/test_data/test_submission.csv  |                0.4246 |"
  End
End