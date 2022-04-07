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
			name, score=line.split(':')
			high_score_dict[name]=int(score)
		ranked_dict=(sorted(high_score_dict.items(), key=lambda x:x[1], 
			reverse=True)[:5])
		print(ranked_dict)

