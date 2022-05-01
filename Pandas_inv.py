from re import A
import pandas as pd
import numpy as np
from round_fct import current_round
health=[100]
current_round=[7]
items=[]
weapon=[]

weapon.append({"gun":50})
weapon.append({"sword":25})
#pandas
def pandasInventory():
    inventory = {"Player Health":health, "Current Round": current_round, 
             "Weapon": weapon, "Items": items}
    pandasInv=pd.DataFrame.from_dict(inventory, orient='index')
    pandasInv=pandasInv.transpose()
    return pandasInv
pandasInventory()

mylist=[health, current_round, weapon, items]