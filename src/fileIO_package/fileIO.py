import json
import os

from helper_package.helper import check_input
from datetime import date

def matches():
    path = 'data/'
    folder = os.fsencode(path)
    list_of_files = []
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        list_of_files.append(filename)
    return list_of_files

def load_match():
    """
    Will load json file and write to match analysis

    """
    
    list_of_files = matches()

    for index in range(0, len(list_of_files)):
        print(f"{index + 1}:  {list_of_files[index]}")
    user_input = input("Which file would you like to open?  ")
    user_input = check_input(user_input, len(list_of_files), 1)
    selected_file = user_input - 1
    selected_file = list_of_files[selected_file]
    open_file = open(f"./data/{selected_file}")
    data = json.load(open_file)
    print(f"{data[0]["Team 1"]} vs {data[0]["Team 2"]}")



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

    print("Thank you for using the Cricket Stats Application!")
    exit(0)

def remove_matches():
    list_of_files = matches()

    for index in range(0, len(list_of_files)):
        print(f"{index + 1}:  {list_of_files[index]}")
    user_input = input("Which file would you like to remove?  ")
    user_input = check_input(user_input, len(list_of_files), 1)
    selected_file = user_input - 1
    selected_file = list_of_files[selected_file]
    os.remove(f"./data/{selected_file}")
    print("Thank you for using the Cricket Stats Application!")
    exit(0)