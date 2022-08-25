
import json
from os.path import exists
import os
import glob
from tracemalloc import stop


# this was done purely by hand and google was never used so it might not be size-effective
def input_analyst():

    user_input = input("your input: ")
    #Return True if the string is a numeric string, False otherwise.
    if user_input.isnumeric():   
     print("Entered user_input is Integer:", user_input)
     num = int(user_input) #if its a int set num as the inputed value
    else:
     print("Entered user_input is a string") #if the inputed data is a string print so and stop the function
     return
    
    if user_input.isnumeric(): # if its a int display it's lengh
        print("The int lengh is: ",len(user_input))
        
    
    if (num % 2) == 0: # check if the number is even or odd
     print("{} is Even".format(num))
    else:
     print("{} is Odd".format(num))

    if num % 7 == 0: # check if the number is divisible by 7 without a remainder or not
         print("{} divisible by 7 without a remainder".format(num))
    else:
         print("{} isnt divisible by 7 without a remainder".format(num))


    
