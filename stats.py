def numwords_instring(stringin):
    dumplist = stringin.split()
    wordcount = 0
    for word in dumplist:
        wordcount += 1

<<<<<<< HEAD
    print (f"Found {wordcount} total words") 
=======
    print (f"{wordcount} words found in the document") 
>>>>>>> f5a07e26cc930b80736f434f8baf48d428af3629
    return wordcount


def charcount_instring(stringin):
    newstringin = stringin.lower()
    counter = {}
    for char in newstringin:
        if char not in counter: 
            counter[char] = 1
        elif char in counter:
            counter[char] += 1
<<<<<<< HEAD
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

=======
    print (counter)
    return counter
>>>>>>> f5a07e26cc930b80736f434f8baf48d428af3629
