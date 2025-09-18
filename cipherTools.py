ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def cleanKey(key):
    """
    Deduplicates elements in an iterable

    Args:
        key(iterable): value to deduplicate
    """
    lettersInKey = set() # create an empty set that will contain the letters we've used
    keyOut = '' # empty string to return
    for i in key: # for every letter in the submitted key...
        if i not in lettersInKey: # if it's a new letter...
            keyOut += i # add it to the output
        lettersInKey.add(i) # no matter what, add it to the set
    return keyOut # spit out our string deduped

def encode(toEncode:str , outputLoc:str , encodePattern:str):
    """
    Encodes a textfile using encodePattern
    
    Args:
        toEncode(str): location of txt file to encode
        outputLoc(str): location to write encoded txt
        encodePattern(str): 26 character long string to substitute by
    """
    if(len(cleanKey(encodePattern)) != 26 or cleanKey(encodePattern) != encodePattern): # make sure encodePattern is the right length
        raise ValueError("encodePattern must be exactly 26 characters long with no duplicated letters")
    with open(toEncode , "r") as tR:
        with open(outputLoc , "w") as tW:
            tR = tR.read()
            out = "" # init a var to write out output to
            for i in tR: # for each letter in the input text...
                upper = i.isupper() # remember if the character is uppercase
                letterIndex = ALPHABET.find(i.lower()) # find the index in the lowercase set
                if(letterIndex != -1): # if it exists in the set (ie is a letter)
                    foundLetter = encodePattern[letterIndex] # match the found index
                    out += foundLetter.upper() if upper else foundLetter # ternary to preserve case
                else:
                    out += i # add the punctuation or space
            tW.write(out) # write that jawn to the output file

def decode(toEncode:str , outputLoc:str , encodePattern:str , originalPattern = ALPHABET):
    """
    decodes a textfile using encodePattern
    
    Args:
        toEncode(str): location of txt file to decode
        outputLoc(str): location to write decoded txt
        encodePattern(str): 26 character long string to substitute by
        [Optional] originalPattern(str): defaults to ALPHABET, but needs to be specified sometimes
    """
    if(len(cleanKey(encodePattern)) != 26 or cleanKey(encodePattern) != encodePattern): # make sure encodePattern is the right length
        raise ValueError("encodePattern must be exactly 26 characters long with no duplicated letters")
    with open(toEncode , "r") as tR:
        with open(outputLoc , "w") as tW:
            tR = tR.read()
            out = "" # init a var to write out output to
            for i in tR: # for each letter in the input text...
                upper = i.isupper() # remember if the character is uppercase
                letterIndex = encodePattern.find(i.lower()) # find the index in the lowercase set
                if(letterIndex != -1): # if it exists in the set (ie is a letter)
                    foundLetter = ALPHABET[letterIndex] # match the found index
                    out += foundLetter.upper() if upper else foundLetter # ternary to preserve case
                else:
                    out += i # add the punctuation or space
            tW.write(out) # write that jawn to the output file