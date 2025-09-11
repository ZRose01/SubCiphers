#TODO Generic and Keyword

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def cleanKey(key):
    lettersInKey = set()
    keyOut = ''
    for i in key:
        if i not in lettersInKey:
            keyOut += i
        lettersInKey.add(i)
    return keyOut

print(cleanKey("aagooba"))

