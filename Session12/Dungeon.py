import random
map = {
    "size_x": 14,
    "size_y": 7,
}
walls = [
    {"x": 1,"y": 1,},
    {"x": 2,"y": 2,},
    {"x": 1,"y": 2,},
    {"x": 3,"y": 3,},
    {"x": 3,"y": 2,},
    {"x": 2,"y": 5,},
    {"x": 3,"y": 5,},
    {"x": 4,"y": 5,},
    {"x": 6,"y": 5,},
    {"x": 5,"y": 3,},
    {"x": 5,"y": 2,},
    {"x": 0,"y": 5,},
    {"x": 0,"y": 4,},
    {"x": 3,"y": 0,},
    {"x": 4,"y": 0,},
    {"x": 5,"y": 0,},
    {"x": 3,"y": 6,},   
]
k1 = {
    "symbol": "K",
    "x":0,
    "y":0,
}
k2 = {
    "symbol": "K",
    "x":map["size_x"] - 1,
    "y":0,
}
exit = {
    "symbol": "E",
    "x": map["size_x"] - 1,
    "y": map["size_y"] - 1,
}
keys = [k1,k2]


defaul_damage = 25
defaul_shield = 10
defaul_health = 100
player = {
    "symbol": "P",
    "exp" : 0,
    "hp" : 100,
    "level": 1,
    "backpack": {
        "Damage spell": {
            "level": 1,
            "value": 0.2,
            "cooldown": 3,
        },
        "Shield spell": {
            "level": 1,
            "value": 0.2,
            "cooldown": 2,
        },
    }     
}
m1 = {}
m2 = {}
m3 = {}
boss = {}
monsters = [m1,m2,m3]
obstacles = [player,exit]
healing_potion = {"value": 50,}
armour = {"value": 5,}
sword  = {"value": 5,}
special_items = []

for w in walls:
    w["symbol"] = "W"
    obstacles.append(w)
def hit_something(object_x,object_y,obstacle):
    if type(obstacle) == list:
        for ob in obstacle:
            if ob["x"] == object_x and ob["y"] == object_y:
                return True
        return False
    else:
        if obstacle["x"] == object_x and obstacle["y"] == object_y:
                return True
        return False
def print_map():
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            empty_pos = True
            for ob in obstacles:
                # if ob["x"] == x and ob["y"] == y:
                if hit_something(x,y,ob):
                    if (ob is k2 and level < 2) or (ob in monsters and (level < 3 or hit_something(player["x"],player["y"],ob))) or (ob in keys and ob not in obstacles):
                        break
                    else:
                        empty_pos = False
                        print(ob["symbol"],end = " ")
            if empty_pos:
                print("-",end = " ")                 
        print()
    return
def monsters_move():
    if level >= 3:
        for m in monsters:
            while True:
                dx = random.randint(-1,1)
                dy = random.randint(-1,1)
                if dx != 0 and dy != 0:
                    continue
                if 0 <= m["x"] + dx < map["size_x"] and 0 <= m["y"] + dy < map["size_y"]:
                    if dx == 0 and dy == 0:
                        break
                    if hit_something(m["x"]+dx,m["y"]+dy,walls) or hit_something(m["x"] + dx,m["y"] + dy,exit)  or hit_something(m["x"] + dx,m["y"] + dy,monsters) :
                        continue                  
                    if hit_something(m["x"] + dx,m["y"] + dy,keys):
                        hit_able_key = False
                        for k in keys:
                            if (hit_something(m["x"] + dx,m["y"] + dy,k)) and (k not in obstacles):
                                hit_able_key = True
                        if not hit_able_key:
                            continue
                else:
                    continue
                m['x'] += dx 
                m['y'] += dy
                break
        return 
