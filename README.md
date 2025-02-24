# Terminal Adventure Game

Create a terminal_game.py that walks the player through a captivating mini-game adventure! In each step of the adventure, the player should be presented with 2 or more options on where to go next.

Be as creative as you want with this, but make sure your code runs!

Some ideas include:

    A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
    A “Day in the Life” story that walks you through choices the main character makes based on conditions like the time of day, the actions that the player take, etc.
    A classic mini-RPG (role-playing game) with hp health points, character moves like attack/block/heal, and NPCs (non-player characters) that attacks based on a random number generator.

## The Game Theory

Here i will break down how the game consist, how the history will be
This is story of a young prince from Mali, who's fighting for is life with assaulters that came from another continent

### Main Characters
- The prince can attack, defend, earn points after beating an assaulter. He can also heal, quit the game if he want 
When the game start the Prince had 100 of pv(pv is how the player health will be represented in the game).

The player has three type of attack:
- Basic
- Powerfull
- Special attack
The player can receive three types attack:
- Basic
- Powerfull
- Fatal attack
## TO-DO
- Make a better game logic 
- Re-define the code
- Make a command parsers function for the game
## Suggestion
- The inputs are a little inconsistent since the player needs to use a mix of upper and lower case letters depending on the menu. You can use .lower() to help sanitize input from the player to avoid this.
- Remember to use lower_snake_case for variable names unless you are defining constants.
- Right now the game is a little unbalanced since the enemy may not get a turn.