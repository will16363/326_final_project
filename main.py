import random
import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot as plt
from matplotlib import use
from pytest import Item
from unittest import result


player_weapons = [{"fist": 5}]
player_supplies = []
score_file = 'score.txt'


class Dice():
    """A dice object which has 6 sides
    
    Attributes:
        sides (set): the sides of the dice
    """
    #set operations 1
    def __init__(self, sides=[0]):
        """Initializes the sides attribute of the dice"""
        self.sides= sides
        x1={1,2,3}
        x2={4,5,6}
        sides.append(x1.union(x2))
     
    #Sequence unpacking 2
    def roll(self):
        """Takes the value of two random sides and returns the sum
        
        Side effects:
            appends the resulting sum of the two sides to the roll values list
            
        Returns: 
            Returns the sum of the two dice sides
        """
        sideValue=(1, 2, 3, 4, 5, 6)
        side1=sideValue[0]
        side6=sideValue[5]
        result1=random.randint(side1, side6)
        result2=random.randint(side1, side6)
        result = result1+result2
        return result

    # data visualization
    def roll_track(self, result):
        """Each time the dice is rolled, the summary value is appeneded
            to a pandas dataframe and plots the roll on a scatterplot
        
        Returns: 
            Returns the scatterplot of the dataframe
        """
        d = {"Roll Number":[i for i in range(100)], "Roll Value": result}
        rollplot=pd.DataFrame.from_dict(d, orient='index')
        rollplot=rollplot.transpose()
        return rollplot.plot.scatter('Roll Number', y = 'Roll Value')


def game_over(ZombiePlayer, round_num):                
    """Determines when the game of Zombie Rolls is officially over. The game is 
       considered over if the player has no health left or has defeated the 
       final zombie at round 13
    
    Args:
        health (int): The health of the player expressed as an integer
        round_num (int): The round number expressed as an integer
    
    Returns:
        game_status (bool): The status of the game, True if the game is over, 
            otherwise False.
    """
    return ZombiePlayer.player_health <= 0 or round_num < 14



# needs docstrings
def gather_supplies(d):
    """Get players to roll and assign an item. The player will need to roll two 
    dyes and the supplies the get will be depending on what number the dice 
    rolls on. This logic also applies to the weapons in this game.
  
    Args:
        d (dice instance): this variable represents an instance of the dice class
   
   Side Effects: 
        Player will get a weapon or an item in their inventory and a message
            will be printed to the terminal
   """
    roll = d.roll()
    if roll == 1:
        player_weapons.append({'brass knuckles:25'})
        print("You gathered brass knuckles!")
    elif roll == 2:
        player_supplies.append({'water':40})
        print("You gathered water!")
    elif roll == 3:
        player_weapons.append({'knife':10})
        print("You gathered a knife!")
    elif roll == 4:
        player_supplies.append({'shoes':30})
        print("You gathered shoes!")
    elif roll == 5:
        player_weapons.append({'axe':10})
        print("You gathered an axe!")
    elif roll == 6:
        player_supplies.append({'food':40})
        print("You gathered food!")
    elif roll == 7:
        player_weapons.append({'baseball bat':10})
        print("You gathered a baseball bat!")
    elif roll == 8:
        player_supplies.append({'medical supplies':40})
        print("You gathered medical supplies!")
    elif roll == 9:
        player_weapons.append({'golf club':10})
        print("You gathered a golf club!")
    elif roll == 10:
        player_supplies.append({'lighter':30})
        print("You gathered a lighter!")
    elif roll == 11:
        player_weapons.append({'shotgun':30})
        print("You gathered a shotgun!")
    elif roll == 12:
        player_supplies.append({'gloves':30})
        print("You gathered gloves!")


# f strings 3
def use_supply(ZombiePlayer, item):
    """Heals the player's health depending on what healing item they choose to
        use

    Args:
        ZombiePlayer (class): The ZombiePlayer class
        item (str): The item that the player has chosen to heal with

    Side effects:
        Prints which item the player used to heal and how much health was restored
    """
    if item == 'water': 
        ZombiePlayer.increase_health(40)
        print(f"You used {item} and gained 40 health!")
    elif item == 'shoes': 
        ZombiePlayer.increase_health(30)
        print(f"You used {item} and gained 30 health!")
    elif item == 'food': 
        ZombiePlayer.increase_health(40)
        print(f"You used {item} and gained 40 health!")
    elif item == 'medical supplies': 
        ZombiePlayer.increase_health(40)
        print(f"You used {item} and gained 40 health!")
    elif item == 'lighter': 
        ZombiePlayer.increase_health(30)
        print(f"You used {item} and gained 30 health!")
    elif item == 'gloves': 
        ZombiePlayer.increase_health(30)
        print(f"You used {item} and gained 30 health!")



