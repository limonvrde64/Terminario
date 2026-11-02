import json
import os

def save_data(namedatafile, savedata):
    with open(namedatafile, "w") as file:
        json.dump(savedata, file)
    return

def get_data(namedatafile):
    with open(namedatafile, "r") as file:
        namedata = (json.load(file))
    return namedata
#aqui se ve si esta el archivo con la informacion del jugador en el sistema, sino, la crea 
#--------------------------------------------------------------------------------------
def check_dataplayerjson_exist():
    DP_file = "dataplayer.json"
    if os.path.exists(DP_file):
        dataplayer = get_data(namedatafile=DP_file)
        
    if not os.path.exists(DP_file):

        name = input("¡¡welcome player!!, please write your name and press ENTER\n")
        print("\x1b[10A\r\x1b[J", end="")
        skin = input("\r!!ok, now, choose a letter or number for your skin¡¡        \n")

        while True:

            if len(skin) != 1:
                print("\x1b[10A\r\x1b[J", end="")
                skin = input("insert a only character... try again.\n")

            else:
                dataplayer = { 
                    "name":name,
                    "skin":skin,
                    "weapons":["Little pencil"],
                    "potions":[],
                    "rublons":0
                    }
                break 
    return dataplayer

#----------------------------------------------------------------------------------------
#datos de los items del juegooooo
#----------------------------------------------------------------------------------------
items = {
    "weapon_stats": {
        "long_range": {
            "Baby staff": {
                "damage": {
                    "pasive_damage": 19,
                    "skill1": "fireboll",
                    "skill2": "psychological poison",
                    "skill3": "mana recharge",
                },
                "attributes": {"price": 99},
            }},
        "low_range": {
            "Spoon": {
                "damage": {
                    "pasive_damage": 30,
                    "skill1": "impotent stab",
                    "skill2": "none",
                    "skill3": "none",
                },
                "attributes": {"price": 33},
            },
            "Killdragons sword": {
                "damage": {
                    "pasive_damage": 499,
                    "skill1": "bisectional disjunction",
                    "skill2": "isomeric compression",
                    "skill3": "non-euclidean severance",
                },
                "attributes": {"price": 4999},
            },
            "Leaf": {
                "damage": {
                    "pasive_damage": 5,
                    "skill1": "none",
                    "skill2": "none",
                    "skill3": "none",
                },
                "attributes": {"price": 1},
            },
            "Little pencil": {
                "damage": {
                    "pasive_damage": 2,
                    "skill1": "none",
                    "skill2": "none",
                    "skill3": "none",
                },
                "attributes": {"price": 0},
            },},},
    "potion_effects": {
        "health potions": {
            "Small healing potion": {
                "effects": {
                    "health_boost": 300,
                    "skill1": "potion sickness 1",
                    "skill2": "none",
                    "skill3": "none",
                },
                "attributes": {"price": 10},
            },
            "Medium healing potion": {
                "effects": {
                    "health_boost": 600,
                    "skill1": "potion sickness 2",
                    "skill2": "none",
                    "skill3": "none",
                },
                "attributes": {"price": 25},
            },
            "Big healing potion": {
                "effects": {
                    "health_boost": 1000,
                    "skill1": "potion sickness 3",
                    "skill2": "none",
                    "skill3": "none",
                },
                "attributes": {"price": 40},
            },}},}
#------------------------------------------------------------------------------------
