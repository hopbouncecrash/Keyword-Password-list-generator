#itertool import
import itertools
#Input wordlists
def menu():    
    print("""
    Please specify mode: 1) password generator 2) prefix adder 3) suffix adder
    H for help, Q to Quit
    """)
    initialtrigger=input()
    if initialtrigger=="H":
        print("""Password Generator generates passwords based on a wordlist. It capitalizes, lowercases, and does
common substitutions such as @ for a and 0 for o, on all the words in the wordlist.
Wordlist should be formatted as a text file with newlines separating each word
Prefix adder will add common prefixes to all words in your wordlist. You can specify the prefix file used.
or use the default prefixes. Prefix file should be formatted as a text file with newlines separating each prefix
Suffix adder will add common suffixes to all words in your wordlist. You can specify the prefix file used,
or use the default suffixes. Suffix file should be formatted as a text file with newlines separating each suffix
    """)
        menu()
    if initialtrigger=="1":
        combomaker()
    if initialtrigger=="2":
        prefixadder()
    if initialtrigger=="3":
        suffixadder()
    if initialtrigger=="Q":
        quit()

def combomaker():
    print("Input wordlist file:")
    wordlistfile=input()
    openwordlist=open(wordlistfile, "r")
    readwordlist=openwordlist.read()
    wordlist=readwordlist.split("\n")
    #create list of permutations of the words
    print("Input length of final words:(each length larger than 1 will take an exponentially larger amount of time")
    Sizeofcombos=input()
    Sizeofcombos=int(Sizeofcombos)
    #Permutations test:
    Comboinit=0
    combolist=[]
    while Comboinit<Sizeofcombos:
        a= itertools.permutations(wordlist, Comboinit+1)
        y = [''.join(i) for i in a]
        combolist=y+combolist
        Comboinit=Comboinit+1
    #Elimintating Duplicates
    combolist=list(dict.fromkeys(combolist))
    #sorting the list
    def lenFunc(e):
        return len(e)
    combolist.sort(key=lenFunc)
    #specify output file
    print("Specify output file:")
    outfile=input()
    #initializing dictionary, if you want to put in/get rid of letter replacements, modify this dictionary
    init_dict = {'!' : ['i', 'l','|','L','I','!'],'|' : ['i', 'I','!','L','|','l'],'(' : ['C', 'c','('],'0' : ['o', 'O','0'],'+' : ['T', 't','+'],'@' : ['A', 'a','@'],'$' : ['S', 's','$'],'a' : ['a','A', '@'], 'b' : ['B','8','b'], 'c' : ['C', '(','c'], 'd' : ['D','d'], 'e' : ['e','E','3'], 'f' : ['F','f'], 'g' : ['G','g'], 'h' : ['H','h'], 'i' : ['I','l','!','|','L','i'], 'j' : ['J','j'], 'k' : ['K','k'], 'l' : ['l','i','!','|','L','I'], 'm' : ['M','m'], 'n' : ['N','n'], 'o' : ['O','0','o'], 'p' : ['P','p'], 'q' : ['Q','q'], 'r' : ['R','r'], 's' : ['S','$','s'], 't' : ['T','+','t'], 'u' : ['U','V','v','u'], 'v' : ['u','U','V','v'], 'w' : ['W','w'], 'x' : ['X','*','x'], 'y' : ['Y','y'], 'z' : ['Z','z']}
    #initialize final list
    finalist=[]
    for word in combolist:
        word=word.lower()     

        # Building new dictionary using only the letters from the word by pulling entries from the existing dictionary
        word_dict={}
        for letter in word:
            if letter in init_dict.keys():
                word_dict[letter] = init_dict[letter]
        #creating ordered list of letters in the word:
        orderedlist=[]
        for letter in word:
            if letter in init_dict.keys():
                orderedlist.append(init_dict[letter])
            else:
                orderedlist.append(list(letter))
        #calculate and extend to final list
        result=list(itertools.product(*orderedlist))
        finalist.extend(result)
    # Outputting result 
    f = open(outfile, "w")
    for listword in finalist:
        word=''
        for letter in listword:
            word=word+letter
        print(word,file=f)
    f.close()
    print("Outputted successfully to:" + outfile)
    menu()
def suffixadder():
    print('Enter in the suffix file:')
    suffixfile=input()
    #suffix file reading into list
    suffix=open(suffixfile, "r")
    suffixdata=suffix.read()
    suffixlist =suffixdata.split("\n")
    suffixlist.append("")
    #input wordlist
    print('Enter in the wordlist:')
    wordlistfile=input()
    #wordlist file reading into list
    wordlist=open(wordlistfile, "r")
    wordlistdata=wordlist.read()
    wordlistlist = wordlistdata.split("\n")
    #input outfile
    print('Enter in the output file:')
    outfile=input()
    #append all suffix to wordlist
    finalist=[]
    for words in wordlistlist:
        tempword=''
        for suffixes in suffixlist:
            tempword=words+suffixes
            finalist.append(tempword)
    #outing the file
    f = open(outfile, "w")
    for listword in finalist:
        word=''
        for letter in listword:
            word=word+letter
        print(word,file=f)
    f.close()
    menu()
def prefixadder():
    #input prefix
    print('Enter in the prefix file:')
    prefixfile=input()
    #prefix file reading into list
    prefix=open(prefixfile, "r")
    prefixdata=prefix.read()
    prefixlist =prefixdata.split("\n")
    prefixlist.append("")
    #input wordlist
    print('Enter in the wordlist:')
    wordlistfile=input()
    #wordlist file reading into list
    wordlist=open(wordlistfile, "r")
    wordlistdata=wordlist.read()
    wordlistlist = wordlistdata.split("\n")
    #input outfile
    print('Enter in the output file:')
    outfile=input()
    #append all prefix to wordlist
    finalist=[]
    for words in wordlistlist:
        tempword=''
        for prefixes in prefixlist:
            tempword=prefixes+words
            finalist.append(tempword)
    #outing the file
    f = open(outfile, "w")
    for listword in finalist:
        word=''
        for letter in listword:
            word=word+letter
        print(word,file=f)
    f.close()
    menu()
menu()