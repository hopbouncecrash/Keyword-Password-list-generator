# Python3 code to do character replacement
# Input a single word
# Input output file, will be a text file
# Output file should be able to be used for password cracking programs like John the Ripper etc.
# Any suggestions or comments, please send to jamesjwu83@gmail.com
import itertools
  
# initializing string
word = str(input("enter word:"))
outfile=str(input("enter output file:"))
word=word.lower()
  
# initializing dictionary
test_dict = {'!' : ['i', 'l','|','L','I'],'|' : ['i', 'I','!','L'],'(' : ['C', 'c'],'0' : ['o', 'O'],'+' : ['T', 't'],'@' : ['A', 'a'],'$' : ['S', 's'],'a' : ['A', '@'], 'b' : ['B','8'], 'c' : ['C', '('], 'd' : ['D'], 'e' : ['E','3'], 'f' : ['F'], 'g' : ['G'], 'h' : ['H'], 'i' : ['I','l','!','|','L'], 'j' : ['J'], 'k' : ['K'], 'l' : ['i','!','|','L','I'], 'm' : ['M'], 'n' : ['N'], 'o' : ['O','0'], 'p' : ['P'], 'q' : ['Q'], 'r' : ['R'], 's' : ['S','$'], 't' : ['T','+'], 'u' : ['U','V','v'], 'v' : ['u','U','V'], 'w' : ['W'], 'x' : ['X','*'], 'y' : ['Y',], 'z' : ['Z']}
  
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
#creating ordered list of letters in the word:
orderedlist=[]
for letter in word:
    if letter in test_dict.keys():
        orderedlist.append(test_dict[letter])
    else:
        orderedlist.append(list(letter))
#print(orderedlist)

# constructing all possible combination of values using product
# mapping using zip()
#for sub in [zip(orderedlist, chr) for chr in product(*final_dict.values())]:
 #   temp = word
  #  print(sub)
   # for repls in sub:
    #    print(repls)
     #   print(temp)
      #  # replacing all elements at once using * operator
       # temp = temp.replace(*repls)
        #print(temp)
    #res.append(temp)
  
# Outputting result 
f = open(outfile, "w")
#for stuff in res:
#    print(stuff,file=f)
#f.close()

#define final list
finalist=list(itertools.product(*orderedlist))
#print final list
for listword in finalist:
    word=''
    for letter in listword:
        word=word+letter
    print(word,file=f)
f.close()