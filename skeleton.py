# if __name__ == "__main__":

""" Score (f-strings) """
"""def score(self, player_score, attack_results):
	Keeps track of the player's score upon completion of the round. This 
	function will use the results of the attack() method which returns 
	True or False. This function will have variables containing points for 
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
	Writes the player's score to a high score file. This function takes the 
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
	Sort the high score file and returns top 5 overall scores. This function 
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
	Plays music during the game. This function opens an mp3 file and uses both 
	the playsound and glob modules to play the music during a game of Zombie
	Rolls.
	
	Args:
		path (str): Path to the music file
	
	Side effects:
		Plays music throughout the game
"""


""" Round Function (optional parameters) """
""" def round_fct(round_number, skip_supply="False"):
	Keeps track of the round within a game of Zombie Rolls. This function takes
	the round number from the main() function which has an initial value of 0. 
	This function then adds 1 to the round number and returns it so that the 
	round can be tracked. This function also prints messages to the terminal 
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