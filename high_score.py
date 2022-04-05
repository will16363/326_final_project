# with statements/data visualization pyplot/list sorting

def high_score(new_score):
	"""Compares the score of the player to the top 5 scores overall by creating
	   and modifying a file.

	Args:
		new_score (int): Score of the player at the end of the game.

	Side effects:
		Creates or modifies a file that high scores are kept in.
		Prints information to the terminal.
	"""
	# use with statement to create and open a file 
	# in the file, make a dictionary that keeps track of user's scores/names
	# pass the file back in and sort it
	# if the user beats one of the high scores, re-sort them
	# print the top 5 overall scores to the terminal