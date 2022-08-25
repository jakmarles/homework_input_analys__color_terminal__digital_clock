# I want to display three lines in the terminal of a menu in different colors

import termcolor

def main():

    user_selection = ""
    while user_selection != "x":
        # menua
        termcolor.cprint("a - this is a green menu",'green') #text and the color of it 
        termcolor.cprint("b - this is a blue menu",'blue') #text and the color of it 
        termcolor.cprint("x - this is a red menu",'red') #text and the color of it 
        # get the user selection
        user_selection = input("select an option: ")
        print("The user select: "+user_selection)
        # implement the user selection
        if user_selection == "a": #since the fuction doesnt do anything every opinion will stop the function 
            return
        if user_selection == "b": #since the fuction doesnt do anything every opinion will stop the function 
            return
        if user_selection == "x": #since the fuction doesnt do anything every opinion will stop the function 
            return
            
       

if __name__ == "__main__":
    main()

