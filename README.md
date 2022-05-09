# 326_final_project
Group INST326's Final Project for INST326 at the University of Maryland.


# Files in our Repository
### main.py 
This is our game's Python script. Use this to run the game

### music_file.mp3 
This is our game's music file. This is needed to play music throughout the duration of the game. 
This music is non-copyrighted as well

### score.txt 
This is our game's high_score file. This houses each player's name and score and is written to and read from


# How to run our game
Our game, Zombie Rolls can be run using using the command line and entering 'python3 main.py' for Mac 
and 'python main.py' for Windows. Our music and high score files can be found in the repository which are 
important to the functionality of the game. Besides from those, you will not need anything in order to run 
our game.


# How to play and interpret the outcome of the game
In our game, Zombie Rolls, you will be fighting against zombies. There are a total of 14 rounds; half are to gather 
and use supplies and the other half are for fighting the zombies. All outcomes (gathering supplies and fighting) are
dice-based. On even rounds, you will gather supplies to prepare yourself for the zombie fights. On odd rounds, you
will fight the zombies using weapons that you acquired and roll dice against the zombie. If the zombie rolls higher 
than you, you take damage which is equal to the zombie's dice roll minus yours. If you roll greater than or equal to
the zombie, you do damage based upon your weapon's strength. This round process continues until you reach the final 
round and defeat the boss zombie or until you run out of health and die. Your score is calculated based on how far 
you made it in the game and is then written to the score file. The top five overall scores are then shown to you.


# Who did what
### William Jones 
Was the main driver during team meetings. Created the play_music, round_fct (optional parameters), game_over, score (f-strings), high_score (with statements), 
and ranked_scores functions (custom list sorting with lambda functions)

### Tsion Demissie 
Created the print_status_bar, increase_health, decrease_health, use_supply, and gather_supplies functions

### Takuya Kameyama 
Created the ZombiePlayer and BossZombie classes and all of their methods (super method and __repr__)

### Patrice Shumate 
Created the main and parse_args funtions (ArgumentParser class)

### John Lehner 
Created the pandas_inventory function (pandas dataframe) as well as the Dice class and its methods (set operations and sequence unpacking)
