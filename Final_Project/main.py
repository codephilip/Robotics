# Created By: Michael Roduin
#Date: 5/1/22
import build_map
import sounds
from random import randint
# for animation
import tkinter as tk
from PIL import Image, ImageSequence
from threading import *

# controls
import robot_controls as tango
from robot_controls import VoiceController
import time

#import animations

import extensions


#import speech_to_text as stt
#import text_to_speech as tts

# gif animation


MAX_TURNS = 25
STANDARD_TURN = 1
STANDARD_SPEED = 1

PLAYER_HEALTH_MAX = 100
EASY_ENEMY_HEALTH_MAX = 50
MEDIUM_ENEMY_HEALTH_MAX = 75
HARD_ENEMY_HEALTH_MAX = 100

# TKinter Root
#root = tk.Tk()
#key = False
#game_map = build_map.generate_level_2
# game_map.generate_level_2()
# print(game_map)
# print(game_map[0][0])
#sounds.hp_sound(16, 12)

# Action Management Functions

# Robot Object
robot = tango.Tangobot()
# animation Object


root = tk.Tk()
file = "deidara-explosion.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(
    file=file, format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50, lambda: animation(count))


def stop_animation():
    root.after_cancel(anim)


def stopit():
    root.destroy()
    # root.quit()


gif_label = tk.Label(root, image="")
gif_label.pack()

start = tk.Button(root, text="Start Game", command=lambda: animation(count))
start.pack()

quitb = tk.Button(root, text="I'm Ready!", command=stopit)
quitb.pack()


root.mainloop()

# work function
# def work():
#     print("sleep time start")
#     for i in range(10):
#         print(i)
#         time.sleep(1)
#     print("sleep time stop")


def recharge():
    return PLAYER_HEALTH_MAX


def end():
    if key:
        sounds.win_sound()
        quit()
    return False


def get_map(map_function):
    return map_function()


def reset_xy(node):
    node.x = x
    node.y = y
    return x, y


def get_options(x, y):
    border_nodes = game_map[x][y].get_bordering()
    dir_options = []
    count = 0
    for i in border_nodes:
        # print(i)
        if i == None:
            count = count + 1
        else:
            if count == 0:
                dir_options.append("North")
            elif count == 1:
                dir_options.append("East")
            elif count == 2:
                dir_options.append("South")
            elif count == 3:
                dir_options.append("West")
            count = count + 1

    # print(dir_options)
    return dir_options


def reset_node(direction, border_nodes):
    #border_nodes = game_map[x][y].get_bordering()
    if direction == "North":
        new_node = border_nodes[0]
        x = new_node.x
        y = new_node.y
    elif direction == "East":
        new_node = border_nodes[1]
        x = new_node.x
        y = new_node.y
    elif direction == "South":
        new_node = border_nodes[2]
        x = new_node.x
        y = new_node.y
    elif direction == "West":
        new_node = border_nodes[3]
        x = new_node.x
        y = new_node.y

    return x, y


