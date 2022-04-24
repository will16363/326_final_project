Class Supplies:

Inventory[]


Weapon
Pistol-20
knife- 10 
axe-10
baseball bat-10
golf club- 10
shotgun- 30

Supplies
Water- 40
Shoes-30
Food-40
Medical supplies- 40
Lighter-30 
Gloves-30  


Def gather_supplies(self, dice_roll):
If dice_roll == 1:
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
       self.player.Invetory.append(“medical_supplies”)
elif dice_roll == 9:
       self.player.Invetory.append(“golf club”)
elif dice_roll == 10:
      self.player.Invetory.append(“lighter”)
elif dice_roll == 11:
      self.player.Invetory.append(“shotgun”)
elif dice_roll == 12:
      self.player.Invetory.append(“gloves”)


def __init__(self, player): 
  Self.player = player
  def gather_supplies(self, dice_roll)  
  def use_supply(self, item)
  Def game_over(self)
  Def print_status_bar(self, percent)
