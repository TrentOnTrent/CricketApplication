class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.overs = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.battingfirst = None

    def add_player(self, player):
        self.players.append(player)

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

class Batter(Player):
    def __init__(self):
        self.runs = 0
        self.balls = 0


def check_input(user_input, upper, lower):
    while True:
        if user_input.isnumeric() == False:
            user_input = input("Please enter an integer:  ")
        elif int(user_input) < lower or int(user_input) > upper:
            user_input = input(f"Please enter a number only between {lower} and {upper}:  ")
        else:
            return user_input

def update_loop(bowler, game, team1, team2):
    """
    Will update stats for each bowl being bowled
    """
    balls_in_over = 0

    while balls_in_over < 6:
        bowl_input = input("Next bowl:  ")


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
    team1 = Team(team_1_name)
    team_2_name = input("Enter name of team 2:  ")
    team2 = Team(team_2_name)
    game = Game(team1, team2)

    for index in range(0, int(number_of_players)):
        team1.add_player(input(f"Please enter name of player number {index + 1} for {team1.name}:  "))
    for index in range(0, int(number_of_players)):
        team2.add_player(input(f"Please enter name of player number {index + 1} for {team2.name}:  "))
    
    amount_of_overs = input("Enter how many overs in game:  ")
    check_input(amount_of_overs, 50, 5)
    game.overs = amount_of_overs

    first_team = input(f"Enter which team is batting first, 1 {team1.name} or 2 {team2.name}:  ")
    check_input(first_team, 2, 1)

    current_batters = []
    if int(first_team) == 1:
        team1.battingfirst = True
        team2.battingfirst = False
        print(f"The opening batters are {team1.players[0]} and {team1.players[1]}")
    else:
        team2.battingfirst = True
        team1.battingfirst = False
        print(f"The opening batters are {team1.players[0]} and {team1.players[1]}")
    
    if team1.battingfirst:
        for index in range(0, int(number_of_players)):
            print(f"{index+1}:  {team2.players[index]}\n")
        current_bowler = input(f"Enter who is bowling first:  ")
        check_input(current_bowler, int(number_of_players), 1)
    else:
        for index in range(0, int(number_of_players)):
            print(f"{index+1}:  {team1.players[index]}\n")
        current_bowler = input(f"Enter who is bowling first:  ")
        check_input(current_bowler, int(number_of_players), 1)
    update_loop(current_bowler, game, team1, team2)