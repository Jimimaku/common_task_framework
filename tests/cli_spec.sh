#shellcheck shell=sh
Describe "geci-ctf"
  clean() { \
            rm --force tests/test_dataset1/example_submission.csv; \
            rm --force tests/test_dataset1/test.csv; \
            rm --force tests/test_dataset1/train.csv; \
            rm --force tests/test_dataset2/example_submission.csv; \
            rm --force tests/test_dataset2/test.csv; \
            rm --force tests/test_dataset2/train.csv; \
            }
  Before "clean"
  After "clean"

  It "partitions the complete dataset"
    When call geci-ctf init tests/test_dataset1/complete_dataset.csv
    The file "tests/test_dataset1/example_submission.csv" should be exist
    The file "tests/test_dataset1/test.csv" should be exist
    The file "tests/test_dataset1/train.csv" should be exist
  End

  It "evaluates a submission"
    When call geci-ctf evaluate tests/test_dataset1/complete_dataset.csv tests/test_dataset1/test_submission.csv
    The first line of output should equal "Submission: tests/test_dataset1/test_submission.csv"
    The second line of output should include "Mean absolute error: 0.4246"
  End
  
  It "evaluates a directory"
    When call geci-ctf evaluate tests/test_dataset1/complete_dataset.csv tests/test_dataset1 --directory
    The first line of output should equal "| submission                               |   mean_absolute_error |"
    The fourth line of output should include "| tests/test_dataset1/test_submission.csv  |                0.4246 |"
  End

    It "partitions the complete dataset"
    geci-ctf init tests/test_dataset2/complete_dataset.csv
    When call cat init tests/test_dataset2/test.csv
    The second line of output should equal "B6-2012-09-02,28.1,NA,NA,NA,NA,NA"
    The third line of output should equal "B6-2012-09-03,32.0,16.2,16.0,10.3,NA,NA"
  End
End