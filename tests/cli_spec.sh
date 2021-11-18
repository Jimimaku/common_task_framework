#shellcheck shell=sh
Describe "geci-ctf"
  clean() { \
            rm --force tests/test_dataset_simple/example_submission.csv; \
            rm --force tests/test_dataset_simple/test.csv; \
            rm --force tests/test_dataset_simple/train.csv; \
            rm --force tests/test_dataset_pollos_petrel/example_submission.csv; \
            rm --force tests/test_dataset_pollos_petrel/test.csv; \
            rm --force tests/test_dataset_pollos_petrel/train.csv; \
            }
  Before "clean"
  After "clean"

  It "partitions the complete dataset"
    When call geci-ctf init tests/test_dataset_simple/complete_dataset.csv
    The file "tests/test_dataset_simple/example_submission.csv" should be exist
    The file "tests/test_dataset_simple/test.csv" should be exist
    The file "tests/test_dataset_simple/train.csv" should be exist
  End

  It "evaluates a submission"
    When call geci-ctf evaluate tests/test_dataset_simple/complete_dataset.csv tests/test_dataset_simple/test_submission.csv
    The first line of output should equal "Submission: tests/test_dataset_simple/test_submission.csv"
    The second line of output should include "Mean absolute error: 0.4246"
  End

  It "evaluates a directory"
    When call geci-ctf evaluate tests/test_dataset_simple/complete_dataset.csv tests/test_dataset_simple --directory
    The first line of output should equal "| submission                                     |   mean_absolute_error |"
    The fourth line of output should include "| tests/test_dataset_simple/test_submission.csv  |                0.4246 |"
  End

  It "test.csv includes NA"
    geci-ctf init tests/test_dataset_pollos_petrel/complete_dataset.csv
    When call cat tests/test_dataset_pollos_petrel/test.csv
    The second line of output should equal "B6-2012-09-02,28.1,NA,NA,NA,NA,NA"
    The third line of output should equal "B6-2012-09-03,32.0,16.2,16.0,10.3,NA,NA"
  End

  It "train.csv includes NA"
    geci-ctf init tests/test_dataset_pollos_petrel/complete_dataset.csv
    When call cat tests/test_dataset_pollos_petrel/train.csv
    The second line of output should equal "B6-2012-08-25,9.8,12.3,14.0,8.1,NA,NA,1.0"
    The line 9 of output should equal "B6-2012-09-01,22.5,NA,NA,NA,NA,NA,8.0"
  End
End
