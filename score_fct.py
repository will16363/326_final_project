def score(player_score, ):
	"""Keeps track of the player's score upon completion of the round.

	Args:
		player_score (int): The player's score before the round starts
	
	Returns:
		new_score (int): The player's score after the completion of the round.
	"""
	survives_round = 25
	dies_to_zomb = -10
	# if the player survives the round/beats the zombie (take the result of the attack method):
		new_score = player_score + survives_round
	# elif the player dies to the zombie (take result of the attack method):
		new_score = player_score + dies_to_zomb
	return new_score