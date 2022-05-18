# 326_final_project
Group INST326's Final Project for INST326 at the University of Maryland.


# Files in our Repository
### main.py 
This is our game's Python script. Use this to run the game from the terminal.


### score.txt 
This is our game's high_score file. This houses each player's name and score and is written to and read from. 
Make sure that this file is empty with no extra spaces/lines so that an error does not occur.


# How to run our game
Our game, Zombie Rolls can be run using using the command line and entering 'python3 main.py' for Mac/Linux 
and 'python main.py' for Windows. Our high score file can be found in the repository which are 
important to the functionality of the game. Besides from those, you will not need anything in order to run 
our game.


# How to play and interpret the outcome of the game
In our game, Zombie Rolls, you will be fighting against zombies. There are a total of 14 rounds; half are to gather 
and use supplies and the other half are for fighting the zombies. All outcomes (gathering supplies and fighting) are
dice-based. On even rounds, you will gather supplies to prepare yourself for the zombie fights. On odd rounds, you
will fight the zombies using weapons that you acquired and roll dice against the zombie. If the zombie rolls higher 
than you, you take damage which is equal to the zombie's dice roll minus yours. If you roll greater than or equal to
the zombie, you do damage based upon your weapon's strength. This round process continues until you reach the final 
round and survive the boss zombie's triple attack or until you run out of health and die. Your score is calculated based 
on how far you made it in the game and is then written to the score file. The top five overall scores are then shown to you.


# Who did what
### William Jones 
Created the game_over, high_score (with statements), ranked_scores functions (custom list sorting with lambda functions),
helped create choose_supply/choose_weapon, and helped with main().

### Tsion Demissie 
Created the print_status_bar, increase_health, decrease_health, use_supply (f-strings), gather_supplies, roll_track (data visualization) functions, and helped with main().

### Takuya Kameyama 
Created the ZombiePlayer and BossZombie classes and all of their methods (super method and __repr__), helped create choose_supply/choose_weapon, and helped with main().

### Patrice Shumate 
Created the choose_weapon (list comprehension), choose_supply, Dice __init__ (set operations), and helped with main().

### John Lehner 
Created the pandas_inventory function (pandas dataframe) as well as the Dice class and its methods (sequence unpacking) and helped
with main().


# Notes for Professor/TA's:
In our repository, John is not showing up as a Contributor on the main page but he worked hard and was a big contributor
to our group. If we open the settings tab in the repository, he is listed as a Collaborator there. The data visualization 
will open seperately from VS Code in a seperate window once the game is complete.