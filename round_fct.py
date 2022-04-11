# optional parameters

current_round = 7
player_input = input("Would you like to skip your supply run? Type False for no"
	" or True for yes: ")

def round_fct(round_number, skip_supply="False"):
	"""Keeps track of the round within a game of Zombie Rolls.

	Args:
		round_number (int): The current round number
		skip_supply (bool, optional): Allows the player to skip the supply run 
			round and skips straight to the Zombie fight. Defaults to False.
	
	Side effects: 
		Prints information to the terminal
	
	Returns:
		round_num (int): the number correspoding to the round in the game
	"""
	if skip_supply == "True":
		round_num = round_number + 1
		print(f"You have skipped your supply run. Now prepare for the "
			"Zombie fight!")
		return round_num
	else:
		round_num = round_number + 1
		print("You may now gather supplies!")
		return round_num
	

round_fct(current_round)

