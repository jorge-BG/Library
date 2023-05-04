import os
class  UI():
    ##  This class contains UI Menus and most of the UI Printing actions.

    clear_screen= lambda x: os.system('cls' if os.name=='nt' else 'clear')

    def  __init__(self):
        self.clear_screen()
        self.Welcome_Menu()

    def Additional_NewLines(self, val):
        for x in range(val-1):
            print("\n")
    

    def Welcome_Menu(self):
        print("***************************************************************")
        print("                    WELCOME TO THE LIBRARY                     ")
        print("***************************************************************")
        self.Additional_NewLines(2)

    def options_menu(self):
        self.clear_screen()
        print("***************************************************************")
        print("                   WHAT WOULD YOU LIKE TO DO                   ")
        print("***************************************************************")
        self.Additional_NewLines(1)
        print("1.-Add New Book")
        print("2.-Print Books Currently in the Library")
        print("Q.-Exit")
        self.Additional_NewLines(1)

    def farewell_menu(self):
        self.clear_screen()
        print("***************************************************************")
        print("                      HOPE TO SEE YOU SOON                     ")
        print("***************************************************************")
        self.Additional_NewLines(2)
    
    def new_book_parameters(self,str):
        self.clear_screen()
        print("***************************************************************")
        print("             New Book?: Please Enter "+str+"                   ")
        print("***************************************************************")
        self.Additional_NewLines(2)

    def upgrade_library(self,bookEntries:list[str],bookFound):
        self.clear_screen()
        print("***************************************************************")
        print("              YOUR LIBRARY WILL LOOK LIKE THIS                 ")
        print("---------------------------------------------------------------")
        for entry in bookEntries:
            print("*--"+entry+"--*\n")
        print("***************************************************************")
        self.Additional_NewLines(1)
        if bookFound:
            print("WARNING!! This operation will overwrite book with matching ISBN\n")
        print("Are you sure you want to upgrade the library? (Y/n):  ")
        self.Additional_NewLines(2)

    def print_library(self,bookEntries:list[str]):
        self.clear_screen()
        print("***************************************************************")
        print("          THESE ARE THE BOOKS STORED IN YOUR LIBRARY           ")
        print("---------------------------------------------------------------")
        for entry in bookEntries:
            print("*--"+entry+"--*\n")
        print("***************************************************************")
        input("                Press Enter to Continue                        ")
        self.Additional_NewLines(2)