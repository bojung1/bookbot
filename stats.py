def numwords_instring(stringin):
    dumplist = stringin.split()
    wordcount = 0
    for word in dumplist:
        wordcount += 1

    print (f"Found {wordcount} total words") 
    return wordcount


def charcount_instring(stringin):
    newstringin = stringin.lower()
    counter = {}
    for char in newstringin:
        if char not in counter: 
            counter[char] = 1
        elif char in counter:
            counter[char] += 1
    #print (counter)
    return counter

def sort_on(dictin):
    return dictin["num"]



def sort_dict(dictin):
    newlist = []
    newdict = {} 

    for dictentry in dictin:
        if dictentry.isalpha():
            newdict = {"name":dictentry, "num":dictin[dictentry]}
            newlist.append(newdict)

    newlist.sort(reverse=True, key=sort_on)

    return newlist

