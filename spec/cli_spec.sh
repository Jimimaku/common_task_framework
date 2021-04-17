#shellcheck shell=sh

It 'exists'
  When call geci-ctf Mundo
  The output should eq 'Hola Mundo'
End
