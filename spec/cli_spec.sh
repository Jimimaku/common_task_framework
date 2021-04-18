#shellcheck shell=sh

It 'exists'
  When call geci-ctf --help
  The first line of output should eq "Usage: main.py [OPTIONS] PATH_TO_COMPLETE_DATASET"
End
