from match_functions_package.match_functions import create_new_game
from helper_package.helper import check_input
from fileIO_package.fileIO import load_match


def main():
    """
    Main loop, asking user to create new game or review previous games
    """
    print("Welcome to the Cricket Stats Application!\n")
    print("1. Create and track a new cricket game.\n")
    print("2. Review a previous game.\n")
    print("3. Remove/edit previous games.\n")
    print("4. Save and exit.\n")
    
    user_input = input("Please enter which feature you wish to use:  ")

    user_input = check_input(user_input, 4, 1)
    match user_input:
        case 1:
            # run create new game function
            create_new_game()
        case 2:
            # run review cricket game function
            load_match()
        case 3:
            # run remove/edit previous cricket game function
            pass
        case 4:
            # quits application
            print("Thank you for running the Cricket Stats Application")
            exit(0)

main()