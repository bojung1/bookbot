from stats import numwords_instring 
from stats import charcount_instring 
<<<<<<< HEAD
from stats import sort_dict
=======
>>>>>>> f5a07e26cc930b80736f434f8baf48d428af3629

def get_book_text(path_file):
    with open(path_file) as f:
        file_barf = f.read()
    return file_barf

<<<<<<< HEAD
def print_clean_list(listin):
    print ("--------- Character Count -------")
    for dictentry in listin:
        print (f"{dictentry['name']}: {dictentry['num']}")
    print ("============= END ===============")

def main():
    
    bookpath = "./books/frankenstein.txt"
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {bookpath}...")

    bookbarf = get_book_text(bookpath)
    
    print ("----------- Word Count ----------")

    numwords_instring(bookbarf)
    
    

    countchars =  charcount_instring(bookbarf)
    sorted_char_list = sort_dict(countchars)
    print_clean_list(sorted_char_list)
=======

def main():
    bookbarf = get_book_text("./books/frankenstein.txt")
    numwords_instring(bookbarf)
    charcount_instring(bookbarf)
    #print (bookbarf)
>>>>>>> f5a07e26cc930b80736f434f8baf48d428af3629


main() 


