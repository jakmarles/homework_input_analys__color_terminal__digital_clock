# I want to receive an input of variable and analyze it.
# print 
# 1.if it is a number or a string
# 2.in case it is a number print how long it is.
# 2.1 is it even or odd and is it divisible by 7 without a remainder


from  helper import *

def main():
#  menu 
    user_selection = ""
    while user_selection != "x":
        print("a - Input something")
        print("x - exit")
        # get the user selection
        user_selection = input("select an option: ")
        print("The user select: "+user_selection)
        # implement the user selection
        if user_selection == "a":
            input_analyst()
            break
       

if __name__ == "__main__":
    main()

