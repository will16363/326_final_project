import random
import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot as plt
from matplotlib import use
from pytest import Item
from argparse import ArgumentParser
# from babylonian import parse_args # do we need the babylonian one or can we use the argparse that Aric uses instead?
from unittest import result


weapons = [{"pistol":20, 'knife':10, 'axe':10, 'baseball bat': 10, 
            'golf club':10, 'shotgun':30}]
supplies = [{"water":40, 'shoes':30, 'food':40, 'medical supplies': 40, 
            'lighter':30, 'gloves':30}]
player_weapons = []
player_supplies = []
score_file = 'score.txt'


class Dice():
    """A dice object which has 6 sides
    
    Attributes:
        sides (set): the sides of the dice
    """
    #set operations
    def __init__(self, sides):
        """Initializes the sides attribute of the dice"""
        self.sides= sides
        sides=()
        sides.update(6)
     
    #Sequence unpacking   
    def roll(self):
        """Takes the value of two random sides and returns the sum
        
        Side effects:
            appends the resulting sum of the two sides to the roll values list
            
        Returns: Returns the sum of the two dice sides
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
        
        Returns: Returns the scatterplot of the dataframe
        """
        d = {"Roll Number":[i for i in range(100)], "Roll Value": result}
        rollplot=pd.DataFrame.from_dict(d, orient='index')
        rollplot=rollplot.transpose()
        return rollplot.plot.scatter('Roll Number', y = 'Roll Value')


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
    round_num += round_num + 1
    if skip_supply == "True":
        print(f"You have skipped your supply run. Now prepare for the "
              "Zombie fight!")
        print("round "+ round_num)
        return round_num
    else:
        print(f"round "+ round_num)
        print("You may now gather supplies!")
        return ("round" + round_num)



def print_status_bar(ZombiePlayer): 
    """ Health function """
    """def print_status_bar(percent):
    This function gets the players health and keeps track of it using
      percentage represented by individual bars
      ex- = is 10% == is 20%. Each player will gain or lose a bar
      depending on how they are performing in the game. The status bars add up
      to 100. There are also weapons and supplies in this game worth different
      amount of points. So the player's health level will change based on that.
    Args:
     This function gets the players health and keeps track of it using
      percentage represented by individual bars ex- = is 10% == is 20%. Each player
      will gain or lose a bar depending on how they are
      performing in the game. The status bars add up
      to 100.
      
    Side effect: prints players health status 
    """
    if ZombiePlayer.player_health == 100:
        print("100% [==========]")                             
    elif ZombiePlayer.player_health < 100 and ZombiePlayer.player_health >= 90:
        print("90% [========= ]")
    elif ZombiePlayer.player_health < 90 and ZombiePlayer.player_health >= 80:
        print("80% [========  ]")
    elif ZombiePlayer.player_health < 80 and ZombiePlayer.player_health >= 70:
        print("70% [=======   ]")
    elif ZombiePlayer.player_health < 70 and ZombiePlayer.player_health >= 60:
        print("60% [======    ]")
    elif ZombiePlayer.player_health < 60 and ZombiePlayer.player_health >= 50:
        print("50% [=====     ]")
    elif ZombiePlayer.health < 50 and ZombiePlayer.player_health >= 40:
       print("40% [====      ]")
    elif ZombiePlayer.player_health < 40 and ZombiePlayer.player_health >= 30:
        print("30% [===       ]")
    elif ZombiePlayer.player_health < 30 and ZombiePlayer.player_health >= 20:
        print("20% [==        ]")
    elif ZombiePlayer.player_health < 20 and ZombiePlayer.player_health >= 10:
        print("10% [=         ]")
    elif ZombiePlayer.player_health < 10 and ZombiePlayer.player_health >= 0:
        print("0% [          ]")
        return (round_num)


def game_over(ZombiePlayer, round_num):                
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
    return ZombiePlayer.player_health <= 0 or round_num == 13

