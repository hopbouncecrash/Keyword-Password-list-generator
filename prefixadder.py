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