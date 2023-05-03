import os
class  UI():

    clear_screen= lambda x: os.system('cls' if os.name=='nt' else 'clear')

    def  __init__(self):
        self.clear_screen()
        self.Welcome_Menu()

    def Additional_NewLines(self, val):
        for x in range(val):
            print("\n")
    

    def Welcome_Menu(self):
        print("***************************************************************")
        print("                    WELCOME TO THE LIBRARY                     ")
        print("***************************************************************")
        self.Additional_NewLines(2)

    def Options_Menu(self):
        self.clear_screen()
        print("***************************************************************")
        print("                   WHAT WOULD YOU LIKE TO DO                   ")
        print("***************************************************************")
        self.Additional_NewLines(1)
        print("1.-Add New Book")
        print("2.-Print Books Currently in the Library")
        print("Q.-Exit")

    def Farewell_Menu(self):
        self.clear_screen()
        print("***************************************************************")
        print("                      HOPE TO SEE YOU SOON                     ")
        print("***************************************************************")
        self.Additional_NewLines(2)
    
    def New_Book_Parameters(self,str):
        self.clear_screen()
        print("***************************************************************")
        print("             New Book?: Please Enter "+str+"                   ")
        print("***************************************************************")
        self.Additional_NewLines(2)

    def Upgrade_Library(self,bookEntries:list[str]):
        self.clear_screen()
        print("***************************************************************")
        print("              YOUR LIBRARY WILL LOOK LIKE THIS                 ")
        print("---------------------------------------------------------------")
        for entry in bookEntries:
            print("            "+entry)
        print("***************************************************************")
        self.Additional_NewLines(2)

    def Print_Library(self,bookEntries:list[str]):
        self.clear_screen()
        print("***************************************************************")
        print("          THESE ARE THE BOOKS STORED IN YOUR LIBRARY           ")
        print("---------------------------------------------------------------")
        for entry in bookEntries:
            print("---"+entry+"---")
        print("***************************************************************")
        self.Additional_NewLines(2)