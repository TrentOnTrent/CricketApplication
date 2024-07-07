# Cricket Stats Application

[GitHub link](https://github.com/TrentOnTrent/CricketApplication)

Code style: PEP 8 style guide adhered to.

## Features

1. Writing ball-by-ball cricket commentary and saving stats
2. Reading previous cricket scorecards created through application and reading stats
3. Removing/editing previous games and deleting if necessary

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

## Help documentation
- To install application, open the run.sh script file, which will check to see if Python3 is installed and enable the running of the application! (If application doesn't automatically run, navigate to the src folder in terminal and use `bash run.sh` command to run file)
- No dependencies are required for this application as any packages are included in the source material
- Python3 required to run application, run.sh script will check to see if this is installed
- Application is mainly navigated by integer inputs except for main loop, which allows for "W" input for a wicket