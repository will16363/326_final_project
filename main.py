import random
from playsound import playsound
import glob

class Dice():
    def __init__(self, sides=6):
        self.sides= sides
        
    def roll(self):
        sideValue=(1, 2, 3, 4, 5, 6)
        side1, side2, side3, side4, side5, side6= sideValue
        self.sides=sideValue
        result1=random.randint(side1, side6)
        result2=random.randint(side1, side6)
        result = result1+result2
        return result
    
    def printResult(result):
        print(f"The sum of your dice rolls is {result}")


def game_over(health, round_num):
    """Determines when the game of Zombie Rolls is officially over. The game is 
       considered over if the player has no health left or has defeated the 
       final zombie at round 13.
    
    Args:
        health (int): The health of the player expressed as an integer
        round_num (int): The round number expressed as an integer

    Returns:
        game_status (bool): The status of the game, True if the game is over, 
            otherwise False.
    """
    return health == 0 or round_num == 13


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



def play_music(path):
	"""This function plays music during the game.

	Args:
		path (str): Path to the music file.

	Side effects:
		Plays music throughout the game.
	"""
	for song in glob.glob(path):
		playsound(song)
play_music("music_file.mp3")


# custom list sorting using lambda
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

# optional parameters

current_round = 7
player_input = input("Would you like to skip your supply run? Type False for no"
                     " or True for yes: ")


