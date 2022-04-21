# with statements

def high_score(player_name, new_score, score_file):
	"""Writes the player's score to a high score file.

	Args:
		new_score (int): Score of the player at the end of the game.
		player_name (str): Name of the player (maybe use self.name?)
		score_file (str): File path for the high score file.

	Side effects:
		Modifies a file that high scores are kept in.
	"""
	with open(score_file, 'a') as f:
		f.write(f'{player_name}:{new_score}\n')