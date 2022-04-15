
import random

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
