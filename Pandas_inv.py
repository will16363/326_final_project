import pandas as pd
from round_fct import current_round
health=[100]
current_round=[7]
weaponInventory={"Sword": 15}
#weaponInventory.update({"Sword": 15})
weaponInventory["Sword"] = 15
foodInventory={"Bread": 5}

def pandasInventory():
    newWeapon = weaponInventory
    for key,value in newWeapon.items():
        k=key
        v=value

    weaponsDict={"Weapon": k}
    damageDict={"Weapon Damage": v}
  
    dfWeapon=pd.DataFrame(weaponsDict, index=[0])
    dfDamage=pd.DataFrame(damageDict, index=[0])

     
    food=foodInventory
    for key,value in food.items():
        a=key
        s=value

    
    foodDict=[{"Food":a}]
    buffDict=[{"Food Buff": s}]
   
    dfFood=pd.DataFrame(foodDict, index=[0])
    dfBuff=pd.DataFrame(buffDict, index=[0])

    healthData={"Health": health}
    dfHealth=pd.DataFrame(healthData, index=[0])

    roundData={"Round": current_round}
    dfRound=pd.DataFrame(roundData, index=[0])

    df1=pd.concat([dfHealth, dfRound, dfWeapon, dfDamage, dfFood,dfBuff], axis=1)
    return df1
pandasInventory()
