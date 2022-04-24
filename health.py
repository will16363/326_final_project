Def print_status_bar (self):
	If self.player.health == 100:
    Return “100% [==========]” 
Elif self.player.health == 90:
  	    Return “90% [=========  ]”
	Elif self.player.health == 80:
  	    Return “80% [========    ]”
	Elif self.player.health == 70:
  	    Return “70% [=======      ]”
	Elif self.player.health == 60:
	    Return “60% [======        ]”
Elif self.player.health == 50:  
    Return “50% [=====          ]”
Elif self.player.health == 40:
    Return “40% [====            ]”
Elif self.player.health == 30:
    Return “30% [===              ]”
Elif self.player.health == 20:
    Return “20% [==                ]”
Elif self.player.health == 10:
    Return “10% [=                  ]”
Elif self.player.health == 0:
    Return “0% [                    ]”

def decrease_health(self, damage):
    If self.player.health - damage <= 0:
        gameover(self);
    else:
        self.player.health -= damage

Def increase_health(self, heal)
    If self.player.health + heal >= 100:
        Self.player.health = 100
    Else:
        Self.player.health += heal


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
