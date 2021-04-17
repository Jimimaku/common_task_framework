#shellcheck shell=sh

It 'exists'
  When call geci-ctf
  The output should eq 'Hola Mundo'
End
