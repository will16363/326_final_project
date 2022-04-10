from random import choice

"""Need to figure out how players will only attack zombies with > 0 health and vice versa.
Probably need to do something similar to Mancala's functions: validate_move(), get_move()"""
# definitely work in progress!

class Zombie:
    """Action of one zombie.
    
        Attributes:
            zombie (str): zombie + index number of zombie.
            player (str): name of player zombie is attacking.
            damage (int): amount of damage done by zombie.    
    """
    def __init__(self, zombie):   
        """Initialize new zombie object.
        
        Args:
            zombie (str) = zombie + index number of zombie  
                  

        """
        self.zombie = zombie
        self.player = ""
        self.damage = ""
        
    def attack(self, player_list):
        """Attack of zombie on a player.
        
        Args:
            player_list (list): list of players.
        
        Returns:
            Str: True if attack succeeds; False if it does not.
        """
        self.player = choice([player_list])
        
        # call dice_roll()
        zombie_roll = self.zombie.DiceRoll()
        player_roll = self.player.DiceRoll()
        
        if zombie_roll > player_roll:
            self.damage = zombie_roll - player_roll              # or choice([1:6]) for damage?
            print(f'{self.player} took {self.damage} damage.')
            # call health function to update health
            # print something like "you now have [health] health left."            
            return True
        else:
            print('{self.player} dodged the attack!.')
            return False


class BossZombie(Zombie):
    """Action of boss zombie.
    
        Attributes:
            player_list (list): list of players.    
    """
    def __init__(self, player_list):
        """Initialize boss zombie.
        
        Args:
            player_list (list): list of players.
        """
        self.player_list = player_list
        
    def attack(self):
        """Boss zombie attack on all players, then on a single player."""
        roll1 = DiceRoll()
        roll2 = DiceRoll()
        roll3 = DiceRoll()
        roll4 = DiceRoll()
        roll5 = DiceRoll()
        
        # call health function to update health
        # self.player_list[0] -= roll1
        # self.player_list[1] -+ roll2 
        # etc.
        
        super().attack(self.player_list)
        # this should perform a normal zombie attack on one player.
               
    def __repr__(self):
        """Returns a statement of damage taken by each player from the boss zombie attack."""
        return (
            f"{self.player_list[0]} took {roll1} damage.\n"
            f"{self.player_list[1]} took {roll2} damage.\n"
            f"{self.player_list[2]} took {roll3} damage.\n"
            f"{self.player_list[3]} took {roll4} damage.\n"
            f"{self.player_list[4]} took {roll5} damage."
        )
        
class Player:
    """Action of one player.
    
    Attribute:
        weapon (str): player's weapon.
        player (str): name of player.
        zombie (str): zombie + index number of zombie.
        damage (int): amount of damage done by player using weapon.
    """
    def __init__(self, weapon):
        """Initalize player object.
        
        Args:
            weapon (str): player's weapon.
        """
        self.weapon = weapon     # take in weapon choice from round()
        self.player = player 
        self.zombie = ""
        self.damage = [weapon]
        
    def attack(self, zombie_list):
        """Ask for player input which zombie they would like to attack.
           self.zombie = input
           Initiate DiceRoll()
           return True if attack executes.  False if it does not.
           update health using health().
           print something like "You did xx dmg on zombie."
        """
