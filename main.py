from stats import numwords_instring 
from stats import charcount_instring 

def get_book_text(path_file):
    with open(path_file) as f:
        file_barf = f.read()
    return file_barf


def main():
    bookbarf = get_book_text("./books/frankenstein.txt")
    numwords_instring(bookbarf)
    charcount_instring(bookbarf)
    #print (bookbarf)


main() 