def print_backpack():
    print("Here is your backpack:")
    for i,item in enumerate(player["backpack"].keys()):
        if item == "Healing potion" and player["backpack"]["Healing potion"]["number"] == 0:
            continue
        print(i+1,". ",item,sep = "",end = "")
        if item != "Healing potion":
            print(": level:",player["backpack"][item]["level"],end = "")
            if item == "Damage spell":
                print("; cooldown: 3 turns; increase your damage by",player["backpack"][item]["value"]*100,"percent in 1 turn")
            if item == "Shield spell":
                print("; cooldown: 2 turns; increase your shield by",player["backpack"][item]["value"]*100,"percent in 1 turn")
        else:
            print(" x",player["backpack"]["Healing potion"]["number"])
        
    # input("\nPress enter to continue\n")
    while True:
        i = input("\nChoose a spell to use or 0 to quit: ")
        if not i.isdigit():
            print("Enter a number.")
            continue
        i = int(i) - 1 
        if i == -1:
            break
        elif 0 <= i < len(player["backpack"]):
            print()
            spell = list(player["backpack"].keys())[i]
            if spell == "Healing potion" and player["backpack"]["Healing potion"]["number"] > 0:
                player["hp"] += player["backpack"]["Healing potion"]["value"]
                if player["hp"] > defaul_health:
                    player["hp"] = defaul_health
                # del player["backpack"][spell]                    
                player["backpack"]["Healing potion"]["number"] -= 1
                print("You've been healed successfully. Your HP:",player["hp"])
            
            elif spell == "Damage spell":
                if player["backpack"][spell]["cooldown"] == 3:
                    player["damage"] *= 1 + player["backpack"][spell]["value"]
                    player["damage"] = round(player["damage"],1)
                    player["backpack"][spell]["cooldown"] = 0
                    print("Your damage has been increased successfully. Your damage:",player["damage"])
                else:
                    print("Your spell is cooling down.",3 - player["backpack"][spell]["cooldown"],"turn(s) left.")
            elif spell == "Shield spell":
                if player["backpack"][spell]["cooldown"] == 2:
                    player["shield"] *= 1 + player["backpack"][spell]["value"]
                    player["shield"] = round(player["shield"],1)
                    player["backpack"][spell]["cooldown"] = 0
                    print("Your shield has been increased successfully. Your shield:",player["shield"])
                else:
                    print("Your spell is cooling down.",2 - player["backpack"][spell]["cooldown"],"turn(s) left.")
            
            # input("\nPress enter to continue")
            
            break
        else:
            print("Invalid number.")
            continue
def player_move():
    print("Your move?(w/a/s/d/q = quit) ")
    if level >= 3:
        print("Press b to check your backpack")
        print("Press i to check your stats")
    move = input().upper()
    print()
    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    elif move == "Q":
        return "quit"
    elif move == "B" and level >= 3:
        print_backpack()
    elif move == "I" and level >= 3:
        print("Your stats:")
        print("* Level:",player["level"])
        print("* EXP: ",player["exp"],"/100",sep = "")
        print("* HP: ",player["hp"],"/100",sep = "")
        print("* Damage:",player["damage"])
        print("* Shield:",player["shield"])
        if armour not in special_items and level >= 5:
            print("You're wearing an armour. (increase",armour["value"],"shield)")
        if sword not in special_items and level >5:
            print("You're holding a sword. (increase",armour["value"],"damage)")    
        input("\nPress enter to continue\n")
        
    else:
        print("Invalid move!")
        return "continue"


    # Check if movable
    if 0 <= dx + player['x']< map['size_x'] and 0 <= dy + player['y'] < map['size_y']:
        if hit_something(player["x"] + dx,player["y"] + dy,walls):
            print("You can't not move through walls.\n")
        else:
            player['x'] += dx 
            player['y'] += dy
            if dx != 0 or dy != 0:
                player["hp"] += 0.2
            if player["hp"] > defaul_health:
                player["hp"] = defaul_health
            return [dx,dy]
    else:
        print("You can't go out of the map.\n")