def choose_supply(player_supplies):
    """Prompts the user to choose an item to heal their health.

    Args:
        player_supplies (list of dicts): A list of dictionaries that house each
            healing item that the player has in their inventory

    Returns:
        healing_item (str): The healing item that the player has chosen to use
    """
    healing_item = input("Choose an item to use to heal yourself or None if you"
        " have not gathered any items: ")
    return healing_item


# pandas dataframe 4
def pandasInventory(ZombiePlayer, round_num):
    """Dataframe that tracks the players current health, current round, 
        weapons, and items
        
    Args:
        ZombiePlayer (class): One round of action for zombie and player
        round_num (int): The round number
        
    Returns: 
        The dataframe
    
    Side effects:
        Prints the dataframe so that the player can see what they have in their
            inventory
    """
    inventory = {"Player Health": ZombiePlayer.player_health, "Current Round": round_num, 
             "Weapons": player_weapons, "Items": player_supplies}
    pandasInv=pd.DataFrame.from_dict(inventory, orient='index')
    print(pandasInv)


# list comprehension 5
def choose_weap(player_weapons):
    """Prompts the user to choose a weapon from their inventory

    Args:
        player_weapons (list of dicts): A list of dictionaries that house each
            weapon that the player has in their inventory

    Returns:
        weapon_damage (int): The player's chosen weapon's damage expressed as 
            an int
    """
    weapon = input("Choose your weapon: ")
    chosen_weapon = [weap[weapon] for weap in player_weapons if weapon in weap]
    weapon_damage = chosen_weapon[0]
    return int(weapon_damage)


# with statements 6
def high_score(player, new_score, score_file):
    """Writes the player's score to a high score file.
    
    Args:
        new_score (int): Score of the player at the end of the game.
        player_name (str): Name of the player (maybe use self.name?)
        score_file (str): File path for the high score file.
    
    Side effects:
        Modifies a file that high scores are kept in.
    """
    with open(score_file, 'a') as f:
        f.write(f'{player}:{new_score}')


# custom list sorting using lambda 7
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
            high_score_dict[name]=score
        ranked_dict=(sorted(high_score_dict.items(), key=lambda x:x[1], 
            reverse=True)[:5])
        print(f"These are the top 5 overall scores: \n {ranked_dict}")


class ZombiePlayer:
    """One round of action for zombie and player.
    
    Attributes:
        zombie (str): name of zombie.
        player (str): name of player.
        player_health (int): health of player.
        zombie_health (int): health of zombie.
        damage (int): damage to be taken by zombie or player.
        weapon (str): name of weapon selected by player.
        self.zombie_roll (int): result of dice roll; default set to 0.
        self.player_roll (int): result of dice roll; default set to 0.
    """    
    def __init__(self, zombie, player, player_health, zombie_health):   
        """Initialize new zombie and player object."""
        self.zombie = zombie     
        self.player = player      
        self.player_health = player_health
        self.zombie_health = zombie_health
        self.damage = 0
        self.zombie_roll = 0   
        self.player_roll = 0   

    def attack(self, item, player_score, score_file):
        """Attack action for both player and zombie.
        
        Side effects:
            prints statements on the terminal.
        """
        while self.zombie_health > 0 and self.player_health > 0:
            zombie_roll = Dice.roll(self)
            player_roll = Dice.roll(self)
            print(f"{self.zombie} rolled a {zombie_roll}. {self.player} rolled a {player_roll}.")
            if zombie_roll > player_roll:
                zomb_damage = int(zombie_roll) - int(player_roll)              
                self.human_decrease_health(zomb_damage)
                print(f'{self.player} took {zomb_damage} damage. {self.player} has {self.player_health} health remaining!')
                self.print_status_bar()
                input("Press c to continue...")
            elif zombie_roll <= player_roll:        
                self.zomb_decrease_health(item)
                print(f'{self.zombie} took {item} damage. {self.zombie} has {self.zombie_health} health remaining!')
        if self.zombie_health <= 0:
            self.zombie_health = 25
            return player_score
        elif self.player_health <= 0:
            high_score(self.player, player_score, score_file)
            ranked_scores(score_file)

   
    def human_decrease_health(self, damage):
        """Decrease the player's health based on the Zombie's dice roll.

        Args:
            damage (int): The difference of the Zombie and player's dice roll
                expressed as an int
        
        Side effects:
            Decreases player_health variable.
        """
        if self.player_health - damage <= 0:
            self.player_health = 0
        else:
            self.player_health -= damage
        
   
    def increase_health(self, heal):
        """This keeps track of the health gained by each player. Player is able to 
        collect supplies throughout the game such as water, food, shoes and so on. 
        Then they collect these things this their health points have increased.

        Args:
     	    heal(int): represents how much the player healed based on the 
        	    supplies they were able to collect.
    
        Side Effects: 
     	    player gains health up to 100
        """
        if self.player_health + heal >= 100:
            self.player_health = 100
        else:
            self.player_health += heal

  
    def zomb_decrease_health(self, damage):
        """This keeps track of the health lost by each player.
        There are different types of weapons in this games such as bats
        and shotgun. WIth this we will be able to see how much points
        were lost depending on the tool they used to attack.
    
        Args:
        damage(int): represents the damage the players took due to an attack.
    
        Side Effects: player loses health and if the health is 0 or less
                    the function calls the game_over() function
        """
        if self.zombie_health - damage <= 0:
            self.zombie_health = 0
        else:
            self.zombie_health -= damage
            
  
    def print_status_bar(self): 
        """This function gets the players health and keeps track of it using
        percentage represented by individual bars ex- = is 10% == is 20%. Each 
        player will gain or lose a bar depending on how they are performing in the 
        game. The status bars add up to 100. There are also weapons and supplies 
        in this game worth different amount of points. So the player's health 
        level will change based on that.
        
        Side effects:
            player's health is printed throughout the game 
        """
        if self.player_health == 100:
            print("100% [==========]")                             
        elif self.player_health < 100 and self.player_health >= 90:
            print("90% [========= ]")
        elif self.player_health < 90 and self.player_health >= 80:
            print("80% [========  ]")
        elif self.player_health < 80 and self.player_health >= 70:
            print("70% [=======   ]")
        elif self.player_health < 70 and self.player_health >= 60:
            print("60% [======    ]")
        elif self.player_health < 60 and self.player_health >= 50:
            print("50% [=====     ]")
        elif self.player_health < 50 and self.player_health >= 40:
            print("40% [====      ]")
        elif self.player_health < 40 and self.player_health >= 30:
            print("30% [===       ]")
        elif self.player_health < 30 and self.player_health >= 20:
            print("20% [==        ]")
        elif self.player_health < 20 and self.player_health >= 10:
            print("10% [=         ]")
        elif self.player_health < 10 and self.player_health >= 0:
            print("0% [          ]")


