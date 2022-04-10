
import random

class Dice_Roller():
    def __init__(self, sides=6):
        self.sides= sides
        
    def roll(self):
        result1=random.randint(1, self.sides)
        result2=random.randint(1, self.sides)
        return result1+result2
    