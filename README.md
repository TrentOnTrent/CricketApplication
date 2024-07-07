# Cricket Stats Application

[GitHub link](https://github.com/TrentOnTrent/CricketApplication)

Code style: PEP 8 style guide adhered to.

## Features

1. Writing ball-by-ball cricket commentary and saving stats
2. Reading previous cricket scorecards created through application and reading stats
3. Removing previous games and deleting if necessary

## Implementation plan
![An image of a Kanban board](/docs/Trello%20Board.png)
Features to be implemented include: 
- Creating "main menu" to open extra features
![An image of a Kanban board showing ball by ball functions to be implemented](./docs/Ball%20by%20Ball.png)
- Basic loop of ball by ball commentary (user input, adding/changing certain stats, user input, adding/changing certain stats)
- Creating function for end of over to swap current bowler, current batter
- Creating function for end of inning to swap teams
- Setting up game (asking for game details, team details)
![An image of a Kanban board showing writing JSON functions to be implemented](./docs/Writing%20Files.png)
- Saving stats to JSON file 
![An image of a Kanban board showing reading JSON functions to be implemented](./docs/Reading%20Files.png)
- Reading stats from JSON file

## Logic in each feature
### Ball-by-ball feature:
- Enters `create_new_game()`, asking for details of amount of players on each team, team names, creating instances of classes for team and players
- Also asks user for amount of overs, which gets saved into an instance of a Game class
- Asks user for which team is batting first, then asks user for which player is bowling first (from the other team)
- Enters `update_loop()`, which is the main loop that updates for each delivery
- Checks to see if there are any more overs left before running main loop
- If the over is done (i.e 6 balls have been bowled), then enters `end_of_over()`
- Else asks user for what happens each delivery (integer input of 0, 1, 2, 3, 4, 6 or W to represent wicket)
- If `end_of_over()` is called, checks to see if the amount of overs have been met, and runs `end_of_inning()` if so
- `end_of_over()` asks user for next bowler, to then run `update_loop()` again
- Once `end_of_inning()` is called, teams are swapped, and if both teams have batted, `end_of_game()` is called
- `end_of_game()` saves the data stored in the game, team and player classes to an object that is JSON-able

### Reviewing previous scorecards
- Enters `load_match()`, which displays to the user a list of files found in ./data folder
- Asks the user to select a scorecard to show stats of
- Based off user selection, JSON file is converted Python dictionary
- Dictionary is looped through to gather statistics on each team
- Statistics is then printed to the user

### Removing previous scorecards
- Enters `remove_match()`, which displays to the user a list of files found in ./data folder (utilising same function as `load_match()`)
- Asks the user to select a scored to delete
- Based off user selection, deletes scorecard JSON file that is selected
- Error checking utilised to determine if function succesfully runs


## Help documentation
- To install application, open the run.sh script file, which will check to see if Python3 is installed and enable the running of the application! (If application doesn't automatically run, navigate to the src folder in terminal and use `bash run.sh` command to run file)
- No dependencies are required for this application as any packages are included in the source material
- Python3 required to run application, run.sh script will check to see if this is installed
- Application is mainly navigated by integer inputs except for main loop, which allows for "W" input for a wicket