class BossZombie(ZombiePlayer):
    """One round of action for boss zombie.
    
    Attributes:
        self.roll1 (int): 1st damage from boss zombie's special attack.
        self.roll2 (int): 2nd damage from boss zombie's special attack.
        self.roll3 (int): 3rd damage from boss zombie's special attack.
    """
    def __init__(self, zombie, player, player_health, zombie_health):
        """Initialize new boss zombie object.
        
        Args:
            player (str): name of player.
            zombie (str): name of zombie.
            chosen_weapon (str): name of weapon selected by player.
        """
        super().__init__(zombie, player, player_health, zombie_health)
        self.roll1 = 0
        self.roll2 = 0
        self.roll3 = 0

    # __repr__() 8
    def __repr__(self):   
        """Returns a formal representation of damage taken by the player from 
            the special attack."""
        return (
            f"1st attack: {self.roll1} damage dealt to {self.player}.\n"        
            f"2nd attack: {self.roll2} damage dealt to {self.player}.\n"
            f"3rd attack: {self.roll3} damage dealt to {self.player}.\n"
            f"Total damage: {self.roll1 + self.roll2 + self.roll3}." 
            )   
    
    # super() method 9
    def attack(self):
        """Special attack action of boss zombie followed by attack method of 
            parent class.
        
        Side effects:
            prints statements and repr on terminal.
        """ 
        self.roll1 = Dice.roll(self)    
        self.roll2 = Dice.roll(self)
        self.roll3 = Dice.roll(self)
        damage = int(self.roll1) + int(self.roll2) + int(self.roll3)
        super().human_decrease_health(damage)
        print(repr(self))
        super().print_status_bar()
        input("Press c to continue...")
        if self.player_health <=0:
            return True
        else:
            self.zombie_health = 0
            print(f"Congratulations, you survived a week in Zombie Rolls and killed the final boss!")
            

def main(): 
    """The main driver of a game of Zombie Rolls.

    Side effects:
        Changes the round_num, player_score, player_health, and zombie_health
            variables. Creates an instance of the ZombiePlayer class. Modifies 
            the score file using high_score(). Prints important game information
            to the terminal.
    """
    print("Welcome to Zombie Rolls!")  
    player = input("Enter your name: ")
    zombie = 'Zombie'
    round_num = 0
    player_score = 0
    player_health = 100
    zombie_health = 25
    game = ZombiePlayer(zombie, player, player_health, zombie_health)
    while game_over(game, round_num) != False:
        if round_num == 13:
            player_health = game.player_health
            boss = BossZombie(zombie, player, player_health, zombie_health)
            boss.attack()
            player_score += 100
            high_score(player, player_score, score_file)
            ranked_scores(score_file)
            round_num += 1
        elif (round_num % 2) == 0:
            print(f"Round {round_num}")
            d = Dice()
            gather_supplies(d)
            pandasInventory(game, round_num)
            item = choose_weap(player_weapons)
            heal_item = choose_supply(player_supplies)
            use_supply(game, heal_item)
            round_num += 1
        else: 
            print(f"Round {round_num}.")
            game.attack(item, player_score, score_file)
            player_score += 25
            round_num += 1


if __name__ == "__main__":
    main()