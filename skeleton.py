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


""" Music Function """
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


""" Gathering Supplies Method """
"""def gather_supplies(dice_roll):
   Get players to roll and assign an item. The player will need to roll two dyes
   and the supplies the get will be depending on what number the dice rolls on.
   This logic also applies to the weapons in this game.

   Args:
       dice_roll(int): this variable represents the sum of the two dices that 
       		each player rolls
    
    Side Effects: 
    	Player will get a weapon or an item in their inventory
"""
 

""" Print Status Bar """
"""def print_status_bar(percent):
	Returns a display depending on the players health. This function gets the 
	players health and keeps track of it using percentage represented by 
	individual bars ex- = is 10% == is 20%. Each player will gain or lose a bar
    depending on how they are performing in the game. The status bars add up
    to 100. There are also weapons and supplies in this game worth different
    amount of points. So the player's health level will change based on that.
   
   Args:
		percent (int): Player's health represented as an int, i.e. 10, 70, etc.

   Returns:
       health_stat_bar (str): Returns the health status bar based on the players 
       		health
    
    Side Effects: 
    	Player health status bar is available for printing
"""
 

""" Health function """
"""def health_function():
	Keeps track of the players health depending on their performance
 	
	Returns:
		if weapon == '': Each weapon and supply is worth a different amount of 
		points and this is where you plug that in. this.player.max_health=int 
		this shows what the current health of the player is depending on the 
		attack they went through or the supplies they got.
"""

""" decrease health """
"""def decrease_health(damage):
	Keeps track of the health lost by each players
   
   Args:
       damage(int): represents the damage the players took
   
   Side Effects: 
   		player loses health and if the health is 0 or less the function 
		   calls the game_over() function
"""
 
""" increase_health """
"""def increase_health(heal):
	Keeps track of the health gained by the player
  
   Args:
       heal(int): represents how much the player healed
  
   Side Effects: 
   		Player gains health up to 100
"""

""" use_supply """
"""def use_supply(item):
	Keeps track of the health gained by the player after they have used an item
	that was collected during a supply run.
   
   Args:
       item (int): represents the supplies the player can use ranging from 
       		weapons to supplies.
  
   Side Effects: 
   		Calls the increase or decrease of health function
"""

""" Dice Class """
"""A dice having 6 sides
	
 Attributes:
		sides (int): The number of sides on the dice
"""
  
""" Dice Class Roll Method """
"""def roll():	
	Picks a random integer between 1-6 and assigns it to a variable. This is 
	done again and then the two varables are added together.

	Side effects:
			Assigns a value of 1-6 to the sides
   	
    Returns: 
    	Returns the sum of the two dice rolls
"""

""" Print Result Method """
"""def print_result():
	Displays the resulting roll of the dice.

	Side effects: 
 		Prints the sum of the dice rolls to the console.
"""

""" Inventory Function (Pandas Dataframe) """
"""Viewable pandas dataframe for the player visually see what is in their 
	inventoryA CSV file in UTF-8 encoding with columns 'Weapon' (str), 'Food' 
 	(str), '\n' 'Round' (str). The first row of the file contains column 
  	headers; each subsequent row describes the item and its value. We will know
	more about how this function operates and what exactly it does once we 
	have learned about Pandas next week.
"""


""" Zombie Class """
"""class Zombie:
	Action of one zombie.  In the game, the zombies will only be capable of 
   	attempting to attack the player once during the night round. During the day, 
   	they wander aimlessly and are harmless. 
   
	Attributes:
		zombie (str): zombie and the number associated with the zombie (zombie#) 
  			doing the attacking. For the game, there will be a list containng 
     		three zombies and each zombie will take action in the order of the 
       		index per turn as long as they are "alive". To determine the status 
         	of the zombie, the health() will be called at the start of the round 
          	of each of the zombies' turns.  If their health is not 0, then they 
           	will be allowed to attack.  Limited to string types.
		player (str): name of player zombie is attacking.  This is a single 
  			player game, therefore only one player name will exist per game. 
     		Limited to string types.
		damage (int): represents the amount of damage done by zombie. The 
  			round() will be called to determine if it's night or day. 
     		If it's night, the DiceRoll Class will be called and the amount of
       		damage will be determined based on a dice roll of the zombie and a 
         	dice roll of the player which are automatically executed per attack 
          	for both zombie and player.  The exact amount of damage done by the 	
           	zombie on the player will be calculted by subtracting the result of 
            the dice roll of the player from the result of the dice roll of the 
            zombie. For these dice rolls, we will be using two 6-sided dice. If 
            the player's dice roll is higher than the zombie's, the attack fails 
            and damage is set to 0. The health() method will be called each time 
            the player takes damage to update the health of the player. The 
            minimum value is 0 should the player succeed in evading the attack. 
            The maximum value is 10, which is calculated by taking the lowest 
            roll possible of 2 and subtracting the number from the highest role
            possible of 12. Limited to integer types to work with numbers only.
"""
 
