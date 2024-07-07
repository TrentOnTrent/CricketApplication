import json
import os

from datetime import date

def load_match():
    """
    Will load json file and write to match analysis

    """
    
    path = './data'
    folder = os.fsencode(path)
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        print(f"{filename}")

def save_match(game: dict, team1: list, team2: list):
    """
    Will take data of match being played and write to json file
    
    """
    today = date.today()
    json_file = []
    json_file.append(game)
    json_file.extend(team1)
    json_file.extend(team2)
    print (json.dumps(json_file))
    filename = game["Team 1"]+ " v " + game["Team 2"] + " " + str(today)
    with open(f'./data/{filename}.json', 'w+') as out_file:
        json.dump (json_file, out_file, sort_keys = True, indent = 4, ensure_ascii = False)