def reset():    
    defaul_damage = 25
    defaul_shield = 10
    # defaul_health = 100
    player["x"] = 0
    player["y"] = map["size_y"] - 1
    # player["hp"] = defaul_health
    player["damage"] = defaul_damage
    player["shield"] = defaul_shield
    if level == 1:
        obstacles.append(k1)
    else:
        for k in keys:
            obstacles.append(k)
    if level >= 3:
        if level >= 6:
            monsters.append(boss)
        for m in monsters:
            if m in obstacles:
                obstacles.remove(m)
            m["symbol"] = "M"
            m["hp"] = 75
            m["damage"] = 20
            m["shield"] = 15
            if m is boss:
                m["symbol"] = "B"
                m["hp"] = 150
                m["damage"] = 30
                m["shield"] = 10
                m["critical"] = 1.5
            while True:
                m["x"] = random.randint(0, map["size_x"] - 1)
                m["y"] = random.randint(0, map["size_y"] - 1)
                if hit_something(m["x"],m["y"],obstacles):
                    continue
                else:
                    obstacles.append(m)
                    break
    if level >= 4:
        for i in special_items:
            special_items.remove(i)
        print("Hint: There is a healing potion hidden in the map.")
        while True:
            healing_potion["x"] = random.randint(0, map["size_x"] - 1)
            healing_potion["y"] = random.randint(0, map["size_y"] - 1)
            if hit_something(healing_potion["x"],healing_potion["y"],obstacles):
                if hit_something(healing_potion["x"],healing_potion["y"],monsters):
                    break
                else:
                    continue
            else:
                break
        special_items.append(healing_potion)
    if level >= 5:
        print("Hint: There is an ARMOUR to increase shield \nand a SWORD to increase damage hidden in the map.")
        for item in [armour,sword]:
            while True:
                item["x"] = random.randint(0, map["size_x"] - 1)
                item["y"] = random.randint(0, map["size_y"] - 1)
                if hit_something(item["x"],item["y"],obstacles):
                    if hit_something(item["x"],item["y"],monsters):
                        break
                    else:
                        continue
                elif hit_something(item["x"],item["y"],special_items):
                    continue
                else:
                    break
            special_items.append(item)
    return False
def defeated_mons():
    if encounter_boss:
        input("You receive 70 exp and a healing potion\n")
        player["exp"] += 70
        player["backpack"]["Healing potion"]["number"] += 1
    else:
        input("You receive 30 exp\n")
        player["exp"] += 30
    if player["exp"] >= 100:
        print("Level up!")
        print("Choose a spell to upgrade:")
        player["exp"] -= 100
        player["level"] += 1
        while True:
            for i,item in enumerate(player["backpack"].keys()):
                if item != "Healing potion":
                    print(i+1,". ",item,sep = "",end = "")
                    print(": level:",player["backpack"][item]["level"],end = "")
                    if item == "Damage spell":
                        print("; cooldown: 2 turns; increase your damage by",player["backpack"][item]["value"]*100,"percent in 1 turn")
                    if item == "Shield spell":
                        print("; cooldown: 1 turn; increase your shield by",player["backpack"][item]["value"]*100,"percent in 1 turn")
            i = input("\nChoose to level up: ")
            if not i.isdigit():
                print("Enter a number.")
                continue
            i = int(i) - 1 
            if 0 <= i < 2:
                print()
                spell = list(player["backpack"].keys())[i]
                player["backpack"][spell]["level"] += 1
                player["backpack"][spell]["value"] += 0.2
                player["backpack"][spell]["value"] = round(player["backpack"][spell]["value"],2)
                print(spell,": level:",player["backpack"][spell]["level"],end = "")                
                if spell == "Damage spell":
                    print("; cooldown: 2 turns; increase your damage by",player["backpack"][spell]["value"]*100,"percent in 1 turn")
                if spell == "Shield spell":
                    print("; cooldown: 1 turn; increase your shield by",player["backpack"][spell]["value"]*100,"percent in 1 turn")
                input("\nPress enter to continue")
                
                break
            else:
                print("Invalid number.")
                continue
level = 0
got_all_key = False
win = True
lose = False
    
