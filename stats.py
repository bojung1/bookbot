def numwords_instring(stringin):
    dumplist = stringin.split()
    wordcount = 0
    for word in dumplist:
        wordcount += 1

    print (f"{wordcount} words found in the document") 
    return wordcount


def charcount_instring(stringin):
    newstringin = stringin.lower()
    counter = {}
    for char in newstringin:
        if char not in counter: 
            counter[char] = 1
        elif char in counter:
            counter[char] += 1
    print (counter)
    return counter