""" Zombie Init Method """
"""def __init__(self):   
	Initialize new zombie object.
		
		self.zombie = ""
		self.player = ""
		self.damage = ""
"""
          
""" Zombie Attack Method """
"""def attack(self, zombie_list, player):
	Attack of one zombie on the player.  The method will iterate through the 
 	list of zombies, which will	allow each zombie to attempt to attack the 
  	player one time each, as long as they are 'alive'.  

	Args:
		zombie_list (list of str): list containing the zombies
		player (str): player's name
		
	Side effects: 
 		Prints statements for the dice roll results, amount of damage taken, and 
   		amount of life the player has left.

	Returns:
		is_true (bool): True if the attack succeeds (dice roll of zombie is 
  			higher than player's). False if the attack fails (dice roll of the
     		zombie is lower than player's).
"""
        

""" Boss Zombie Class """
"""class BossZombie(Zombie):
    Action of boss zombie.  Different from regular zombie in that it first 
    launches three consecutive attacks in addition to one normal zombie attack. 
    Appears on the final night of the game which is determined by using the 
    round().  A list will be used to contain the boss zombie for the code to 
    work within the inherited attack method.
    
	Attributes:
		boss_zombie (str): boss zombie and the number associated with the 
  			boss_zombie (boss_zombie#). For the game, there will be a list
     		containing the one boss zombie and it will appear on the final night 
       		of the game, which is determined by using the round(). Unlike for 
         	the Zombie Class, there is no need to call the health() as it only
			appears for one turn and will take a turn before the player, 
   			allowing it to always be 'alive' to take a turn.  Limited to string 
      		types.     
		player (str): name of player zombie is attacking. This is a single 
  			player game, therefore only one player name will exist per game. 
     		Limited to string types.
		special_dmg (int): represents the amount of total damage done by the 
  			three consecutive attacks performed by the boss zombie. Limited to 
     		integer types to work with numbers only.
		damage (int): represents the amount of the 'normal zombie' attack done 
  			by the boss zombie. The method will be inherited by using the 
     		super() and will iterate through the boss_zombie_list as it did for 
       		the zombie_list, and go through all the rest of the code to attempt 
         	to attack the player.Limited to integer types to work with numbers 
          	only.
		roll1 (int): 1st roll of the boss zombie attack. The player is unable to 
  			evade this attack and will take a damage based on a single die roll.
     		The minimum value is 1 and the maximum value is 6, which are the 
       		lowest and highest roll possible on a regular 6-sided die. 
         	Limited to integer types to work with numbers only.
		roll2 (int): 2nd roll of the boss zombie attack. The player is unable to 	
  			evade this attack and will take a damage based on a single die roll. 
     		The minimum value is 1 and the maximum value is 6, which are the 
       		lowest and highest roll possible on a regular 6-sided die.
         	Limited to integer types to work with numbers only.
		roll3 (int): 3rd roll of the boss zombie attack. The player is unable to 
  			evade this attack and will take a damage based on a single die roll.  
     		The minimum value is 1 and the maximum value is 6, which are the 
       		lowest and highest roll possible on a regular 6-sided die.
         	Limited to integer types to work with numbers only.

	Side effects: prints statements for the dice roll results, amount of damage 
 		taken, and amount of life the player has left.
"""

""" Zombie Boss init Method """
"""def __init__(self):
	Initialize boss zombie. There is only one boss zombie for this game.

	Side effects:
		Initializes the boss Zombie's attributes
"""

