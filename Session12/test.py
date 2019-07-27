player = {
    "symbol": "P",
    "exp" : 0,
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
# print(type(player["backpack"].keys()))
print("Healing potion" in player["backpack"])
print("Damage spell" in player["backpack"])