import random
from playsound import playsound
import glob
import pandas as pd


weapons = {"pistol":20, 'knife':10, 'axe':10, 'baseball bat': 10, 
            'golf club':10, 'shotgun':30}
supplies = {"water":40, 'shoes':30, 'food':40, 'medical supplies': 40, 
            'lighter':30, 'gloves':30}
score_file = 'score.txt'
music_file = "music_file.mp3"


class Dice:
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


# optional parameters (below are just test variables for round_fct())
def round_fct(round_num, skip_supply="False"):
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
        round_num += round_num + 1
        print(f"You have skipped your supply run. Now prepare for the "
              "Zombie fight!")
        return round_num
    else:
        round_num += round_num + 1
        print("You may now gather supplies!")
        return round_num


def print_status_bar(self):
    if self.player.health == 100:
        print("100% [==========]")                             
    elif self.player.health < 100 and self.player.health >= 90:
        print("90% [========= ]")
    elif self.player.health < 90 and self.player.health >= 80:
        print("80% [========  ]")
    elif self.player.health < 80 and self.player.health >= 70:
        print("70% [=======   ]")
    elif self.player.health < 70 and self.player.health >= 60:
        print("60% [======    ]")
    elif self.player.health < 60 and self.player.health >= 50:
        print("50% [=====     ]")
    elif self.player.health < 50 and self.player.health >= 40:
       print("40% [====      ]")
    elif self.player.health < 40 and self.player.health >= 30:
        print("30% [===       ]")
    elif self.player.health < 30 and self.player.health >= 20:
        print("20% [==        ]")
    elif self.player.health < 20 and self.player.health >= 10:
        print("10% [=         ]")
    elif self.player.health < 10 and self.player.health >= 0:
        print("0% [          ]")


def decrease_health(self, damage):
    if self.player.health - damage <= 0:
        self.game_over()
    else:
        self.player.health -= damage


def increase_health(self, heal):
    if self.player.health + heal >= 100:
        self.player.health = 100
    else:
        self.player.health += heal


def game_over(Player.self.health, round_num):                
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
    return Player.self.health <= 0 or round_num == 13


def use_supply(self, item):
    if item == 'pistol': 
        decrease_health(self, 20)
    elif item == 'shotgun': 
        decrease_health(self, 30)
    elif item == 'golf club': 
        decrease_health(self, 10)
    elif item == 'axe': 
        decrease_health(self, 10)
    elif item == 'baseball bat': 
        decrease_health(self, 10)
    elif item == 'watert': 
        increase_health(self, 40)
    elif item == 'shoes': 
        increase_health(self, 30)
    elif item == 'food': 
        increase_health(self, 40)
    elif item == 'medical supplies': 
        increase_health(self, 40)
    elif item == 'lighter': 
        increase_health(self, 30)
    elif item == 'gloves': 
        increase_health(self, 30)


def gather_supplies(self, Dice.roll()):
    if dice_roll == 1:
        self.player.Invetory.append(“pistol”)
    elif dice_roll == 2:
        self.player.Invetory.append(“water”)
    elif dice_roll == 3:
        self.player.Invetory.append(“knife”)
    elif dice_roll == 4:
        self.player.Invetory.append(“shoes”)
    elif dice_roll == 5:
        self.player.Invetory.append(“axe”)
    elif dice_roll == 6:
        self.player.Invetory.append(“food”)
    elif dice_roll == 7:
        self.player.Invetory.append(“baseball bat”)
    elif dice_roll == 8:
        self.player.Invetory.append(“medical supplies”)
    elif dice_roll == 9:
        self.player.Invetory.append(“golf club”)
    elif dice_roll == 10:
        self.player.Invetory.append(“lighter”)
    elif dice_roll == 11:
        self.player.Invetory.append(“shotgun”)
    elif dice_roll == 12:
        self.player.Invetory.append(“gloves”)



# health=[100]
# current_round=[7]
# weaponInventory={"Sword": 15}
# weaponInventory.update({"Sword": 15}) --> working on figuring this out
# weaponInventory["Sword"] = 15
# foodInventory={"Bread": 5}

