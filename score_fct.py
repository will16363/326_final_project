def score(player_score, #result of attack method):
	"""Keeps track of the player's score upon completion of the round.

	Args:
		player_score (int): The player's score before the round starts
	
	Side effects:
		Prints information to the terminal during a round of Zombie Rolls.
	
	Returns:
		new_score (int): The player's score after the completion of the round.
	"""
	survives_round = 25
	dies_to_zomb = 10
	# if the player survives the round/beats the zombie (take the result of the attack method):
		new_score = player_score + survives_round
		print(f"You earned {survives_round} points for defeating the zombie!")
	# elif the player dies to the zombie (take result of the attack method):
		new_score = player_score - dies_to_zomb
		print(f"You lost {dies_to_zomb} for dying to the zombie!")
	return new_score