# needs doctrings
<<<<<<< HEAD
def use_supply(ZombiePlayer, item):
    if item == 'water': 
        ZombiePlayer.increase_health(ZombiePlayer, 40)
    elif item == 'shoes': 
        ZombiePlayer.increase_health(ZombiePlayer, 30)
    elif item == 'food': 
        ZombiePlayer.increase_health(ZombiePlayer, 40)
    elif item == 'medical supplies': 
        ZombiePlayer.increase_health(ZombiePlayer, 40)
    elif item == 'lighter': 
        ZombiePlayer.increase_health(ZombiePlayer, 30)
    elif item == 'gloves': 
        ZombiePlayer.increase_health(ZombiePlayer, 30)


# needs doctrings
def gather_supplies(Zombie_Player, Dice):
    """Gathering Supplies """
    """Get players to roll and gather an based on the number they get item.
      The player will need to roll two dyes and the supplies
      the get will be depending on what number the dice rolls on.
      This logic also applies to the weapons in this game.
    Args:
      dice_roll(int): this variable represents the sum of the two
      dices that the player rolls
   Side Effects: Player will get a weapon or an supply added to their
   inventory
    """
    if Dice.roll() == 1:
        player_weapons.append({'water':0})
    elif Dice.roll() == 2:
=======
def gather_supplies(ZombiePlayer, Dice):
    if Dice.roll() == 2:
>>>>>>> ede3b3cb92cc4cc98046eca6d43367d1197659aa
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


# needs doctrings
def use_supply(ZombiePlayer, item):
    if item == 'water': 
        ZombiePlayer.increase_health(ZombiePlayer, 40)
    elif item == 'shoes': 
        ZombiePlayer.increase_health(ZombiePlayer, 30)
    elif item == 'food': 
        ZombiePlayer.increase_health(ZombiePlayer, 40)
    elif item == 'medical supplies': 
        ZombiePlayer.increase_health(ZombiePlayer, 40)
    elif item == 'lighter': 
        ZombiePlayer.increase_health(ZombiePlayer, 30)
    elif item == 'gloves': 
        ZombiePlayer.increase_health(ZombiePlayer, 30)