# pandas dataframe
def pandasInventory():
    newWeapon = weaponInventory
    for key,value in newWeapon.items():
        k=key
        v=value
    weaponsDict={"Weapon": k}
    damageDict={"Weapon Damage": v}
    dfWeapon=pd.DataFrame(weaponsDict, index=[0])
    dfDamage=pd.DataFrame(damageDict, index=[0])
    food=foodInventory
    for key,value in food.items():
        a=key
        s=value
    foodDict=[{"Food":a}]
    buffDict=[{"Food Buff": s}]
    dfFood=pd.DataFrame(foodDict, index=[0])
    dfBuff=pd.DataFrame(buffDict, index=[0])
    healthData={"Health": health}
    dfHealth=pd.DataFrame(healthData, index=[0])
    roundData={"Round": current_round}
    dfRound=pd.DataFrame(roundData, index=[0])
    df1=pd.concat([dfHealth, dfRound, dfWeapon, dfDamage, dfFood,dfBuff], axis=1)
    return df1


# f-strings
def score(player_score, Zombie_Player.attack()):
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
	if Player.attack == 'True' and Zombie.attack == 'False':
		new_score = player_score + survives_round
		print(f"You earned {survives_round} points for defeating the zombie!")
    if Zombie.attack == 'True' and Player.attack == 'False':
		new_score = player_score - dies_to_zomb
		print(f"You lost {dies_to_zomb} for dying to the zombie!")
	return new_score


# with statements
def high_score(Player.self.player, new_score, score_file):
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


class Zombie_Player:
     def __init__(self):   
        """Initialize new zombie and player object."""
        self.zombie = ""
        self.player = ""
        self.player.health = {health.function.self.player.max_health}
        self.zombie.health = {health.function.self.zombie.max_health}
        self.damage = 0

    def attack(self, self.zombie, self.player):
        while self.zombie.health > 0 and self.player.health > 0:
            zombie_roll = self.zombie.DiceRoll()
            player_roll = self.player.DiceRoll()
            print(f"{self.zombie} rolled a {zombie_roll}. {self.player} rolled 
                a {player_roll}.")
            if zombie_roll > player_roll:
                self.damage = int(zombie_roll) - int(player_roll)              
                print(f'{self.player} took {self.damage} damage.')
                decrease_health(self.player, self.damage)
                print_status_bar(self)
            elif zombie_roll <= player_roll:
                self.damage = int(self.weapon) #the damage of the weapon that the player chooses to use           
                print(f'{self.zombie} took {self.damage} damage.')
                decrease_health(self.zombie, self.damage)
                print_status_bar(self)
        if self.zombie.health <= 0:
            score(player_score, 'True')
            player_input = input("Would you like to skip your supply run? Type"
               " False for no or True for yes: ")
            round_fct(round_num, player_input)
        elif self.player.health <= 0:
            p_score = score(player_score, 'False')
            high_score(self.player, p_score, score_file)
            ranked_scores(score_file)


# super() method
class BossZombie(Zombie_Player):    
    def __init__(self):
        self.boss_zombie = ""

    def __repr__(self):       # put __repr__ before super()?
    """Returns a formal representation of damage taken by the player from the special attack."""
    return (
        f"{self.player} took {roll1} damage from the first attack.\n"
        f"{self.player} took {roll2} damage from the second attack.\n"
        f"{self.player} took {roll3} damage from the third attack.\n"
        f"{self.player} took a combined total of {self.special_dmg} damage from the boss zombie attack!"
    )
    
    def attack(self, self.boss_zombie, self.player):
            roll1 = DiceRoll()    
            roll2 = DiceRoll()
            roll3 = DiceRoll()
            total_dmg = int(roll1) + int(roll2) + int(roll3)
            decrease_health(self.player, total_dmg)
            __repr__(self)
            print_status_bar(self)
            super().attack(self.boss_zombie, self.player)


def main()