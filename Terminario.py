import random
import keyboard
import time
import os
import json
from game_data import items, check_dataplayerjson_exist

def get_data(namedatafile):
    with open(namedatafile, "r") as file:
        namedata = (json.load(file))
    return namedata

def save_data(namedatafile, savedata):
    with open(namedatafile, "w") as file:
        json.dump(savedata, file)
    return

dataplayer = get_data("dataplayer.json")
#funciones que no importan mucho
#---------------------------------------------------------------------------------------
def reprice(weapon_stats, potion_effects):
    #aqui falta la logica de como los tienderos van a cambiar el precio de las armas
    #segun las tiendas
    return
    
def accept():
    while True:
        confirt = keyboard.read_key().lower()
    
        if confirt == "enter":
            return
#----------------------------------------------------------------------------------------
def description_of_items(item, items):
    print("\x1b[10A\r\x1b[J", end="")
    
    if item in items["weapon_stats"]["long_range"]:
        diccionary = items["weapon_stats"]
        category2 = "damage"
        category3 = "pasive_damage"
        category = "long_range"

    elif item in items["weapon_stats"]["low_range"]:
        diccionary = items["weapon_stats"]
        category2 = "damage"
        category3 = "pasive_damage"
        category = "low_range"
        
    else:
        if item in items["potion_effects"]["health potions"]:
            diccionary = items["potion_effects"]
            category = "health potions"
            category2 = "effects"
            category3 = "health_boost"
                                 
    print(f"Pasive Damage: {diccionary[category][item][category2][category3]}" \
          f"\nSkill N1: {diccionary[category][item][category2]["skill1"]}" \
          f"\nSkill N2: {diccionary[category][item][category2]["skill2"]}" \
          f"\nSkill N3: {diccionary[category][item][category2]["skill3"]}" \
          "\n*Ok")

    accept()
    return

# todo def world(dataplayer,weapon_stats):

    # ? falta desarrollo

def main_store(dataplayer, items):

    while True:
        
        commodity = [
        "Baby staff",
        "Spoon",
        "Killdragons sword",
        "Leaf",
        "Small healing potion",
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
        
        time.sleep(0.1)
        while True:
            
            for d in commodity:
                if d in dataplayer["weapons"]:
                    d = "not available"
            
            for index, brand in enumerate(brands):
                brands[index] = ""
                if index == position:
                    m_ind = index
            brands[m_ind] = "*"

            print("\x1b[10A\r\x1b[J", end="")
            print(f"hello {dataplayer["name"]} this is the store")
            print( "¡¡¡please, choose your purchase!!!, or else press Esc for go to the main menu...\n" \
                  f"{brands[0]}[{commodity[0]}]  {brands[1]}[{commodity[1]}]  {brands[2]}[{commodity[2]}]\n" \
                  f"{brands[3]}[{commodity[3]}]  {brands[4]}[{commodity[4]}]  {brands[5]}[{commodity[5]}]")

            time.sleep(0.2)
            choose = keyboard.read_key()
            
            if choose == "esc":
                return

            elif choose == "flecha izquierda":
                if position != 0:
                    position -= 1
                else:
                    position = 5

            elif choose == "flecha derecha":
                if position != 5:
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
                description_of_items(commodity[position],items)
                time.sleep(0.1)

            elif choose == "enter":
        #resumen para miguel del futuro: decidi que el precio de las armas iba a ser un valor estatico en todas las tiendas
        #del mardito juego y que las tiendas le iban a subir o bajar porcentualmente el precio base a las marditas cosas, tambien 
        #que todas las armas de el juego iban a estar en weapon_stats y potion_effects
 #----------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
                time.sleep(0.2)
                brandL = "*"
                brandR = ""
                while True:
                    print("\x1b[10A\r\x1b[J", end="")
                    print(f"its price is {price} rublons, do you really want buy {commodity[position]}?         rublons:{dataplayer["rublons"]}" 
                        "\n(press \"E\" to see the attributes)\n" \
                        f"{brandL}yes  {brandR}no") 

                    time.sleep(0.2)           
                    key = keyboard.read_key().lower()

                    if key == "flecha derecha":
                        brandL = ""
                        brandR = "*"
            
                    elif key == "flecha izquierda":
                        brandR = ""
                        brandL = "*"

                    elif key == "e":
                        description_of_items(commodity[position],items)
                        time.sleep(0.1)
                    
                    elif key == "enter" and brandR == "*":
                        break

                    elif key == "enter" and brandL == "*":
                        print("\x1b[10A\r\x1b[J", end="")
                        time.sleep(0.2)
                        if dataplayer["rublons"] >= price: 
                            dataplayer["rublons"] -= price
                            
                            if commodity[position] in items["weapon_stats"]["long_range"] or commodity[position] in items["weapon_stats"]["low_range"]:
                                dataplayer["weapons"].append(commodity[position])

                            else:
                                dataplayer["potions"].append(commodity[position])
                            
                            print("x1b[10A\r\x1b[J", end="")
                            print("your item has been purchase✅​\n*ok")
                            accept() 

                        else:
                            print("x1b[10A\r\x1b[J", end="")
                            print("you dont have enough rublons for buy this item, you are an egg mother\n*ok ")
                            accept()
                            
def start(dataplayer,items):

    os.system("cls")

    position = 0
    brand0 = "*"
    brand1 = ""
    brand2 = ""
    brand3 = ""
    brands = [brand0, brand1, brand2, brand3]
    
    while True:        
        for index, brand in enumerate(brands):
            brands[index] = ""
            if index == position:
                m_ind = index
        brands[m_ind] = "*"
        
        print("\x1b[10A\r\x1b[J", end="")
        print(f"this is the main menu, you can go to the store, play the game, save your game or load your games!!"\
              f"\n{brands[0]}[store]  {brands[1]}[play]  {brands[2]}[save]  {brands[3]}[load]") 
          
        time.sleep(0.2)
        action = keyboard.read_key()
   
        if action == "flecha derecha":
            if position == 3:
                position = 0
            else:
                position += 1

        elif action == "flecha izquierda":
            if position == 0:
                position = 3
            else:
                position -= 1

        elif action == "enter" and position == 0:
            main_store(dataplayer = dataplayer, items=items)
            
        # * elif action == "enter" and position == 1:
            # ? aqui falta la funcion que ejecute el juego principal

        elif action == "enter" and position == 2:
            save_data(namedatafile="dataplayer.json",savedata=dataplayer)

        #elif action == "enter" and position == 3:
            #como el programa va a usar los archivos de partidas guardadas por el jugador

start(dataplayer=dataplayer, items=items)


               
