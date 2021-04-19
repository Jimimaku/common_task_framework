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
End