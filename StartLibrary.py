###Imports###
from resources.Library import Library
from resources.UI import UI
from resources.Book import Book
from resources.SafeInput import SafeInput
import sys 

#----------Main Script---------------
# Handles overall Library Probam state based on User Input

### Program Variables ###
menu_option= "main"
file=  sys.argv[1]
user_input= str()
exit= 1

### Initialization of functional classes ###
library_menu=UI()
my_library= Library(file)
new_book= Book()
s_i=SafeInput()

input("                <- Press Enter to Continue ->")
while (exit):
    match menu_option:
        case "main":
            library_menu.options_menu()
            user_input , menu_option= s_i.safe_input("main")
        case "1":
            library_menu.new_book_parameters("Title")
            user_input , menu_option= s_i.safe_input("1")
            new_book.set_book_title(user_input)
        case "Author":
            library_menu.new_book_parameters("Author")
            user_input , menu_option= s_i.safe_input("Author")
            new_book.set_book_author(user_input)
        case "ISBN":
            library_menu.new_book_parameters("ISBN")
            user_input , menu_option= s_i.safe_input("ISBN")
            new_book.set_book_isbn(user_input)
        case "Year":
            library_menu.new_book_parameters("Publication Year")
            user_input , menu_option= s_i.safe_input("Year")
            new_book.set_book_pyear(user_input)                
        case "Upgrade":
            found=my_library.is_book_in_database(new_book)
            my_library.register_book(new_book)
            library_menu.upgrade_library(my_library.get_registered_book_entries("ui"), found)
            user_input , menu_option= s_i.safe_input("Upgrade")
            if (user_input == "Y" or user_input == "y"):
                my_library.add_book_to_database(new_book)
            else:
                my_library.unregister_book(new_book)
            my_library= Library(file) # Refreshing information in the registry with file info.
            menu_option="main"
        case "2":
            library_menu.print_library(my_library.get_registered_book_entries("ui"))
            menu_option="main"
        case "q":
            library_menu.farewell_menu()
            exit=0
        case "Q":
            library_menu.farewell_menu()
            exit=0
    

    
