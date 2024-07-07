from fileIO_package.fileIO import save_match
from helper_package.helper import check_input

class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.overs = 0
        self.overs_remaining = 0
    
    def __dir__(self):
        list_of_attributes = {"Team 1": self.team1.name, "Team 2": self.team2.name, "Overs in game": self.overs}
        return list_of_attributes
    
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.battingfirst = None
        self.wickets = 0

    def add_player(self, player):
        self.players.append(player)

    def __dir__(self):
        list_of_attributes = {self.players, self.wickets}
        return list_of_attributes
    
class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.batting = None
        self.runs = 0
        self.balls = 0
        self.wickets = 0
        self.overs = 0
    
    def __dir__(self):
        list_of_attributes = {"Name": self.name, "Team": self.team, "Runs": self.runs, "Balls Faced": self.balls, "Wickets taken": self.wickets, "Overs bowled": self.overs}
        return list_of_attributes

def check_ball(user_input):
    """
    Checks ball user input to make sure one of possible options
    """
    list_of_correct_inputs = ["0", "1", "2", "3", "4", "6", "W"]
    # Repeats until user gives correct input
    while user_input not in list_of_correct_inputs:
        user_input = input("Please try again:  ")
    return user_input



def update_loop(bowler: Player, game: Game, batting_team: Team, bowling_team: Team):
    """
    Will update stats for each bowl being bowled
    """
    balls_in_over = 0
    current_batter = []
    for index in range(0, len(batting_team.players)):
        if batting_team.players[index].batting == True:
            current_batter.append(batting_team.players[index])
    # runs until end of over, i.e = balls_in_over != 6
    while balls_in_over < 6:
        bowl_input = input("Next bowl:  ")
        bowl_input = check_ball(bowl_input)
        balls_in_over += 1
        if bowl_input == "W":
            current_batter[0].balls += 1
            current_batter = wicket_taken(bowler, current_batter, batting_team)
        else:
            current_batter[0].runs += int(bowl_input)
            current_batter[0].balls += 1
    end_of_over(bowler, game, batting_team, bowling_team)


def wicket_taken(bowler: Player, current_batter: list, batting_team: Team):
    """
    Will run if wicket is taken, updating batters and various stats
    """
    bowler.wickets += 1
    current_batter[0].batting = False
    out_batter = current_batter[0]
    for index in range(batting_team.players.index(out_batter) + 1, len(batting_team.players)):
        if batting_team.players[index].batting == None:
            batting_team.players[index].batting = True
            current_batter[0] = batting_team.players[index]
            return current_batter

def end_of_over(bowler: Player, game, batting_team, bowling_team):
    """
    Will run at end of over (once no of bowls bowled = 6)
    """
    bowler.overs += 1
    game.overs_remaining -= 1
    if game.overs_remaining == 0:
        end_of_inning(game, batting_team, bowling_team)
        batting_team, bowling_team = bowling_team, batting_team
    for index in range(0, len(bowling_team.players)):
            print(f"{index+1}:  {bowling_team.players[index].name}\n")
    current_bowler = input(f"Enter who is bowling:  ")
    current_bowler = check_input(current_bowler, len(batting_team.players), 1)
    current_bowler = bowling_team.players[current_bowler - 1]
    update_loop(current_bowler, game, batting_team, bowling_team)

def end_of_inning(game: Game, batting_team: Team, bowling_team: Team):
    """
    Will run if end of inning, setting up new inning 
    """

    # Checks to see if both teams have batted
    if batting_team.battingfirst == False:
        end_of_game(game)

    print ("End of inning! Swapping teams")
    game.overs_remaining = game.overs
    for player in batting_team.players:
        # Sets whoever was batting last at end of inning to not batting 
        if player.batting == True:
            player.batting = False
    print(f"The opening batters are {bowling_team.players[0].name} and {bowling_team.players[1].name}")
    # Initialising first players that are batting
    bowling_team.players[0].batting = True
    bowling_team.players[1].batting = True
    return

def end_of_game(game: Game):
    """
    Runs once both teams have batted, turns class attributes into a JSON-able list
    """
    print("End of game! Saving stats to file")
    game_attributes = game.__dir__()
    team1_players = []
    team2_players = []
    for player in game.team1.players:
        team1_players.append(player.__dir__())
    for player in game.team2.players:
        team2_players.append(player.__dir__())
    save_match(game_attributes, team1_players, team2_players)



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
    amount_of_overs = check_input(amount_of_overs, 50, 2)
    game.overs = amount_of_overs
    game.overs_remaining = amount_of_overs

    # Setting up first team batting
    first_team = input(f"Enter which team is batting first, 1 {team1.name} or 2 {team2.name}:  ")
    first_team = check_input(first_team, 2, 1)

    if first_team == 1:
        team1.battingfirst = True
        team2.battingfirst = False
        print(f"The opening batters are {team1.players[0].name} and {team1.players[1].name}")
        # Initialising first players that are batting
        team1.players[0].batting = True
        team1.players[1].batting = True
    else:
        team1.battingfirst = False
        team2.battingfirst = True
        print(f"The opening batters are {team2.players[0].name} and {team2.players[1].name}")
        # Initialising first players that are batting
        team2.players[0].batting = True
        team2.players[1].batting = True
    
    # Setting up first bowler
    if team1.battingfirst:
        for index in range(0, int(number_of_players)):
            print(f"{index+1}:  {team2.players[index].name}\n")
        current_bowler = input(f"Enter who is bowling first:  ")
        current_bowler = check_input(current_bowler, int(number_of_players), 1)
        current_bowler = team2.players[current_bowler - 1]
        update_loop(current_bowler, game, team1, team2)
    else:
        for index in range(0, int(number_of_players)):
            print(f"{index+1}:  {team1.players[index].name}\n")
        current_bowler = input(f"Enter who is bowling first:  ")
        current_bowler = check_input(current_bowler, int(number_of_players), 1)
        current_bowler = team1.players[current_bowler - 1]
        update_loop(current_bowler, game, team2, team1)
    