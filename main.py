import random
from playsound import playsound
import glob
import pandas as pd
from unittest import result


weapons = [{"pistol":20, 'knife':10, 'axe':10, 'baseball bat': 10, 
            'golf club':10, 'shotgun':30}]
supplies = [{"water":40, 'shoes':30, 'food':40, 'medical supplies': 40, 
            'lighter':30, 'gloves':30}]
player_weapons = []
player_supplies = []
score_file = 'score.txt'
music_file = "music_file.mp3"


class Dice():
    #set operations
    def __init__(self, sides):
        self.sides= sides
        sides=()
        sides.update(6)
     
    #Sequence unpacking   
    def roll(self):
        sideValue=(1, 2, 3, 4, 5, 6)
        side1=sideValue[0]
        side6=sideValue[5]
        result1=random.randint(side1, side6)
        result2=random.randint(side1, side6)
        result = result1+result2
        return result


def play_music(path):
	"""This function plays music during the game.

	Args:
		path (str): Path to the music file.

	Side effects:
		Plays music throughout the game.
	"""
	for song in glob.glob(path):
		playsound(song)


# optional parameters
def round_fct(round_num, skip_supply="False"):
    """Keeps track of the round within a game of Zombie Rolls.

    Args:
    	round_number (int): The current round number
        skip_supply (str, optional): Allows the player to skip the supply run 
                round and skips straight to the Zombie fight. Defaults to False.

    Side effects: 
        Prints information to the terminal.

    Returns:
        round_num (int): The number correspoding to the round in the game.
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


def print_status_bar(Zombie_Player):
    if Zombie_Player.player_health == 100:
        print("100% [==========]")                             
    elif Zombie_Player.player_health < 100 and Zombie_Player.player_health >= 90:
        print("90% [========= ]")
    elif Zombie_Player.player_health < 90 and Zombie_Player.player_health >= 80:
        print("80% [========  ]")
    elif Zombie_Player.player_health < 80 and Zombie_Player.player_health >= 70:
        print("70% [=======   ]")
    elif Zombie_Player.player_health < 70 and Zombie_Player.player_health >= 60:
        print("60% [======    ]")
    elif Zombie_Player.player_health < 60 and Zombie_Player.player_health >= 50:
        print("50% [=====     ]")
    elif Zombie_Player.health < 50 and Zombie_Player.player_health >= 40:
       print("40% [====      ]")
    elif Zombie_Player.player_health < 40 and Zombie_Player.player_health >= 30:
        print("30% [===       ]")
    elif Zombie_Player.player_health < 30 and Zombie_Player.player_health >= 20:
        print("20% [==        ]")
    elif Zombie_Player.player_health < 20 and Zombie_Player.player_health >= 10:
        print("10% [=         ]")
    elif Zombie_Player.player_health < 10 and Zombie_Player.player_health >= 0:
        print("0% [          ]")


def decrease_health(Zombie_Player, damage):
    if Zombie_Player.player_health - damage <= 0:
        game_over()
    else:
        Zombie_Player.player.health -= damage
    if Zombie_Player.zombie_health - damage <= 0:
        Zombie_Player.zombie_health = 0
        

def increase_health(Zombie_Player, heal):
    if Zombie_Player.player_health + heal >= 100:
        Zombie_Player.player_health = 100
    else:
        Zombie_Player.player_health += heal


def game_over(Zombie_Player, round_num):                
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
    return Zombie_Player.player_health <= 0 or round_num == 13


def use_supply(Zombie_Player, item):
    if item == 'water': 
        increase_health(Zombie_Player, 40)
    elif item == 'shoes': 
        increase_health(Zombie_Player, 30)
    elif item == 'food': 
        increase_health(Zombie_Player, 40)
    elif item == 'medical supplies': 
        increase_health(Zombie_Player, 40)
    elif item == 'lighter': 
        increase_health(Zombie_Player, 30)
    elif item == 'gloves': 
        increase_health(Zombie_Player, 30)


def gather_supplies(Zombie_Player, Dice):
    if Dice.roll() == 1:
        player_weapons.append({'water':0})
    elif Dice.roll() == 2:
        player_supplies.append({'water':40})
    elif Dice.roll() == 3:
        player_weapons.append({'knife':10})
    elif Dice.roll() == 4:
        player_supplies.append({'shoes':30})
    elif Dice.roll() == 5:
        player_weapons.append({'axe':10})
    elif Dice.roll() == 6:
        player_supplies.append({'food':40})
    elif Dice.roll() == 7:
        player_weapons.append({'baseball bat':10})
    elif Dice.roll() == 8:
        player_supplies.append({'medical supplies':40})
    elif Dice.roll() == 9:
        player_weapons.append({'golf club':10})
    elif Dice.roll() == 10:
        player_supplies.append({'lighter':30})
    elif Dice.roll() == 11:
        player_weapons.append({'shotgun':30})
    elif Dice.roll() == 12:
        player_supplies.append({'gloves':30})

# pandas dataframe
def pandasInventory(Zombie_Player, round_num):
    inventory = {"Player Health":Zombie_Player.health, "Current Round": round_num, 
             "Weapon": player_weapons, "Items": player_supplies}
    pandasInv=pd.DataFrame.from_dict(inventory, orient='index')
    pandasInv=pandasInv.transpose()
    return pandasInv


# f-strings
def score(player_score, true_false):
    """Keeps track of the player's score upon completion of the round.

    Args:
        player_score (int): The player's score before the round starts
        true_false (str): A string representing true if the player defeats the
            zombie and false if they die

    Side effects:
        Prints information to the terminal during a round of Zombie Rolls.

    Returns:
        new_score (int): The player's score after the completion of the round.
    """
    survives_round = 25
    dies_to_zomb = 50
    if true_false == 'True':
        new_score = player_score + survives_round
        print(f"You earned {survives_round} points for defeating the zombie!")
    if true_false == 'False':
        new_score = player_score - dies_to_zomb
        print(f"You lost {dies_to_zomb} for dying to the zombie!")
    return new_score


# with statements
def high_score(Zombie_Player, new_score, score_file):
    """Writes the player's score to a high score file.

    Args:
        new_score (int): Score of the player at the end of the game.
        player_name (str): Name of the player (maybe use self.name?)
        score_file (str): File path for the high score file.

    Side effects:
        Modifies a file that high scores are kept in.
    """
    with open(score_file, 'a') as f:
        f.write(f'{Zombie_Player.player}:{new_score}\n')


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
    def __init__(self, player, zombie, chosen_weapon):   
        """Initialize new zombie and player object."""
        self.zombie = player      # need to determine how this is set.  Need to be passed thru in parameter?
        self.player = zombie      # need to determine how this is set.  
        self.player_health = 100
        self.zombie_health = 25
        self.damage = 0
        self.weapon = chosen_weapon

    def attack(self):
        while self.zombie_health > 0 and self.player_health > 0:
            zombie_roll = self.zombie.DiceRoll()
            player_roll = self.player.DiceRoll()
            print(f"{self.zombie} rolled a {zombie_roll}. {self.player} rolled "
                "a {player_roll}.")
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
            print(f"You have beaten the Zombie!")
            player_input = input("Would you like to skip your supply run? Type"
                " False for no or True for yes: ")
            round_fct(round_num, player_input)
        elif self.player.health <= 0:
            p_score = score(player_score, 'False')
            high_score(self.player, p_score, score_file)
            ranked_scores(score_file)


# super() method + repr
class BossZombie(Zombie_Player):    
# take out __init__ because we need to use same attributes as parent class.  Automatically inherited from parent class.
# boss zombie will just inherit all attributes w/o overriding
# No need for boss zombie attribute because boss zombie will just be set to regular zombie attribute.  
# This works because only boss zombie present in last round.

    def __repr__(self):   
        """Returns a formal representation of damage taken by the player from 
            the special attack."""
        return (
            f"{self.player} took {roll1} damage from the first attack.\n"        # roll not defined.
            f"{self.player} took {roll2} damage from the second attack.\n"
            f"{self.player} took {roll3} damage from the third attack.\n"
            f"{self.player} took a combined total of {self.damage} damage " 
                "from the boss zombie attack!"
            )   
    
    def attack(self):
        roll1 = Dice.roll()    
        roll2 = Dice.roll()
        roll3 = Dice.roll()
        total_dmg = int(roll1) + int(roll2) + int(roll3)
        decrease_health(self.player, total_dmg)
        print(repr(self))
        print_status_bar(self)
        super().attack()

def main():