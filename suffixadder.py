#input suffix
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