def round_fct(round_number, skip_supply="False"):
    """Keeps track of the round within a game of Zombie Rolls.

    Args:
    	round_number (int): The current round number
        skip_supply (str, optional): Allows the player to skip the supply run 
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
        # include the fighting round here Zombie(attack) so that it skips the
        # supply run round. 
    else:
        round_num = round_number + 1
        print("You may now gather supplies!")
        return round_num
round_fct(current_round)


# f-strings
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


# work in progress
# Create zombie list function?
"""
def create_list(num):
    zombs_list = list(['zombie' + str(n) for n in range(int(num))])
    
    return zombs_list
    """


class Zombie:
    """Action of one zombie.  In the game, the zombies will only be capable of attempting to attack the
       player once during the night round.  During the day, they wander aimlessly and are harmless. 
    
        Attributes:
            zombie (str): zombie and the number associated with the zombie (zombie#) doing the attacking.
                          For the game, there will be a list containng three zombies and each zombie will 
                          take action in the order of the index per turn as long as they are "alive".
                          To determine the status of the zombie, the health() will be called at the 
                          start of the round of each of the zombies' turns.  If their health is not 0,
                          then they will be allowed to attack.  Limited to string types.
            player (str): name of player zombie is attacking.  This is a single player game, therefore
                          only one player name will exist per game.  Limited to string types.
            player.health (int): represents the health of the player.  Set after the attacks of the zombies
                                 and after health() is called to reflect the damage done on the player.
                                 Limited to interger types to work with numbers only.
            damage (int): represents the amount of damage done by zombie.  The round() will be called to
                          determine if it's night or day.  If it's night, the DiceRoll Class 
                          will be called and the amount of damage will be determined based on a dice roll
                          of the zombie and a dice roll of the player which are automatically executed
                          per attack for both zombie and player.  The exact amount of damage done by
                          the zombie on the player will be calculted by subtracting the result of the dice
                          roll of the player from the result of the dice roll of the zombie.  For these
                          dice rolls, we will be using two 6-sided dice.  If the player's dice roll is
                          higher than the zombie's, the attack fails and damage is set to 0.
                          The health() will be called each time the player takes damage to update the
                          health of the player.  The minimum value is 0 should the player succeed in evading
                          the attack.  The maximum value is 10, which is calculated by taking the lowest 
                          roll possible of 2 and subtracting the number from the highest role possible of 12.
                          Limited to integer types to work with numbers only.
    """
    def __init__(self):   
        """Initialize new zombie object."""
        
        self.zombie = ""
        self.player = ""
        self.player.health = {health.function.self.player.max_health}
        self.damage = 0
        
    def attack(self, zombie_list, player):
        """Attack of one zombie on the player.  The method will iterate through the list of zombies, which will
        allow each zombie to attempt to attack the player one time each, as long as they are 'alive'.  
        
        Args:
            zombie_list (list of str): list containing the zombies.
            player (str): player's name.
            
        Side effects: prints statements for the dice roll results, amount of damage taken, and amount of 
                      life the player has left.
        
        Returns:
            bool: True if the attack succeeds (dice roll of zombie is higher than player's).
                  False if the attack fails (dice roll of the zombie is lower than player's).
        """
        # while loop to iterate through the zombie list and each zombie will execute attack as long as they are 'alive'.
        # I think it works?
        self.player = player
        
        count = 1
        zombie_index = 0
        zombie_num = len[zombie_list]
        
        while count < zombie_num:
            for zombie in zombie_list:
                self.zombie = zombie[zombie_index]
                
            if health_dict(zombie_list[zombie_index]) >= 0:        # check health status of zombie, maybe this works?
            # call dice_roll()
                zombie_roll = self.zombie.DiceRoll()
                player_roll = self.player.DiceRoll()
                print(f"{self.zombie} rolled a {zombie_roll}.")
                print(f"{self.player} rolled a {player_roll}.")
        
                if zombie_roll > player_roll:
                    self.damage = zombie_roll - player_roll              
                    print(f'{self.player} took {self.damage} damage.')
                    count += 1
                    zombie_index += 1
                    return True

                else:
                    print(f'{self.player} dodged the attack!.')
                    self.damage = 0
                    count += 1
                    zombie_index += 1
                    return False

            decrease_health(self.player, self.damage)                 # call health function to update health
            self.player.health = {health.self.player.max_health}
            print(f"{self.player} has {health.self.player.max_health} left.")
        
        if zombie_num == 0:
            print("There are no zombies left.  Go to next round.")
            # call round() to skip round.


class BossZombie(Zombie):
    """Action of boss zombie.  Different from regular zombie in that it first launches three consecutive
    attacks in addition to one normal zombie attack.  Appears on the final night of the game which is
    determined by using the round().  A list will be used to contain the boss zombie for the code to 
    work within the inherited attack method.
    
        Attributes:
            boss_zombie (str): boss zombie and the number associated with the boss_zombie (boss_zombie#).
                          For the game, there will be a list containing the one boss zombie and it will 
                          appear on the final night of the game, which is determined by using the round().
                          Unlike for the Zombie Class, there is no need to call the health() as it only
                          appears for one turn and will take a turn before the player, allowing it to
                           always be 'alive' to take a turn.  Limited to string types.     
            player (str): name of player zombie is attacking.  This is a single player game, therefore
                          only one player name will exist per game.  Limited to string types.
            special_dmg (int): represents the amount of total damage done by the three consecutive attacks
                               performed by the boss zombie.  Limited to integer types to work with numbers
                               only.
            damage (int): represents the amount of the 'normal zombie' attack done by the boss zombie.
                          The method will be inherited by using the super() and will iterate through the
                          boss_zombie_list as it did for the zombie_list, and go through all the rest of
                          the code to attempt to attack the player.Limited to integer types to work with 
                          numbers only.
            roll1 (int): 1st roll of the boss zombie attack.  The player is unable to evade this attack and
                         will take a damage based on a single die roll.  The minimum value is 1 and the
                         maximum value is 6, which are the lowest and highest roll possible on a regular
                         6-sided die.  Limited to integer types to work with numbers only.
            roll2 (int): 2nd roll of the boss zombie attack.  The player is unable to evade this attack and
                         will take a damage based on a single die roll.  The minimum value is 1 and the
                         maximum value is 6, which are the lowest and highest roll possible on a regular
                         6-sided die.  Limited to integer types to work with numbers only.
            roll3 (int): 3rd roll of the boss zombie attack.  The player is unable to evade this attack and
                         will take a damage based on a single die roll.  The minimum value is 1 and the
                         maximum value is 6, which are the lowest and highest roll possible on a regular
                         6-sided die.  Limited to integer types to work with numbers only.

        Side effects: prints statements for the dice roll results, amount of damage taken, and amount of 
                      life the player has left.
    """
    def __init__(self):
        """Initialize boss zombie.  There is only one boss zombie for this game."""
        
        self.boss_zombie = ""
        self.player = ""
        self.special_dmg = 0
        self.damage = 0
        self.roll1 = 0
        self.roll2 = 0
        self.roll3 = 0
        

    def attack(self, boss_zombie_list, player):
        """Boss zombie performs three consecutive attacks on player.  The attacks cannot be dodged.
        The DiceRoll Class is called for each of the three attacks and rolls a number between one and six.
        The player receives damage equivalent to the result of the dice roll and health() is called to 
        update player's health.  Super() is used to inherit the attack method from the parent Zombie Class.
        Doing so will allow the boss zombie to execute a normal zombie attack after it's special attack.
        Boss zombie is contained in a list.
        
        Args:
            boss_zombie_list (list of str): list containing the boss zombie.
            player (str): name of player.
        """
        # do while loop similar to Zombie Class to set self.boss_zombie = boss_zombie[index]
        count = 1
        boss_zombie_index = 0
        boss_zombie_num = len[boss_zombie_list]
        
        while count < boss_zombie_num:
            for boss_zombie in boss_zombie_list:
                self.boss_zombie = boss_zombie[boss_zombie_index]
            
            # No need to check for boss zombie health since it spawns last round and attacks before player.
            self.roll1 = DiceRoll()    # roll just 1 die.  so damage is 1-6 per roll.
            self.roll2 = DiceRoll()
            self.roll3 = DiceRoll()
            total_dmg = (self.roll1) + (self.roll2) + (self.roll3)
            
            self.special_dmg = total_dmg
            decrease_health(self.player, self.special_dmg)    # call health() to update
            print(f"{self.player} has {health.self.player.max_health} left.")
            count += 1
            boss_zombie_index += 1
            
        super().attack(boss_zombie_list, player)     
        # this should perform a normal zombie attack on one player by using attack method from Zombie Class.
               
    def __repr__(self):       # put __repr__ before super()?
        """Returns a formal representation of damage taken by the player from the special attack."""
        return (
            f"{self.player} took {self.roll1} damage from the first attack.\n"
            f"{self.player} took {self.roll2} damage from the second attack.\n"
            f"{self.player} took {self.roll3} damage from the third attack.\n"
            f"{self.player} took a combined total of {self.special_dmg} damage from the boss zombie attack!"
        )
        

class Player:
    """Action of player.  Attack zombies during the night and can make a selection between supply run
    or attack zombie during the day.  During the attack sequence, player chooses which zombie they would
    like to attack from the zombie_list, then the DiceRoll Class is called to initiate the dice roll for
    the player and the zombie.  
     
    Attributes:
        weapon (str): player's weapon.  Limited to string types.
        player (str): name of player.  Limited to string types.
        zombie (str): zombie the player is attacking.  Limited to string types.
        boss_zombie (str): default is set to None.  In the final round, the attribute can be set
                           to boss zombie to allow the player to select and attack.
        damage (int): amount of damage done by player using weapon; damage value is pulled from the
                      inventory dict.  Damage is set to 0 if the player's attack attempt is not succesful.
    """
    def __init__(self, player):
        """Initalize player object.
        
        Args:
            player (str): name of player.
            
        Side effects: prints statements for the dice roll results, amount of damage taken, and amount of 
                      life for the zombies/boss zombie.

        """
        self.weapon = "" 
        self.player = player
        self.player.health = {health.function.self.player.max_health}
        self.zombie = ""
        boss_zombie = ""
        self.damage = weapon_dict[self.weapon]
        
    def attack(self, zombie_list, boss_zombie_list=None):
        """Attacks of player on the zombie.  Allows player to make a weapon selection.  DiceRoll Class is
        called to determine whether the attack succeeds or not.  Attack is succesful if the result of the
        dice roll is higher than the zombie's dice roll.  If the result of the dice roll is lower, the
        attack misses.  Zombie receives full damage of the weapon upon success of attack.
        
        Args:
            zombie_list (list of str): list containing the zombies.
            boss_zombie_list (list of str): list contaiing the boss zombie.  Default set to None until
            last round.
            
        Side effects: prints statements for the dice roll results, amount of damage taken, and amount of 
                      life the zombies have left.

        Returns:
            bool: True if the attack succeeds (dice roll of player is higher than zombie's).
                  False if the attack fails (dice roll of player is lower than zombie's).
        """
        # the attack method should allow player to attack both regular zombie and boss zombie in the final
        # round if player was unable to kill all zombies by final round.
        
        if boss_zombie_list == None:
            self.boss_zombie = None
        else:
            self.boss_zombie = boss_zombie_list[0]
        
        if len(zombie_list) != 0:                     # as long as there's at least ONE zombie left...
            print(f"{len(zombie_list)} zombie(s) left.")
            print("Choose your weapon.")
            print(weapon_dict)
            weap_choice = input()                     # could also do lower.input() to make lowercase
            
            if weap_choice not in weapon_dict:
                print('Please type your weapon of choice.')
                weap_choice = input()
            else:
                self.weapon = weap_choice
            
            self.zombie = zombie_list[0]              # attack zombie in index 0
            zombie_roll = self.zombie.DiceRoll()
            player_roll = self.player.DiceRoll()
            
            if  player_roll >= zombie_roll:              
                print(f"You attacked {self.zombie} with {self.weapon}."
                      f"It took {self.damage} damage.")
                decrease_health(self.zombie, self.damage)
                print(f"{self.zombie} has {health.self.zombie.max_health} left.")
                return True

            else:
                print('The attack was unsuccesful.')
                self.damage = 0
                return False
            
        if {health.self.zombie.max_health} <= 0:
            zombie_list.pop(0)
            print(f"There are {len(zombie.list)} zombies left.")
            
        if len(zombie_list) == 0:
            print("You have defeated all zombies.  Go to next round.")
            # if there are no zombies left, then the game should not execute the entire attack method in the 1st place.
            # Because round would be skipped during the zombie's attack because they attack first.
            # I created this "if" statement as a failsafe.
            # call round() to skip round()?
            
        if self.boss_zombie != None:
            print(f"{len(boss_zombie_list)} boss zombie to defeat!")
            print("Choose your weapon.")
            print(weapon_dict)
            weap_choice = input()                     # could also do lower.input() to make lowercase
            
            if weap_choice not in weapon_dict:
                print('Please type your weapon of choice.')
                weap_choice = input()
            else:
                self.weapon = weap_choice    
            
            boss_zombie_roll = self.boss_zombie.DiceRoll()
            player_roll = self.player.DiceRoll()       
        
            if  player_roll >= boss_zombie_roll:              
                print(f"You attacked {self.boss_zombie} with {self.weapon}."
                      f"It took {self.damage} damage.")
                decrease_health(self.boss_zombie, self.damage)
                print(f"{self.boss_zombie} has {health.self.boss_zombie.max_health} left.")

            else:
                print('The attack was unsuccesful.')
                self.damage = 0
        
    def supply_run(self):    # I probably don't need to do this?
        """Supply runs can only happen during the day and if the player input is False to the question
        whether the player would like to skip the supply run during the round().  If the player does not
        skip the supply run, the gather_supply() is called to initiate supply run.  The inventory() is called
        to update it with the item found by the player.
            
        Side effects: prints statements of items found by player.
        """
        # determined by round()
        # call gather_supply()
        # prints out something like "you found [item]!"
        # adds item to dictionary, if item is already in dict, then does not get added.


weaponInventory[supply_name] = supply_value