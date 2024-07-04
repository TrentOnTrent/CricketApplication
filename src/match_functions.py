def check_input(user_input, upper, lower):
    while True:
        if user_input.isnumeric() == False:
            user_input = input("Please enter an integer:  ")
        elif int(user_input) < lower or int(user_input) > upper:
            user_input = input(f"Please enter a number only between {lower} and {upper}:  ")
        else:
            return user_input

def update_loop():
    """
    Will update stats for each bowl being bowled
    """
    pass

def wicket_taken():
    """
    Will run if wicket is taken, updating batters and various stats
    """
    pass

def end_of_over():
    """
    Will run at end of over (once no of bowls bowled = 6)
    """

def end_of_inning():
    """
    Will run if end of inning, setting up new inning 
    """
    pass

def create_new_game():
    """
    Initialises new game and creates players/teams
    """
    print("Creating a new game!\n")
    number_of_players = input("How many players on each team:  ")

    number_of_players = check_input(number_of_players, 11, 5)
    team_1_name = input("Enter name of team 1:  ")
    team_2_name = input("Enter name of team 2:  ")
    team_1_players = []
    team_2_players = []
    
    for index in range(1, int(number_of_players)):
        team_1_players.append(input(f"Please enter name of player number {index} for {team_1_name}:  "))
    for index in range(1, int(number_of_players)):
        team_2_players.append(input(f"Please enter name of player number {index} for {team_2_name}:  "))
    
    amount_of_overs = input("Enter how many overs in game:  ")
    check_input(amount_of_overs, 50, 5)
    
    first_team = input(f"Enter which team is batting first, 1 {team_1_name} or 2 {team_2_name}:  ")
    check_input(first_team, 2, 1)

    current_batters = []
    if first_team == 1:
        current_batters = [team_1_players[0], team_1_players[1]]
    else:
        current_batters = [team_2_players[0], team_2_players[1]]
    print(f"The opening batters are {current_batters[0]} and {current_batters[1]}")
    #current_bowler = input(f"Enter who is bowling first