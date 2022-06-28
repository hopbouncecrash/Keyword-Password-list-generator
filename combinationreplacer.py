# input word and convert to lowercase
word = str(input("enter word:"))
outfile=str(input("enter output file:"))
word=word.lower()
#binary function
teststr=word
binarydegrees=2**len(teststr)
length=len(teststr)
x=0
binaries=[]
finalist=[]
while x<binarydegrees:
    binx=bin(x)
    binx=str(binx)
    binx=binx[2:]
    while len(binx)<length:
        binx='0'+binx
    binaries.append(binx)
    x=x+1
#replacement function
def replacechar(char):
    if char == 'a':
        char = '@'
    else: 
        if char == '@':
            char = 'a'
    if char == 'c':
        char = '('
    else: 
        if char == '(':
            char = 'c'
    if char == 'e':
        char = '3'
    else: 
        if char == '3':
            char = 'e'
    if char == 'i':
        char = '!'
    else: 
        if char == '!':
            char = 'i'
    if char == 'l':
        char = '|'
    else: 
        if char == '|':
            char = 'l'
    if char == 'o':
        char = '0'
    else: 
        if char == '0':
            char = 'o'
    if char == 's':
        char = '$'
    else: 
        if char == '$':
            char = 's'
    if char == 't':
        char = '+'
    else: 
        if char == '+':
            char = 't'
    return char
#loop through based on binaries and replace character
for combos in binaries:
    s=0
    rword=word
    while s<len(combos):
        if combos[s]=='0':
            char=rword[s]
            char=replacechar(char)
            rword = rword[:s] + char + rword[s+1:]
        s=s+1
    finalist.append(rword)
#eliminate duplicates
finalist=list(dict.fromkeys(finalist))
capitilizedlist=[]
#lower and upper case combinations
for stuff in finalist:
    for combos in binaries:
        s=0
        rword=stuff
        while s<len(combos):
            if combos[s]=='0':
                char=rword[s]
                char=char.upper()
                rword = rword[:s] + char + rword[s+1:]
            s=s+1
        capitilizedlist.append(rword)
finalist=finalist+capitilizedlist
finalist=list(dict.fromkeys(finalist))
#checking output, comment out print(finalist)
f = open(outfile, "w")
for stuff in finalist:
    print(stuff,file=f)
f.close()