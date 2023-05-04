from functools import total_ordering 

@total_ordering
class Book():
    # Wrapper class for Book information

    title= str()
    author= str()
    isbn= str()
    pyear= str()

    def __init__(self,title="", author="", isbn="", pyear="") :
        self.title= title
        self.author= author
        self.isbn= isbn
        self.pyear= pyear

    
    def get_book_entry(self)->str:
        #Returns Book Details as required for db interaction
        return self.title+"/"+self.author+"/"+self.isbn+"/"+self.pyear
    
    def get_book_Information(self)->str:
        #Returns Book Details as required for UI printing
        return "Title: "+self.title+" -- "+"Author:  "+self.author+" -- "+"ISBN:  "+self.isbn+" -- "+"Publication Year:  "+self.pyear
    
    def get_book_title(self)->str:
        return self.title
    def set_book_title(self,title)->str:
        self.title=title

    def get_book_author(self)->str:
        return self.author
    
    def set_book_author(self,author)->str:
         self.author=author

    def get_book_isbn(self)->str:
        return self.isbn
    
    def set_book_isbn(self,isbn)->str:
        self.isbn=isbn
    
    def get_book_pyear(self)->str:
        return self.pyear
    
    def set_book_pyear(self,pyear)->str:
        self.pyear=pyear
    
    def __eq__(self,other_book:"Book"):
        return int(self.get_book_isbn()) == int(other_book.get_book_isbn())
    
    def __lt__(self,other_book:"Book"):
        return int(self.get_book_pyear()) < int(other_book.get_book_pyear())