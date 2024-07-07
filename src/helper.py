def check_input(user_input, upper, lower):
    """
    Checks numerical user input against upper and lower bounds, checking for correct user input
    """
    while True:
        if user_input.isnumeric() == False:
            user_input = input("Please enter an integer:  ")
        elif int(user_input) < lower or int(user_input) > upper:
            user_input = input(f"Please enter a number only between {lower} and {upper}:  ")
        else:
            return int(user_input)