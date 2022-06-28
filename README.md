# Keyword-Password-list-generator
Keywork password list generator

Generates a password list that can be used for password cracking based on a keyword.

Feedback is welcome, I plan to add header and footer functionality as well.

Usage: Run program in Python.

example: python3 combinationreplacer.py

Currently one working program:

  combinationreplacer.py takes a word as an argument (example:cat) replaces the letters with common replacements, capitilizes/lowercases the letters, and outs those    results to a file.
  
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