""" Boss Zombie Attack Method """        
"""def attack(self, boss_zombie_list, player):
	Boss zombie performs three consecutive attacks on player. The attacks cannot 
 	be dodged. The DiceRoll Class is called for each of the three attacks and 
  	rolls a number between one and six. The player receives damage equivalent to 
   	the result of the dice roll and health() is called to update player's 
    health.  Super() is used to inherit the attack method from the parent Zombie 
    Class. Doing so will allow the boss zombie to execute a normal zombie attack 
    after it's special attack. Boss zombie is contained in a list.
	
	Args:
		boss_zombie_list (list of str): list containing the boss zombie
		player (str): name of player
"""     

""" Boss Zombie repr Method """	
"""def __repr__(self):
	Returns a formal representation of damage taken by the player from the 
 	boss Zombie's special attack.
  	
	Side effects: 
		Prints the formal representation of damage taken by the player from the
			boss Zombie's special attack
"""


""" Player Class """
"""class Player:
    Action of player. Attack zombies during the night and can make a selection 
    between supply run or attack zombie during the day. During the attack 
    sequence, player chooses which zombie they would like to attack from the 
    zombie_list, then the DiceRoll Class is called to initiate the dice roll for
    the player and the zombie.  
     
    Attributes:
        weapon (str): player's weapon
        player (str): name of player
        zombie (str): zombie the player is attacking
        boss_zombie (str): default is set to None. In the final round, the
        	attribute can be set to boss zombie to allow the player to select 
         	and attack.
        damage (int): amount of damage done by player using weapon; damage value 
        	is pulled from the inventory dict. Damage is set to 0 if the 
         	player's attack attempt is not succesful.
    """
    
""" Player Class init Method """
"""def __init__(self, player):
	Initalize player object.
	
	Args:
		player (str): name of player
		
	Side effects: 
 		Prints statements for the dice roll results, amount of damage taken, and 
   		amount of life for the zombies/boss zombie.
"""

""" Player Class Attack Method """
"""def attack(self, zombie_list, boss_zombie_list=None):
	Attacks of player on the zombie.  Allows player to make a weapon selection.  
 	DiceRoll Class is called to determine whether the attack succeeds or not.
  	Attack is succesful if the result of the dice roll is higher than the 
   	zombie's dice roll.  If the result of the dice roll is lower, the attack 
    misses. Zombie receives full damage of the weapon upon success of attack.
	
	Args:
		zombie_list (list of str): list containing the zombies
		boss_zombie_list (list of str): list contaiing the boss zombie. 
  		Default set to None until last round.
		
	Side effects:
 		Prints statements for the dice roll results, amount of damage taken, and 
   		amount of life the zombies have left.

	Returns:
		is_true (bool): True if the attack succeeds (dice roll of player is 
  			higher than zombie's). False if the attack fails (dice roll of 
     		player is lower than zombie's).
"""
        

""" Supply Run Method """
"""def supply_run(self):
	Supply runs can only happen during the day (even rounds) and if the player 
	input is False to the question whether the player would like to skip the 
	supply run during the round() method.  If the player does not skip the 
	supply run, the gather_supply() method is called to initiate supply run. 
	The inventory() method is called to update it with the item found by the 
	player.
		
	Side effects:
 		Prints statements of items found by player. Adjusts inventory dict.
"""        


""" Main Game Function"""
"""def __main__(playerName,supplyChoice,weaponChoice):
	Runs a game of Zombie Rolls.

	Args:
		playerName (str): name of player
		supplyChoice(bool): whether player choices to re-supply or not
		weaponChoice(str): players choosen weapon	

	Side Effects:
		High score board will be printed to the terminal. Player and zombies' 
		health will be printed to the terminal in the form of strings. The 
		current round number will be printed as an int. Dice roll results will 
		be printed to the terminal. Damage taken to the player will be printed
"""

""" ArgumentParser Function	"""
"""def parse_args(argList):
	Parse command line arguments. 3 arguments are expected (this number may 
	grow). Players name, supply skip option, and players weapon choice. 

	Args:
		argsList (list of str): List of arguments the user will insert into the 
			command line terminal

	Returns:
		namespace: containts a name attribute for the name of the player as a 
			string,  
	"""
