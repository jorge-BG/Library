from resources.Book import Book

class Library():
    # Class that Interacts with the database(file) and handles database information

    Books= dict() # Book Registry - Could be considered the cache version of the database
                  #                 is kept up to date with db and user input
    file= str()

    def __init__(self, file):
        self.file=file
        self.load_database_from_file(file)

    def load_database_from_file(self, file:str ):
        try:
            with open(file) as data:
                for entry in data.readlines():
                    book_info= entry.split("/",4)

                    book= Book(book_info[0],book_info[1],book_info[2],book_info[3].rstrip("\n"))
                    self.register_book(book)
        except  FileNotFoundError:
            print("\nFile Not Found. Library could not load")
        except  OSError:
            print("\nAn error ocurred while loading Library Data.")
        except ValueError:
            print("\nAn error ocurred while reading Library Data.")

    def register_book(self, book:Book):
        # Keeps track of a new book adding it to the registry , not yet adding it to db
        self.Books[book.get_book_isbn()]=book

    def is_book_in_database(self,book:Book)->int:
        val= self.Books.get(book.get_book_isbn(),0)
        return bool(val)

    def unregister_book(self,book:Book):
        # In case user decides not to add the book to db
        self.Books.pop(book.get_book_isbn())

    def add_book_to_database(self,book:Book):
        try:
            with open(self.file,"w") as database:
                for e in self.get_registered_book_entries("db"):
                    database.write(e+"\n")
        except  FileNotFoundError:
            print("\nFile Not Found. Library could not load")
        except  OSError:
            print("\nAn error ocurred while loading Library Data.")

    def get_registered_book_entries(self,mode)->list[str]:
        # Gets the Books from the Registry and provides relevant information
        # mode -> db provides book info as required for database storage
        # mode -> ui provides book inof as requred for UI printing
        bookList:list[Book]= list()
        for b in self.Books.keys():
            bookList.append(self.Books[b])
            bookList.sort()
        if mode == "db":
            entry_list=map(lambda x:x.get_book_entry(),bookList)
        elif mode == "ui":
            entry_list=map(lambda x:x.get_book_Information(),bookList)
        return entry_list

        