# pandas dataframe
def pandasInventory(ZombiePlayer, round_num):
    """Dataframe that tracks the players current health, current round, 
        weapons, and items
        
    Args:
        ZombiePlayer (class): One round of action for zombie and player
        round_num (int): The round number
        
    Returns: the dataframe
    """
    inventory = {"Player Health":ZombiePlayer.health, "Current Round": round_num, 
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
def high_score(ZombiePlayer, new_score, score_file):
    """Writes the player's score to a high score file.
    Args:
        new_score (int): Score of the player at the end of the game.
        player_name (str): Name of the player (maybe use self.name?)
        score_file (str): File path for the high score file.
    Side effects:
        Modifies a file that high scores are kept in.
    """
    with open(score_file, 'a') as f:
        f.write(f'{ZombiePlayer.player}:{new_score}\n')


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
    def __init__(self, player, zombie, chosen_weapon):   
        """Initialize new zombie and player object."""
        self.zombie = player      
        self.player = zombie      
        self.player_health = 100
        self.zombie_health = 25
        self.damage = 0
        self.weapon = chosen_weapon
        self.zombie_roll = 0   
        self.player_roll = 0   

    def attack(self):
        """Attack action for both player and zombie.
        
        Side effects:
            prints statements on the terminal.
        """
        while self.zombie_health > 0 and self.player_health > 0:
            zombie_roll = self.zombie.DiceRoll()
            player_roll = self.player.DiceRoll()
            print(f"{self.zombie} rolled a {zombie_roll}. {self.player} rolled "
                "a {player_roll}.")
            if zombie_roll > player_roll:
                self.damage = int(zombie_roll) - int(player_roll)              
                print(f'{self.player} took {self.damage} damage.')
                self.decrease_health(self.player, self.damage)
                self.decrease_health(self.damage)  # one argument only
                self.print_status_bar(self)
                input("Press Enter to continue...")
            elif zombie_roll <= player_roll:
                self.damage = int(self.weapon) #the damage of the weapon that the player chooses to use           
                print(f'{self.zombie} took {self.damage} damage.')
                self.decrease_health(self.zombie, self.damage)
                self.decrease_health(self.damage) # one argument only
                self.print_status_bar(self)
        if self.zombie_health <= 0:
            player_score = score(player_score, 'True')
            print(f"You have beaten the {self.zombie}!")
        elif self.player_health <= 0:
            player_score = score(player_score, 'False')
            high_score(self.player, player_score, score_file)
            ranked_scores(score_file)

    
    def decrease_health(self, damage):
        """decrease health"""
        """This keeps track of the health lost by each player.
            There are different types of weapons in this games such as bats
            and shotgun. With this we will be able to see the amount of 
            points lost depending on the damage the player took."
        Args:damage(int): represents the damage the players took due to an attack.
 
        Side Effects: player loses health and if the health falls to 0
                  the function calls the game_over() function and the player loses. 
        """

        if self.player_health - damage <= 0:
            game_over()
        else:
            self.player.health -= damage
        if self.zombie_health - damage <= 0:
            self.zombie_health = 0
        
    # needs doctrings
    def increase_health(self, heal):
        """increase_health"""
            """This keeps track of the health gained by each player.
            Player is able to collect supplies throughout the game such as
            water, food, shoes and so on. When they collect these things this their
            health points have increased."
        Args:
        heal(int): represents how much the player healed based on the supplies they were able to collect.
        Side Effects: player gains health up to 100
        """

        if self.player_health + heal >= 100:
            self.player_health = 100
        else:
            self.player_health += heal
            
    # needs doctrings
    def print_status_bar(self): 
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
    def __init__(self, player, zombie, chosen_weapon):
        """Initialize new boss zombie object.
        
        Args:
            player (str): name of player.
            zombie (str): name of zombie.
            chosen_weapon (str): name of weapon selected by player.
        """
        super().__init__(player, zombie, chosen_weapon)
        self.roll1 = 0
        self.roll2 = 0
        self.roll3 = 0

    # __repr__()    
    def __repr__(self):   
        """Returns a formal representation of damage taken by the player from 
            the special attack."""
        return (
            f"1st: {self.roll1} damage dealt to {self.player}.\n"        
            f"2nd: {self.roll2} damage dealt to {self.player}.\n"
            f"3rd: {self.roll3} damage dealt to {self.player}.\n"
            f"Total damage: {self.damage}." 
            )   
    
    # super() method 
    def attack(self):
        """Special attack action of boss zombie followed by attack method of 
            parent class.
        
        Side effects:
            prints statements and repr on terminal.
        """
        self.boss_zombie_health = 50  
        self.roll1 = Dice.roll()    
        self.roll2 = Dice.roll()
        self.roll3 = Dice.roll()
        self.zombie_roll = 1   
        self.player_roll = 0
        self.damage = int(self.roll1) + int(self.roll2) + int(self.roll3)
        super().decrease_health(self.damage) 
        print(repr(self))
        super().print_status_bar(self)
        input("Press Enter to continue...")
        super().attack()


def main(): 
    #figure out where im going to put the list comphrensions 
    # EXPR FOR ITERVAR IN ITERABLE 
    
    print("Welcome to zombie rolls!")  
    round_num=0
    player_score=0
    while game_over() == False:
        while round_num < 13:
            round_fct(round_num,skip_supply= input("Would you like to skip this round? True or False?"))
            if skip_supply != "True":
                gather_supplies(ZombiePlayer,Dice)
                pandasInventory(ZombiePlayer,round_num)
                # what is item? make sure this is being defined
                use_supply(ZombiePlayer,item)
                ZombiePlayer.attack()
            
            if skip_supply == "True":
                ZombiePlayer.attack()
    

def parse_args(arglist):#only for command line args(user inputted args)
    parser = ArgumentParser()
    parser.add_argument(name="Sam" help= "players name")
    parser.add_argument()
    return parser.parse_args(arglist)  

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main()
        