def parse_book(book_str, chars_per_line, lines_per_page):
    """
    Write a program that takes in the contents of a book (as a String)
    and the page dimensions (characters per line, number of lines per page), 
    and returns a formatted book.
    """
    TRUNCATE_SYMBOL = "-"
    SPACE = " "
    book = []
    
    #arr of strings from our book
    print(book_str)
    split_book = book_str.split(" ")
    print(split_book)

    word_ptr = 0
    line = ""
    page = []
    line_capacity = chars_per_line    
    
    while word_ptr < len(split_book):
        word = split_book[word_ptr]
        length = len(word) + 1            
        
        #can I fit word into line?
        if line_capacity - length > 0:
            line = line + word + SPACE
            line_capacity = line_capacity - length
            word_ptr += 1
        else:
            #check if page is full
            if len(page) < lines_per_page:
                page.append(line)
                line = ""
                line_capacity = chars_per_line
            else: 
                #move to a new page
                book.append(page)
                page = []               
    print(book)
    return book
    
    
txt = "Write a program that takes in the contents of a book"
bobok = parse_book(txt, 6, 4)
print(bobok)


"""
prompt: "Write a program that takes in the contents of a book (as a String) and the page dimensions (characters per line, number of lines per page), and returns a formatted book."


getNextLine -> String, int (page number) [iterator]

["This is\nmy book.", "It is\nvery", "short."]
[["This is", "my book."], ["It is", "very"], ["short."]] ****
{ 1: ["This is", "my book."],
  2: ["It is", "very"],
  3: ["short."] 
}

or use an iterator


characters per line
    is a word too long (possible truncation)
    
number of lines per page
    


A brown fox ju-
mped over the ...

A brown fox____
jumped 
computersssss-
ss

book = [ ] 
page = ["this ", "is my " ]

6chars per line
5lines per page


**do we truncate??**
my 
bookk-
eeper


my boo-
kepper


this is my book -> ["this", "is", "my", "book"]
"""