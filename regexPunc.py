import re, string
s = "String.With!Punctuation?21:09:05...12/14/15"
cs = "He's..not!what y'all//thought...Harry!!!!"
nps = "Welcome to the string tester with no punctuation" 
 
def remPunc(str) :
    #Top return also works, however regex is faster bc regex is king
    #return temp.translate(None, string.punctuation)
    return re.sub(r'[^\w\s]',' ',str)

print("1: " + s) 
print(remPunc(s))
print("2: " + cs)
print(remPunc(cs))
print("3: " + nps)
print(remPunc(nps))
