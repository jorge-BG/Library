from resources.Book import Book

class Library():

    Books= dict()
    file= str()

    def __init__(self, file):
        self.file=file
        self.LoadDatabaseFromFile(file)

    def LoadDatabaseFromFile(self, file:str ):
        with open(file) as data:
            for entry in data.readlines():
                book_info= entry.split("/",4)
                book= Book(book_info[0],book_info[1],book_info[2],book_info[3])
                self.registerBook(book)

    def registerBook(self, book:Book) :
        self.Books[book.get_book_isbn()]=book

    def unregisterBook(self,book:Book):
        self.Books.pop(book.get_book_isbn())

    def addBookToDatabase(self,book:Book):

        with open(self.file,"w") as database:
            for e in self.getOrderedBooks():
                database.write(e.get_book_entry())

    def getOrderedBooks(self)->list[Book]:
        bookList= list()
        for b in self.Books.keys():
            bookList.append(b)
        bookList.sort()
        return map(lambda x:self.Books[x],bookList)
    
    def getOrderedBookEntries(self):
        ordered=self.getOrderedBooks()
        return map(lambda x:x.get_book_entry(),ordered)


