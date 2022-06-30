# Keyword-Password-list-generator
Keywork password list generator using Itertools

Generates a password list that can be used for password cracking based on a keyword.

combinationreplacer.py will 

Usage: Run program in Python.

example: python3 combinationreplacer.py

  combinationreplacer.py takes a word as an argument (example:cat) replaces the letters with common replacements, capitilizes/lowercases the letters, iterates through all combinations, and outs those results to a file.
  prefixadder.py will take a list of prefixes and attach all the prefixes to a list of words, and outputs them to a file.
  suffixadder.py will take a list of suffixes and attach all the suffixes to a list of words, and outputs them to a file.
  
  Combination replacer example:
  
  Example input: cat
  
  outfile will contain:  
(@+  
(@t  
(a+  
(at  
c@+  
c@t  
ca+  
cat  
(@T  
(A+  
(AT  
(At  
(aT  
C@+  
C@T  
C@t  
c@T  
CA+  
Ca+  
cA+  
CAT  
CAt  
CaT  
Cat  
cAT  
cAt  
caT  
