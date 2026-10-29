import random
import keyboard
import time
import os
data0 = True
# * data0 significa de que no hay informacion acerca del jugador
os.system("cls")

def accept():
    while True:
        confirt = keyboard.read_key().lower()
    
        if confirt == "enter":
            return

def description_of_items(item, weapon_stats, potion_effects):
    
    print("\x1b[10A\r\x1b[J", end="")
    
    if item in weapon_stats["long_range"]:
        diccionary = weapon_stats
        category2 = "damage"
        category3 = "pasive_damage"
        category = "long_range"

    elif item in weapon_stats["low_range"]:
        diccionary = weapon_stats
        category2 = "damage"
        category3 = "pasive_damage"
        category = "low_range"
        
    else:
        if item in potion_effects["health potions"]:
            diccionary = potion_effects
            category = "health potions"
            category2 = "effects"
            category3 = "health_boost"
                                 
    print(f"Pasive Damage: {diccionary[category][item][category2][category3]}" \
          f"\nSkill N1: {diccionary[category][item][category2]["skill1"]}" \
          f"\nSkill N2: {diccionary[category][item][category2]["skill2"]}" \
          f"\nSkill N3: {diccionary[category][item][category2]["skill3"]}" \
          "\n*Ok")

    accept()

# todo def world(dataplayer,weapon_stats):

    # ? falta desarrollo

def store(dataplayer):
    
    weapon_stats = {"long_range": {
                     "Baby staff": {"damage":
                                   {"pasive_damage":19,
                                    "skill1":"fireboll",
                                    "skill2":"psychological poison",
                                    "skill3":"mana recharge"}
                                   },
                    },
                     "low_range": {
                     "Spoon": {"damage":
                               {"pasive_damage":30,
                                "skill1":"impotent stab",
                                "skill2":"none",
                                "skill3":"none"}
                               },
                     "Killdragons sword": {"damage":
                                           {"pasive_damage":499,
                                            "skill1":"bisectional disjunction",
                                            "skill2":"isomeric compression",
                                            "skill3":"non-euclidean severance"}
                                          },
                     "Leaf": {"damage":
                              {"pasive_damage":5,
                               "skill1":"none",
                               "skill2":"none",
                               "skill3":"none"}
                               },
                     "Little pencil": {"damage":
                                       {"pasive_damage":2,
                                        "skill1":"none",
                                        "skill2":"none",
                                        "skill3":"none"}
                                     }}}
    
    potion_effects = {"health potions": {
                     "Small healing potion": {"effects": 
                                              {"health_boost":300,
                                              "skill1": "potion sickness 1",
                                              "skill2": "none",
                                              "skill3": "none"}
                                              },
                                              
                     "Medium healing potion": {"effects":
                                              {"health_boost":600,
                                               "skill1": "potion sickness 2",
                                               "skill2": "none",
                                               "skill3": "none"}
                                              },
                     "Big healing potion": {"effects":
                                           {"health_boost":1000,
                                            "skill1": "potion sickness 3",
                                            "skill2": "none",
                                            "skill3": "none"}
                                            }}}
    # ? potion_efects = {aqui falta codeo para establecer el funcionamiento de las pociones}

    while True:
        
        commodity = [
        "Baby staff",
        "Spoon",
        "Killdragons sword",
        "Leaf",
        "Small healing potion"
        "Little pencil"
        ]
        
        brand0 = "*"
        brand1 = ""
        brand2 = ""
        brand3 = ""
        brand4 = ""
        brand5 = ""
        brands = [brand0,brand1,brand2,brand3,brand4,brand5]
        position = 0
        
        for d in range(len(commodity)):
            if commodity[d] in dataplayer["weapons"]:
                del commodity[d]
                del brands[d]
        
        time.sleep(0.1)
        while True:
            for index, brand in enumerate(brands):
                brands[index] = ""
                if index == position:
                    m_ind = index
            brands[m_ind] = "*"

            print("\x1b[10A\r\x1b[J", end="")
            print(f"hello {dataplayer["name"]} this is the store")
            print( "¡¡¡please, choose your purchase!!!, or else press Esc for go to the main menu...\n" \
                  f"{brands[0]}[{commodity[0]}]  {brands[1]}[{commodity[1]}]  {brands[2]}[{commodity[2]}]\n" \
                  f"{brands[3]}[{commodity[3]}]  {brands[4]}[{commodity[4]}]")

            time.sleep(0.2)
            choose = keyboard.read_key()
            
            if choose == "esc":
                return

            elif choose == "flecha izquierda":
                if position != 0:
                    position -= 1
                else:
                    position = 4

            elif choose == "flecha derecha":
                if position != 4:
                    position += 1
                else:
                    position = 0

            elif choose == "flecha arriba":
                if position != 0:
                    position = 0

            elif choose == "flecha abajo":
                if position != 3:
                    position = 3

            elif choose == "e":
                description_of_items(commodity[position],weapon_stats, potion_effects)

            elif choose == "enter":
        
                if commodity[position] == "Killdragons sword":
                    price = 4999

                elif commodity[position] == "Baby staff":
                    price = 99

                elif commodity[position] == "Spoon":
                    price = 30

                elif commodity[position] == "Leaf":
                    price = 1

                elif commodity[position] == "Small healing potion":
                    price = 10

                time.sleep(0.2)
                brandL = "*"
                brandR = ""
                while True:
                    print("\x1b[10A\r\x1b[J", end="")
                    print(f"its price is {price} rublons, do you really want buy {commodity[position]}?         rublons:{dataplayer["rublons"]}" 
                        "\n(press \"E\" to see the attributes)\n" \
                        f"{brandL}yes       {brandR}no") 
            
                    key = keyboard.read_key().lower()

                    if key == "flecha derecha":
                        brandL = ""
                        brandR = "*"
            
                    elif key == "flecha izquierda":
                        brandR = ""
                        brandL = "*"

                    elif key == "enter" and brandR == "*":
                        break

                    elif key == "e":
                        description_of_items(commodity[position],weapon_stats, potion_effects)
                        time.sleep(0.5)

                    elif key == "enter" and brandL == "*":
                        if dataplayer["rublons"] >= price: 
                            dataplayer["rublons"] -= price
                            
                            if commodity[position] in weapon_stats:
                                dataplayer["weapons"].append(commodity[position])

                            else:
                                dataplayer["potions"].append(commodity[position])
                            
                            print("x1b[10A\r\x1b[J", end="")
                            print("your item has been purchase✅​\n*ok")
                            time.sleep(0.2)
                            accept() 

                        else:
                            print("x1b[10A\r\x1b[J", end="")
                            print("you dont have enough rublons for buy this item, you are an egg mother\n*ok ")
                            time.sleep(0.2)
                            accept()
                            
def start(data0,dataplayer):
    if data0:
        
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
                    "weapons":["little pencil"],
                    "potions":[],
                    "rublons":0
                    }
                break 
    
    brandL = "*"
    brandR = ""
    while True:        

        print("\x1b[10A\r\x1b[J", end="")
        print(f"this is the menu, !!you can go to the store or play the game¡¡\n{brandL}store        {brandR}play")
          
        time.sleep(0.1)
        action = keyboard.read_key()
   
        if action == "flecha derecha":
            brandL = ""
            brandR = "*"

        elif action == "flecha izquierda":
            brandL = "*"
            brandR = ""

        elif action == "enter" and brandL == "*":
            store(dataplayer)
            
        # * elif action == "enter" and brandR == "*":
            # ? aqui falta la funcion que ejecute el juego principal

start(data0,None)


               
