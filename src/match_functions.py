class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.overs = 0
        self.overs_remaining = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.battingfirst = None
        self.wickets = 0

    def add_player(self, player):
        self.players.append(player)

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.batting = None
        self.runs = None
        self.balls = None
        self.wickets = None
        self.overs = None

def check_ball(user_input):
    """
    Checks ball user input to make sure one of possible options
    """
    list_of_correct_inputs = ["0", "1", "2", "3", "4", "6", "W"]
    while user_input not in list_of_correct_inputs:
        user_input = input("Please try again:  ")
    return user_input

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
            return user_input

def update_loop(bowler: Player, game: Game, batting_team: Team, bowling_team: Team):
    """
    Will update stats for each bowl being bowled
    """
    balls_in_over = 0
    current_batter = batting_team.players[bowling_team.wickets]
    current_batter.batting = True
    # runs until end of over, i.e = balls_in_over = 5
    while balls_in_over < 5:
        bowl_input = input("Next bowl:  ")
        bowl_input = check_ball(bowl_input)
        balls_in_over += 1
        if bowl_input == "W":
            wicket_taken()
        else:
            current_batter.runs += bowl_input
            current_batter.balls += 1
    end_of_over(bowler, game, batting_team, bowling_team)


def wicket_taken():
    """
    Will run if wicket is taken, updating batters and various stats
    """
    pass

def end_of_over(bowler, game, batting_team, bowling_team):
    """
    Will run at end of over (once no of bowls bowled = 6)
    """
    game.overs_remaining -= 1
    if game.overs_remaining == 0:
        end_of_inning()
    for index in range(0, bowling_team.players.count):
            print(f"{index+1}:  {bowling_team.players.count[index]}\n")
    current_bowler = input(f"Enter who is bowling:  ")
    check_input(current_bowler, batting_team.players.count, 1)


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

    # Setting up players on each team
    for index in range(0, int(number_of_players)):
        player = (input(f"Please enter name of player number {index + 1} for {team1.name}:  "))
        player = Player(player, team1.name)
        team1.add_player(player)
    for index in range(0, int(number_of_players)):
        player = (input(f"Please enter name of player number {index + 1} for {team2.name}:  "))
        player = Player(player, team2.name)
        team2.add_player(player)
    
    amount_of_overs = input("Enter how many overs in game:  ")
    check_input(amount_of_overs, 50, 5)
    game.overs = amount_of_overs
    game.overs_remaining = amount_of_overs

    # Setting up first team batting
    first_team = input(f"Enter which team is batting first, 1 {team1.name} or 2 {team2.name}:  ")
    check_input(first_team, 2, 1)

    if int(first_team) == 1:
        team1.battingfirst = True
        team2.battingfirst = False
        print(f"The opening batters are {team1.players[0]} and {team1.players[1]}")
    else:
        team1.battingfirst = False
        team2.battingfirst = True
        print(f"The opening batters are {team2.players[0]} and {team2.players[1]}")
    
    # Setting up first bowler
    if team1.battingfirst:
        for index in range(0, int(number_of_players)):
            print(f"{index+1}:  {team2.players[index]}\n")
        current_bowler = input(f"Enter who is bowling first:  ")
        check_input(current_bowler, int(number_of_players), 1)
        current_bowler = team2.players[int(current_bowler)]
        update_loop(current_bowler, game, team1, team2)
    else:
        for index in range(0, int(number_of_players)):
            print(f"{index+1}:  {team1.players[index]}\n")
        current_bowler = input(f"Enter who is bowling first:  ")
        check_input(current_bowler, int(number_of_players), 1)
        current_bowler = team1.players[int(current_bowler)]
        update_loop(current_bowler, game, team2, team1)
    