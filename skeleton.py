# if __name__ == "__main__":

""" Score (f-strings) """
"""def score(self, player_score, attack_results):
	Keeps track of the player's score upon completion of the round. This 
	method will use the results of the attack() method which returns 
	True (beats zombie) or False (loses to zombie). This method will have 
	variables containing points for beating the Zombie or losing to the Zombie. 
	This will then add the corresponding amount of points to the player's score 
	which is being passed in from the previous round.

	Args:
		player_score (int): The player's score before the round starts
		attack_results (bool): The result of the player attack method
	
	Side effects:
		Prints the player's score to the terminal during a round of Zombie Rolls
	
	Returns:
		new_score (int): The player's score after the completion of the round
"""


""" High Score (with statements) """
"""def high_score(player_name, new_score, score_file):
	Writes the player's score to a high score file. This method takes the 
	player's name from the game class, the player's score from the score() 
	method, and a file name. It then appends the player's name and score to the
	file. The format will be "{player_name}:{new_score}\n". Each line will 
	consist of a player's name and their score. The file will be encoded in 
	UTF-8. 

	Args:
		player_name (str): Name of the player (maybe use self.name?)
		new_score (int): Score of the player at the end of the game
		score_file (str): File path for the high score file

	Side effects:
		Writes to a file that high scores are kept in
"""


""" Ranked Score (custom list sorting using lambda) """
"""def ranked_scores(score_file):
	Sort the high score file and returns top 5 overall scores. This method 
	takes the file from the high_score() method and creates an empty dictionary. 
	It then opens the score file and splits each line that consists of a 
	player's name and score so that the player's name and score are added to 
	the dictionary. A lambda function is then used to sort and print the top 5 
	scores to the terminal. The file will be encoded in UTF-8. 
	
	Args:
		score_file (str): File path for the high score file
	
	Side effects:
		Prints the top 5 scores to the terminal from the high score file
"""


""" Music """
""" def play_music(path):
	Plays music during the game. This method opens an mp3 file and uses both 
	the playsound and glob modules to play the music during a game of Zombie
	Rolls. 
	
	Args:
		path (str): Path to the music file
	
	Side effects:
		Plays music throughout the game
"""


""" Round Method (optional parameters) """
""" def game_round(round_number, skip_supply="False"):
	Keeps track of the round within a game of Zombie Rolls. This method takes
	the round number from the main() method which has an initial value of 0. 
	This method then adds 1 to the round number and returns it so that the 
	round can be tracked. This method also prints messages to the terminal 
	for the player. The optional parameter allows the player to skip their 
	supply run if they choose to do so; these rounds are the even round from 
	0-13. If the player skips the supply run, they go straight to the Zombie 
	fight and a message is printed that reflects this.
	
	Args:
		round_number (int): The current round number
		skip_supply (str, optional): True or False; if True, the player skips 
			their supply run. Defaults to False
	
	Side effects: 
		Prints a message to the player depending on whether they choose to skip
			the supply run or not.
	
	Returns:
		round_num (int): the number correspoding to the round in the game
"""


""" Game Over Method """
"""def game_over(health, round_num):
    Determines when the game of Zombie Rolls is officially over. This method 
	will take the health from the health() method and the round number from the 
	game_round() method. The game is considered over if the player has no 
	health left or has defeated the final zombie at round 13. 
    
    Args:
        health (int): The health of the player expressed as an integer
        round_num (int): The round number expressed as an integer

    Returns:
        game_status (bool): The status of the game, True if the game is over, 
            otherwise False.
"""



"""Gathering Supplies """
"""
   Get players to roll and assign an item.
       The player will need to roll two dyes and the supplies
       the get will be depending on what number the dice rolls on.
       This logic also applies to the weapons in this game.
   Args:
       dice_roll(int): this variable represents the sum of the two dices that each player rolls
    Side Effects: Player will get a weapon or an item in their inventory
 
"""
 
"""Print Status Bar"""
"""
   returns a display depending on the players health
       This function gets the players health and keeps track of it using
       percentage represented as a bar. Each player will gain or lose a bar
       depending on how they are performing in the game. The status bar equals
       to 100.
   Returns:
       string: returns the health status bar based on the players health
    Side Effects: player health status bar is available for printing
 
"""
 
""" Game Over Method """
"""def game_over(health, round_num):
   Determines when the game of Zombie Rolls is officially over. This method
   will take the health from the health() method and the round number from the
   game_round() method. The game is considered over if the player has no
   health left or has defeated the final zombie at round 13.
  
   Args:
       health (int): The health of the player expressed as an integer
       round_num (int): The round number expressed as an integer
 
   Returns:
       game_status (bool): The status of the game, True if the game is over,
           otherwise False.
"""
 
 
""" Health function """
"""def print_status_bar(percent):
   The health function is used to keep track of the health of the player. It
   starts with a 100 and can gain health depending on your roll within
   gathering supplies function. It can also lose health depending on your
   zombie fight. The level of injury depends on the type of weapon that gets
   used.
 
   Args:
       def health_function():
  
   Returns:
       if weapon == '':
       this.player.max_health=int
"""
 
 
"""decrease health"""
"""keeps track of the health lost by each players"
   Args:
       damage(int): represents the damage the players took
   
  
   Side Effects: player loses health and if the health is 0 or less
                   the function calls the game_over() function
"""
 
"""increase_health"""
"""keeps track of the health gained by each players"
   Args:
       heal(int): represents how much the player healed
  
   Side Effects: player gains health up to 100
"""
"""use_supply"""
"""keeps track of the health gained by each players"
   Args:
       item(int): represents the supplies the player can use ranging from weapons to supplies.
  
   Side Effects: It calls the increase or decrease of health function
"""

   

