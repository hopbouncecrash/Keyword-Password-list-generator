# Keyword-Password-list-generator
Keywork password list generator using Itertools

Generates a password list that can be used for password cracking based on a keyword.

passwordgenerator.py will 

Usage: Run program in Python.

example: python3 passwordgenerator.py

  passwordgenerator.py has 3 modes, the main password generator module, a prefix adder, and a suffix adder.
  
  Password generator will take a list of words formatted like common wordlists:
  For example, example.txt will be formatted as a text file like so:
  cat
  who
  Steve
  
  and will generator passwords based on those words. Useful to generate an intelligent password cracking list.
  You can specify how many words can be strung together.  It will also do common replacements for letters, such as @ for a and + for t.
  
  Prefix adder will add common prefixes that come before passwords to a wordlist.
  Suffix adder will add common suffixes that come after passwords to a wordlist.
  
  password generator example:
  
  Example input: cat
  
Output file will contain:  
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
