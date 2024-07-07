import json
from datetime import date

def load_match():
    """
    Will load json file and write to match analysis

    """
    
    pass

def save_match(game: dict, team1: list, team2: list):
    """
    Will take data of match being played and write to json file
    
    """
    today = date.today()
    json_file = []
    json_file.extend(game)
    json_file.extend(team1)
    json_file.extend(team2)
    print (json.dumps(json_file))
    filename = game["Team 1"] + " v " + game["Team 2"] + " " + str(today)
    with open('./data/matches.json', 'w') as out_file:
        json.dump (json_file, out_file, sort_keys = True, indent = 4, ensure_ascii = False)

