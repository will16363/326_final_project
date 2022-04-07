# list comprehension

def ranked_scores(score_file):
	"""Sort the high score file and returns top 5 overall scores.

	Args:
		score_file (str): File path for the high score file.

	Side effects:
		Prints information to the terminal
	"""
	high_score_dict = {}
	with open(score_file, 'r', encoding='utf-8') as f:
		for line in f:
			line.split(':')
			high_score_dict[line[0]]=line[1]
		ranked_dict=(sorted(high_score_dict, key=high_score_dict.get, 
			reverse=True)[:5])
		print(ranked_dict)

ranked_scores("scores.txt")

#want the top 5 players' names and their scores to be printed
#rn it's only printing the first letter of the first three entries in the file