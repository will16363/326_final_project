# if __name__ == "__main__":

""" Score (f-strings) """
"""def score(self, player_score, attack_results):
	Keeps track of the player's score upon completion of the round. This 
	method will use the results of the attack() method which returns 
	True or False. This method will have variables containing points for 
	beating the Zombie or losing to the Zombie. This will then add the 
	corresponding amount of points to the player's score which is being passed
	in from the previous round.

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
	file.

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
	takes the high score file and creates an empty dictionary. It then opens the
	score file and splits each line so that the player's name and score are 
	added to the dictionary. A lambda function is then used to sort and print 
	the top 5 scores to the terminal.
	
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
""" def round_fct(round_number, skip_supply="False"):
	Keeps track of the round within a game of Zombie Rolls. This method takes
	the round number from the main() method which has an initial value of 0. 
	This method then adds 1 to the round number and returns it so that the 
	round can be tracked. This method also prints messages to the terminal 
	for the player. The player has the ability to skip the supply runs, which 
	are even rounds from 0-13. If the player skips the supply run, they go 
	straight to the Zombie fight and the message that is played reflects that.
	
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
	will take the health from the Health() method and the round number from the 
	Round() method. The game is considered over if the player has no health left 
	or has defeated the final zombie at round 13. 
    
    Args:
        health (int): The health of the player expressed as an integer
        round_num (int): The round number expressed as an integer

    Returns:
        game_status (bool): The status of the game, True if the game is over, 
            otherwise False.
"""
