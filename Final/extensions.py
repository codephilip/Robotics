#Created By: Michael Roduin
#Date: 5/1/22

import random

def attempt_escape():
    return random.random() > .25 #75%

def attack():
    return random.random() > .25 #75%

def enemy_critical():
    return random.random() > .9 #10%

def player_critical():
    return random.random() > .85 #15%

def easy_enemy_damage():
    damage = [3,4,5]
    hit = int(attack() == True)
    critical = int(enemy_critical() == True) + 1
    if critical == 2 and hit == 1:
        print("Critical Hit")
    elif hit == 1:
        print("Hit")
    else:
        print("Miss")
        return 0
    return random.choice(damage)*critical

def medium_enemy_damage():
    damage = [6,7,8]
    hit = int(attack() == True)
    critical = int(enemy_critical() == True) + 1
    if critical == 2 and hit == 1:
        print("Critical Hit")
    elif hit == 1:
        print("Hit")
    else:
        print("Miss")
        return 0
    return random.choice(damage)*critical

def hard_enemy_damage():
    damage = [9,10,11,12]
    hit = int(attack() == True)
    critical = int(enemy_critical() == True) + 1
    if critical == 2 and hit == 1:
        print("Critical Hit")
    elif hit == 1:
        print("Hit")
    else:
        print("Miss")
        return 0
    return random.choice(damage)*critical

def player_damage():
    damage = [9,10,11,12]
    hit = int(attack() == True)
    critical = int(player_critical() == True) + 1
    if critical == 2 and hit == 1:
        print("Critical Hit")
    elif hit == 1:
        print("Hit")
    else:
        print("Miss")
        return 0
    return random.choice(damage)*critical

"""
for item in range(0,10):
    print(player_damage())
"""
"""
x = [calculate_three_quarter() for item in range(0,100)]
print(sum(x))
"""
