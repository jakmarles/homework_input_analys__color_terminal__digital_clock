
from os.path import exists
from tracemalloc import stop


# this was done purely by hand and google was never used so it might not be size-effective
def input_analyst():

    user_input = input("your input: ")
    # Return True if the string is a numeric string, False otherwise.
    if user_input.isnumeric():
        print("Entered user_input is Integer:", user_input)
        num = int(user_input)  # if its an int set num as the inputed value

    else:
        # if the inputed data is a string print so and stop the function
        print("Entered user_input is a string")
        return

    if user_input.isnumeric():  # if its a int display it's lengh
        print("The int lengh is: ", len(user_input))

    if (num % 2) == 0:  # check if the number is even or odd
        print("{} is an Even number".format(num))
    else:
        print("{} is an Odd number".format(num))

    if num % 7 == 0:  # check if the number is dividable by 7 without a remainder or not and prints how much it would actually be if Divided by 7
        number1 = num
        number2 = 7
        result = number1/number2
        print("{} Dividable by 7 without a remainder".format(num))
        print("{} Dividable by 7 =: {} ".format(num, result))

    else:
        number1 = num
        number2 = 7
        result = number1/number2
        print("{} Isn't dividable by 7 without a remainder".format(num))
        print("{} Divided by 7 =: {} ".format(num, result))