def move(cur_direction, new_direction):
    if cur_direction == "South":
        if new_direction == "North":
            print(cur_direction, "->", new_direction)
            # turn right twice
            robot.turn_right(STANDARD_TURN)
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "West":
            print(cur_direction, "->", new_direction)
            # turn right
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "East":
            print(cur_direction, "->", new_direction)
            direction = new_direction
            # turn left
            robot.turn_left(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
    elif cur_direction == "North":
        if new_direction == "South":
            print(cur_direction, "->", new_direction)
            # turn right twice
            robot.turn_right(STANDARD_TURN)
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "West":
            print(cur_direction, "->", new_direction)

            # turn left
            robot.turn_left(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "East":
            print(cur_direction, "->", new_direction)

            # turn right
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)

    elif cur_direction == "East":
        if new_direction == "South":
            print(cur_direction, "->", new_direction)
            # turn right
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "West":
            print(cur_direction, "->", new_direction)
            # turn right twice
            robot.turn_right(STANDARD_TURN)
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "North":
            print(cur_direction, "->", new_direction)
            # turn left
            robot.turn_left(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
    elif cur_direction == "West":
        if new_direction == "South":
            print(cur_direction, "->", new_direction)
            # turn left
            robot.turn_left(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "East":
            print(cur_direction, "->", new_direction)
            # turn right twice
            robot.turn_right(STANDARD_TURN)
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)
        elif new_direction == "North":
            print(cur_direction, "->", new_direction)
            # turn right
            robot.turn_right(STANDARD_TURN)
            # move forward
            robot.motor_forward(STANDARD_TURN, STANDARD_SPEED)


def fight_weak_enemy():
    # attacking function
    enemy_hp = 10
    health = player_health
    # animation
    if health > 0:
        while enemy_hp > 0:
            print("Attacking")
            hit = randint(5, 10)
            # sounds
            sounds.deal_damage_sound()
            time.sleep(0.2)
            robot.move_arm_y()
            time.sleep(0.2)
            robot.move_lower_arm_y()
            print("Attack did ", hit, " damage!")
            enemy_hp = enemy_hp - hit
            # sounds
            sounds.hp_sound(str(health), str(enemy_hp))
            if enemy_hp > 0:
                enemy_hit = randint(5, 10)
                print("Enemy damaged me", enemy_hit, " points")
                health = health - enemy_hit
                # sounds
                sounds.recieve_damage_sound()
                print("Player Health: ", health)
                # sounds
                sounds.hp_sound(str(health), str(enemy_hp))
            else:
                print("Enemy Killed!")

    else:
        print("You have died")
        exit()

    print("Player Health: ", health)
    return health


def fight_medium_enemy():
    enemy_hp = 25
    health = player_health
    if health > 0:
        while enemy_hp > 0:
            print("Attacking")
            hit = randint(5, 10)
            # sounds
            sounds.deal_damage_sound()
            time.sleep(0.2)
            robot.move_arm_y()
            time.sleep(0.2)
            robot.move_lower_arm_y()
            print("Attack did ", hit, " damage!")
            enemy_hp = enemy_hp - hit
            # # sounds
            # sounds.hp_sound(str(health), str(enemy_hp))
            if enemy_hp > 0:
                enemy_hit = randint(5, 20)
                # sounds
                sounds.recieve_damage_sound()
                time.sleep(0.2)
                robot.move_lower_arm_y()
                print("Enemy damaged me", enemy_hit, " points")
                health = health - enemy_hit
                # # sounds
                # sounds.hp_sound(str(health), str(enemy_hp))
                print("Player Health: ", health)
            else:
                print("Enemy Killed!")
                root = tk.Tk()
                file = "cats-cute-animals.gif"

                info = Image.open(file)

                frames = info.n_frames  # gives total number of frames that gif contains

                # creating list of PhotoImage objects for each frames
                im = [tk.PhotoImage(
                    file=file, format=f"gif -index {i}") for i in range(frames)]

                count = 0
                anim = None

                def animation(count):
                    global anim
                    im2 = im[count]

                    gif_label.configure(image=im2)
                    count += 1
                    if count == frames:
                        count = 0
                    anim = root.after(50, lambda: animation(count))

                def stop_animation():
                    root.after_cancel(anim)

                def stopit():
                    root.destroy()
                    # root.quit()

                gif_label = tk.Label(root, image="")
                gif_label.pack()

                start = tk.Button(root, text="Click Here",
                                  command=lambda: animation(count))
                start.pack()

                quitb = tk.Button(root, text="Let's Continue!", command=stopit)
                quitb.pack()

                root.mainloop()

    else:
        # sounds
        sounds.self_death_sound()
        print("You have died")
        exit()

    print("Player Health: ", health)
    return health


# Declare Starting Values
key = False
player_health = PLAYER_HEALTH_MAX

# Build map and decide starting direction
game_map = get_map(build_map.generate_level_2)
face_direction = build_map.get_start_direction(game_map)
x, y = build_map.get_start_position(game_map)
#cur_direction = face_direction
print(face_direction)
print(game_map[x][y].get_bordering())
# build_map.node.set_border(game_map[x][y])
# print(game_map[x][y].get_bordering())
# print(game_map[x][y].action)
# print(cur_node)

# initiate initial as North
previous_dir = 'North'

#print(x, y)
#move_options = get_options(x,y)
#border_nodes = game_map[x][y].get_bordering()
# print(border_nodes)
i = 0
running = True
while running:
    #border_nodes = game_map[x][y].get_bordering()
    action = game_map[x][y].action
    #move_options = get_options(x, y)
    print(game_map[x][y].action)
    if action == "Recharge":
        player_health = PLAYER_HEALTH_MAX
        print("Recharge Tile... HP restored.")
    elif action == "Weak_Enemy":
        encounter = input(
            "Encountered a weak enemy, would you like to run or fight? ")
        if encounter == "run":
            num = randint(0, 100)
            if num <= 75:
                x = randint(0, 2)
                y = randint(0, 2)
                #border_nodes = game_map[x][y].get_bordering()
                print("You successfully ran away to a random node")
            else:
                print("escape unsuccessful, you will need to fight")
                encounter = "fight"
                # fight_enemy()
        elif encounter == "fight":
            # robot.move_shoulder_y()
            robot.move_arm_y()

            player_health = fight_weak_enemy()
    elif action == "Medium_Enemy":
        encounter = input(
            "Encountered a medium enemy, would you like to run or fight? ")
        if encounter == "run":
            num = randint(0, 100)
            if num <= 75:
                x = randint(0, 2)
                y = randint(0, 2)
                print("You successfully ran away to a random node")
            else:
                print("escape unsuccessful, you will need to fight")
                encounter = "fight"
        elif encounter == "fight":
            player_health = fight_medium_enemy()
    elif action == "Medium_Enemy_With_Key":
        encounter = input(
            "Encountered the medium enemy holding the key, would you like to run or fight? ")
        if encounter == "run":
            num = randint(0, 100)
            if num <= 75:
                x = randint(0, 2)
                y = randint(0, 2)
                print("You successfully ran away to a random node")
            else:
                print("escape unsuccessful, you will need to fight")
                encounter = "fight"
        elif encounter == "fight":
            player_health = fight_medium_enemy()
            key = True
    elif action == "End":
        print("You have found the escape")
        if key == True:
            sounds.win_sound()
            print("You escape with the key")
            running = False
        elif key == False:
            print("You must get the key before escaping!")

    move_options = get_options(x, y)
    print("Options: ", move_options)
    sounds.suggestions_sound(move_options)
    # choice = input("Enter Direction")
    # print(choice)
    # Using Voice Instead

    print("Waiting...")
    print("Listening for voice commands...")
    while True:
        try:
            controller = VoiceController(robot)
            choice = controller.voice_listener()
            time.sleep(1)  # For Testing
            move(previous_dir, choice)
            # save new previous_dir
            previous_dir = choice
            border_nodes = game_map[x][y].get_bordering()
            x, y = reset_node(choice, border_nodes)
            # print(player_health)
            break  # Only triggered if input is valid...
        except ValueError:
            print("Error: Invalid input")


print("finished")

#direction = "North"
# for i in move_options:
# if i == "North":
#x,y = reset_node("North", border_nodes)

# print(x,y)
#border_nodes = game_map[x][y].get_bordering()
# print(border_nodes)
