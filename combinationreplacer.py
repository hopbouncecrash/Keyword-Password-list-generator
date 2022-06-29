# Python3 code to demonstrate working of 
# Character Replacement Combination
# Using zip() + list comprehension + replace() + product()
from itertools import product
  
# initializing string
word = str(input("enter word:"))
outfile=str(input("enter output file:"))
word=word.lower()
  
# initializing dictionary
test_dict = {'a' : ['A', '@'], 'b' : ['B','8'], 'c' : ['C', '('], 'd' : ['D'], 'e' : ['E','3'], 'f' : ['F'], 'g' : ['G'], 'h' : ['H'], 'i' : ['I','l','!','|','L'], 'j' : ['J'], 'k' : ['K'], 'l' : ['i','!','|','L','I'], 'm' : ['M'], 'n' : ['N'], 'o' : ['O','0'], 'p' : ['P'], 'q' : ['Q'], 'r' : ['R'], 's' : ['S','$'], 't' : ['T','+'], 'u' : ['U','V','v'], 'v' : ['u','U','V'], 'w' : ['W'], 'x' : ['X','*'], 'y' : ['Y',], 'z' : ['Z']}
  
# adding original character to possible characters 
for key in test_dict.keys():
    if key not in test_dict[key]:
        test_dict[key].append(key)
#print(test_dict)
#print(len(test_dict))
res = []

# Building new dictionary using only the letters from the word by pulling entries from the existing dictionary
final_dict={}
for letter in word:
    if letter in test_dict.keys():
        final_dict[letter] = test_dict[letter]
  
# constructing all possible combination of values using product
# mapping using zip()
for sub in [zip(final_dict.keys(), chr) for chr in product(*final_dict.values())]:
    temp = word
    for repls in sub:
          
        # replacing all elements at once using * operator
        temp = temp.replace(*repls)
    res.append(temp)
  
# Outputting result 
f = open(outfile, "w")
for stuff in res:
    print(stuff,file=f)
f.close()