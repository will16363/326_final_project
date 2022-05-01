
import random
from unittest import result

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
#f string    
d=Dice
playerRoll=d.roll(Dice)       
def mostRecentRoll(playerRoll):
    return(f"Your most recent roll was {playerRoll}")
mostRecentRoll(playerRoll)