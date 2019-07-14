map = {
    "size_x": 5,
    "size_y": 5,
}

w1 = {
    "x": 1,
    "y": 1,
}

w2 = {
    "x": 2,
    "y": 2,
}

w3 = {
    "x": 1,
    "y": 2,
}

w4 = {
    "x": 3,
    "y": 3,
}

walls = [w1,w2,w3,w4]

key = {
    "symbol": "K",
    "x":0,
    "y":0,
}

door = {
    "x":4,
    "y":4,
}

player = {
    "x": 0,
    "y": 4,
}

got_key = False
win = False
while True:
    # Check if win or not   
    if player["x"] == door["x"] and player["y"] == door["y"]:
        if got_key:
            print("Congrats, you've just escape the dungeon.")
            win = True
        else:
            print("You can't exit, please acquire the key(s) first")

    # Print the map
    for i in range(map["size_y"]):
        for j in range(map["size_x"]):
            if i == player["y"] and j == player["x"]:
                print("P",end = " ")
            elif i == key["y"] and j == key["x"]:
                print(key["symbol"],end = " ")
            elif i == door["y"] and j == door["x"]:
                print("E",end = " ")
            else:
                is_wall = False
                for w in walls:
                    if i == w["y"] and j == w["x"]:
                        print("W",end = " ")
                        is_wall = True
                if not is_wall:
                    print("-",end = " ")             
        print()
    

     
    move = (input("Your move? ")).upper()
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
    else:
        break
    
    # Check if movable
    if 0 <= dx + player['x']< map['size_x'] and 0 <= dy + player['y'] < map['size_y']:
        hit_wall = False
        for w in walls:
            if dx + player['x'] == w["x"] and dy + player['y'] == w["y"]:
                hit_wall = True
                print("You can't not move through walls.")
        if not hit_wall:
            player['x'] += dx 
            player['y'] += dy

    # Check if got key    
    if player["x"] == key["x"] and player["y"] == key["y"]:
        print("You've just pick up a key!!!")
        key["symbol"] = "-"
        got_key = True

    if win:
        break