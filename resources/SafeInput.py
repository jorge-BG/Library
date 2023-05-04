class  SafeInput():
    ### This class acts as a wrapper for most User Inputs, handling cases in which
    ### User Input might may not be reliable or could affect program functionality

    def  __init__(self):
        pass

    @staticmethod
    def safe_input(option)->tuple[str,str]:
        userInput=input("-->  ")
        next_menu=str()
        match option:
            case "main":
                if  userInput not in ["1","2","q","Q"]:
                    input("\n\n Option not Available. Please Choose a Valid Option:  ")
                    next_menu= "main"
                else:
                    next_menu= userInput
            case "1":
                if userInput.__contains__("/"):
                    input("\n\n Invalid character / found. Please try again.\n--Press Enter to Continue--\n")
                    next_menu= "1"
                else:
                    next_menu= "Author"
            case "Author":
                if userInput.__contains__("/"):
                    input("\n\n Invalid character / found. Please try again.\n--Press Enter to Continue--\n")
                    next_menu= "Author"
                else:
                    next_menu= "ISBN"
            case "ISBN":
                if userInput.__contains__("/"):
                    input("\n\n Invalid character / found. Please try again.\n--Press Enter to Continue--\n")
                    next_menu= "ISBN"
                else:
                    try:
                        value=  int(userInput)
                    except ValueError:
                        input("\n\n ISBN Field is expected to be an Number. Please try again\n--Press Enter to Continue--\n")
                        SafeInput.safe_input("ISBN")
                    next_menu= "Year" 
            case "Year":
                if userInput.__contains__("/"):
                    input("\n\n Invalid character / found. Please try again.\n--Press Enter to Continue--\n")
                    next_menu= "Year"
                else:
                    try:
                        value=  int(userInput)
                    except ValueError:
                        print("\n\n ISBN Field is expected to be an Number. Please try again\n--Press Enter to Continue--\n")
                        SafeInput.safe_input("Year")
                    next_menu= "Upgrade"
            case "Upgrade":
                if userInput not in ["Y","y","N","n"]:
                    input("\n\n Invalid character / found. Please try again.\n--Press Enter to Continue--\n")
                    next_menu= "Upgrade"
                else:
                    next_menu= "main"
            case "2":
                next_menu="main"
        return userInput, next_menu
       