print("\nWelcome to Dungeon")
# main loop
while True: 
    if lose:
        print("Do you want to play again?(y/n)")
        cont = input().lower()
        if cont == "y":
            level = 0
            win = True
            lose = False            
            continue
        else:
            break
    
    if win:
        print("\nDo you want to play level ",level + 1,"?(y/n) ",sep = "")
        cont = input().lower()
        if cont == "y" or cont == "":
            level += 1
            win = reset()          
            print("Here is level ",level,":\n",sep = "")
            continue
        else:
            break
    
    # Check if win or not
    if hit_something(player["x"],player["y"],exit):
        exit["symbol"] = ""
        if got_all_key:
            print("Congrats, you've just escape the dungeon.")
            win = True
            print_map()
            continue
        else:
            print("You can't exit, please acquire the key(s) first.\n")
    else:
        exit["symbol"] = "E"    
    
    print_map()
    
    temp_move = player_move()
    if temp_move == "quit":
        break
    if temp_move == "continue":
        continue

    # Check if hit healing potion
    if level >= 4:
        if hit_something(player["x"],player["y"],healing_potion) :
            if "Healing potion" not in player["backpack"]:
                player["backpack"]["Healing potion"] = {
                    "value" : healing_potion["value"],
                    "number": 1,
                }
            else:
                player["backpack"]["Healing potion"]["number"] += 1               
                
            healing_potion["x"] = map["size_x"]
            healing_potion["y"] = map["size_y"]
            print_map()
            print("\nCongratulation you've found the healing potion.")
            print("It is in your back pack now.")
            t = input("Press b to check your backpack\n")
            if t == "b":
                print_backpack()       
    if level >= 5:
        if hit_something(player["x"],player["y"],armour) and defaul_shield == 10 :
            print("\nCongratulation you've found the armour.")
            defaul_shield += armour["value"]
            player["shield"] = defaul_shield
            special_items.remove(armour)
            print("Now your shield is:",player["shield"],"\n")
            input()
        if hit_something(player["x"],player["y"],sword) and defaul_damage == 25 :
            print("\nCongratulation you've found the sword.")
            defaul_damage += sword["value"]
            player["damage"] = defaul_damage
            special_items.remove(sword)
            print("Now your damage is:",player["damage"],"\n")
            input()
    monsters_move()

    encounter_mon = False
    encounter_boss = False
    while level >= 3 and not lose:
        # Check if encouter monster or not
        for m in monsters:
            if hit_something(m["x"],m["y"],player) and m in obstacles:
                encounter_mon = True
                temp_mon = m
                if m is boss:
                    encounter_boss = True
                break
        # Player vs monster
        if encounter_mon:
            exit["symbol"] = "E"
            print_map()
            if not encounter_boss:
                input("\nYou've encountered the monster\n")
            else:
                input("\nYou've encoutered the boss\n")
            turn = random.randint(0,1)
            monst_atk = False
            monst_def = False
            player_atk = False
            player_def = False

            # Print player and monsters infos
            print("Player and Monster infos:")
            for i in [player,temp_mon]:
                if i["symbol"] == "P":
                    print("Player's stats:")
                else:
                    print("Monster's stats:")
                print("* HP: ",i["hp"],sep = "")
                print("* Damage: ",i["damage"],sep = "")
                print("* Shield: ",i["shield"],sep = "")
            input()


            while encounter_mon:
                # Player's turn             
                if turn == 1:
                    # Check monster attack
                    if monst_atk:
                        monst_damage = temp_mon["damage"]
                        if encounter_boss:
                            crit = False
                            if random.randint(0,9) > 8:
                                input("The boss has attacked you critically\n")
                                monst_damage = temp_mon["damage"]*temp_mon["critical"]
                        if player_def:
                            if random.randint(0,9) < 8 :
                                input("You've defended successfully\n") 
                                if monst_damage > player["shield"]:
                                    player["hp"] -= monst_damage - player["shield"]
                            else:
                                input("You've countered the monster\n")
                                temp_mon["hp"] -= 2*monst_damage
                            if player["shield"] != defaul_shield:
                                player["shield"] = defaul_shield
                                print("Now your shield is:",player["shield"])
                                input() 
                            if temp_mon["hp"] <= 0:
                                for ob in obstacles:
                                    if hit_something(ob["x"],ob["y"],temp_mon) and ob in monsters:
                                        obstacles.remove(ob)
                                print("Good job! You've defeated the monster.\n")
                                defeated_mons()
                                encounter_mon = False
                                break
                        else:
                            input("You've been attacked\n")
                            player["hp"] -= monst_damage

                        # Check if player died
                        if player["hp"] <= 0:
                            print("You have been killed\n")
                            encounter_mon = False
                            lose = True
                            break
                    
                        # Print current HP
                        for i in [player,temp_mon]:
                            if i["symbol"] == "P":
                                print("Player's HP:",player["hp"])
                            else:
                                print("Monster's HP:",temp_mon["hp"])
                        print()


                        # if player["backpack"]["Shield spell"]["cooldown"] < 2:
                        #     player["backpack"]["Shield spell"]["cooldown"] += 1
                            
                  

                    # Get player's action
                    player_atk = False
                    player_def = False
                    while True:
                        print("It's your turn")
                        action = input("Do you want to run or attack or defend?(r/a/d/b) ").lower()
                        print()
                        if action == "r":
                            run_rate = 5         
                            if encounter_boss:
                                run_rate = 7
                            if random.randint(0,9) >= run_rate:
                                input("You can run now\n")
                                print_map()
                                player_move()
                                encounter_mon = False                               
                            else:
                                input("You've failed to escape\n")
                            break
                        elif action == "a":
                            input("You are attacking the monster\n")
                            player_atk = True
                            break
                        elif action == "d":
                            input("You are defending\n")
                            player_def = True
                            break
                        elif action == "b":
                            print_backpack()
                            print()
                        else:
                            continue
                    if player["backpack"]["Damage spell"]["cooldown"] < 3:
                        player["backpack"]["Damage spell"]["cooldown"] += 1
                    if player["backpack"]["Shield spell"]["cooldown"] < 2:
                        player["backpack"]["Shield spell"]["cooldown"] += 1
                    turn = 0
                    continue                
                # Monster's turn
                else:              
                    # Check player attack   
                    if player_atk:
                        if monst_def:
                            if random.randint(0,9) < 8:    
                                input("The monster has defended\n")
                                if player["damage"] > temp_mon["shield"]:
                                    temp_mon["hp"] -= player["damage"] - temp_mon["shield"]
                            else:
                                input("The monster has countered you\n")
                                player["hp"] -= 2*player["damage"]
                                if player["hp"] <= 0:
                                    input("You have been killed\n")
                                    encounter_mon = False
                                    lose = True
                                    break
                        else:
                            input("The monster has been attacked\n")
                            temp_mon["hp"] -= player["damage"]

                        if player["shield"] != defaul_shield:
                            player["shield"] = defaul_shield
                            print("Now your shield is:",player["shield"])
                            input()
                        if player["damage"] != defaul_damage:
                            player["damage"] = defaul_damage
                            print("Now your damage is:",player["damage"])
                            input()                                         
                        
                        # Check monster die
                        if temp_mon["hp"] <= 0:
                            for ob in obstacles:
                                if hit_something(ob["x"],ob["y"],temp_mon) and ob in monsters:
                                    obstacles.remove(ob)
                            input("Good job! You've defeated the monster.\n")
                            defeated_mons()
                            encounter_mon = False
                            break
                    
                        # Print current HP
                        for i in [player,temp_mon]:
                            if i["symbol"] == "P":
                                print("Player's HP:",player["hp"])
                            else:
                                print("Monster's HP:",temp_mon["hp"])
                        print()
                    if player["damage"] != defaul_damage:
                        player["damage"] = defaul_damage
                        print("Now your damage is:",player["damage"])
                        input()      
                        
                    input("It's the monster turn\n")
                    hit_rate = 5
                    if encounter_boss:
                        hit_rate = 7 
                    if random.randint(0,9) > hit_rate:
                        monst_atk = False
                        monst_def = True
                    else:
                        monst_atk = True
                        monst_def = False      
                    turn = 1
                    continue
        else:
            break

    # Check player pick up key
    for k in keys:    
        if hit_something(k["x"],k["y"],player) and k in obstacles:
            print("You've just pick up a key!!!\n")
            # k["symbol"] = "-"
            for ob in obstacles:
                if ob is k:
                    obstacles.remove(ob)
            got_all_key = True
    # Check play got all key
    for k in keys:
        if k in obstacles:
            got_all_key = False

