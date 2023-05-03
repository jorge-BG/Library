###Imports###
from resources.Library import Library
from resources.UI import UI
from resources.Book import Book
import sys 

menuOption= "main"
user_input= str()
exit= 1

UI_Instance=UI()
file=  sys.argv[1]
LoadedLibrary= Library(file)
NewBook= Book()

while (exit):
    match menuOption:
        case "main":
            UI_Instance.Options_Menu()
            user_input= input()
            menuOption= user_input
        case "1":
            UI_Instance.New_Book_Parameters("Title")
            menuOption= "Author"
            user_input= input()
            NewBook.set_book_title(user_input)
        case "Author":
            UI_Instance.New_Book_Parameters("Author")
            menuOption= "ISBN"
            user_input= input()
            NewBook.set_book_author(user_input)
        case "ISBN":
            UI_Instance.New_Book_Parameters("ISBN")
            menuOption= "Year"
            user_input= input()
            NewBook.set_book_isbn(user_input)
        case "Year":
            UI_Instance.New_Book_Parameters("Publication Year")
            menuOption= "Upgrade"
            user_input= input()
            NewBook.set_book_pyear(user_input)
            LoadedLibrary.registerBook(NewBook)
        case "Upgrade":
            UI_Instance.Upgrade_Library(LoadedLibrary.getOrderedBookEntries())
            user_input= input("Are you sure you want to upgrade the library? (Y/n):  ")
            if (user_input == "Y" or user_input == "y"):
                LoadedLibrary.addBookToDatabase(NewBook)
            else:
                LoadedLibrary.unregisterBook(NewBook)
            menuOption="main"
        case "2":
            UI_Instance.Print_Library(LoadedLibrary.getOrderedBookEntries())
            input("\n Press Any Key to continue")
            menuOption="main"
        case "q":
            UI_Instance.Farewell_Menu()
            menuOption="q"
            exit=0
        case "Q":
            UI_Instance.Farewell_Menu()
            menuOption="Q"
            exit=0
    
