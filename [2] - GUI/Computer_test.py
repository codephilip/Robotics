from tkinter import *
import time
#import TangoBotController as tango
#from TangoBotController import VoiceController
#import PIL.Image
from PIL import ImageTk, Image
from gtts import gTTS
import os
import pyglet
from time import sleep

#Edit max size
MAX_ITEMS = 20

# Create object
root = Tk()
#robot = tango.Tangobot()

# Adjust size
root.attributes('-fullscreen', True)
#root.geometry("400x700")
command_list = []
list_box = Listbox(root)
list_box.config(width=40, height=6)
list_box.pack(pady=25)
#img = ImageTk.PhotoImage(Image.open("eyes.jpg"))

def delete():
    for i in list_box.curselection():
        command_list.pop(i)
    list_box.delete(ANCHOR)
    print(command_list)

def reset_commands():
    list_box.delete(0, END)
    command_list.clear()
    print(command_list)

def text_to_speech(string):
    voice = gTTS(text = string)
    voice.save('AudioOutput.mp3')
    music = pyglet.media.load('AudioOutput.mp3', streaming=False)
    music.play()
    sleep(music.duration)
    os.remove('AudioOutput.mp3')
    
def execute_commands():

    animation = True

    if animation:
        #newWindow = Toplevel(root)
        #newWindow.geometry("400X700")
        img = ImageTk.PhotoImage(Image.open("eyes.jpg"))

        picture_label = Label(root, image= img)
        #picture_label.config(height=600, width=700)
        picture_label.pack()


    #picture_label = Label(root, image= img)
    #picture_label.pack()
    
    for index in range(len(command_list)):
        list_box.delete(index)
        message = "--> " + str(index+1) + ": " + command_list[index]["command"] + ", "
        for i in command_list[index]:
            if i != "command":
                message = message + i + ": " + str(command_list[index][i]) + ", "
        list_box.insert(index, message)
        root.update()
        if command_list[index]["command"] == "Forward":
            speed = command_list[index]["speed"]
            move_time = command_list[index]["time"]
            print("Command: Forward")
            print("Speed: ", speed)
            print("Time: ", move_time)
            #robot.motor_forward(move_time, speed)
            time.sleep(1)
        elif command_list[index]["command"] == "Reverse":
            speed = command_list[index]["speed"]
            move_time = command_list[index]["time"]
            print("Command: Forward")
            print("Speed: ", speed)
            print("Time: ", move_time)
            #robot.motor_reverse(move_time, speed)
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Turn Right":
            # speed = command_dict["speed"]
            move_time = command_list[index]["time"]
            #robot.turn_right()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Turn Left":
            # speed = command_dict["speed"]
            move_time = command_list[index]["time"]
            #robot.turn_left()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Waist Right":
            #robot.turn_waist_right()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Waist Left":
            #robot.turn_waist_left()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Look Right":
            print("Turn Head Right")
            #robot.turn_head_right()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Look Left":
            #robot.turn_head_left()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Look Center":
            #robot.turn_head_center()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Look Up":
            #robot.tilt_head_up()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Look Down":
            #robot.tilt_head_down()
            time.sleep(1) #For Testing
        elif command_list[index]["command"] == "Speak":
            text_to_speech("Hello World")
        elif command_list[index]["command"] == "Wait":
            print("Waiting...")
            print("Listening for voice commands...")
            #controller = VoiceController(robot)
            #controller.voice_listener()
            time.sleep(4) #For Testing
        list_box.delete(index)
        message = str(index+1) + ": " + command_list[index]["command"] + ", "
        for i in command_list[index]:
            if i != "command":
                message = message + i + ": " + str(command_list[index][i]) + ", "
        list_box.insert(index, str(message))


# Change the label text
def show():
    label.config(text=command_choice.get())

def add():
    command_dict = {}
    choice = command_choice.get()
    print(choice)
    print(position_choice.get())
    position = position_choice.get()
    speed = 0
    if(len(command_list) < MAX_ITEMS and choice != "Commands"):
        if position != "Position":
            if int(position) < len(command_list)+1:
                pos = int(position)
            else:
                label.config(text="Invalid Position, Adding to end")
                print("Invalid Position, Adding to end")
                pos = int(len(command_list) + 1)
        else:
            pos = int(len(command_list) + 1)
        if choice == 'Forward' or choice == 'Reverse':
            speed = speed_choice.get()
            time = time_choice.get()
            try:
                command_dict = {"command": choice, "speed": int(speed), "time": float(time)}
                message = choice + " Speed: " + speed + ", Time: " + time
                command_list.insert(pos-1,command_dict)
                command_choice.set("Commands")
                speed_choice.set("Speed")
                time_choice.set("Time")
                position_choice.set("Position")
            except Exception as e:
                if "could not convert string to float: 'Time'" in e.args:
                    print("Error: Must select a time for this command")
                    label.config(text= "Error: Must select a time for this command")
                elif "could not convert string to float: 'Speed'" in e.args:
                    print("Error: Must select a speed for this command")
                    label.config(text= "Error: Must select a speed for this command")
                    print()
                else:
                    print("Error:", e)

        elif choice == 'Turn Left' or choice == 'Turn Right':
            time = time_choice.get()
            try:
                command_dict = {"command": choice,"time": float(time)}
                command_list.insert(pos-1, command_dict)
                command_choice.set("Commands")
                speed_choice.set("Speed")
                time_choice.set("Time")
                position_choice.set("Position")
            except Exception as e:
                if "could not convert string to float: 'Time'" in e.args:
                    print("Error: Must select a time for this command")
                    label.config(text="Error: Must select a time for this command")
                else:
                    print("ERROR:", e)
        else:
            command_dict = {"command": choice}
            command_list.insert(pos-1,command_dict)
            command_choice.set("Commands")
            speed_choice.set("Speed")
            time_choice.set("Time")
            position_choice.set("Position")
    else:
        if len(command_list) >= MAX_ITEMS:
            print("Too many commands!")
            label.config(text="Too many commands!")
        else:
            label.config(text="Invalid Command")
    list_box.delete(0, END)
    for item in range(len(command_list)):
        message = str(item+1) + ": " + command_list[item]["command"] + ", "
        for i in command_list[item]:
            if i != "command":
                message = message + i + ": " + str(command_list[item][i]) + ", "
        list_box.insert(item, str(message))
    print(command_list)

def change_state(*args):
    command_container = command_choice.get()
    if command_container == 'Forward' or command_container == 'Reverse':
        speed_drop.configure(state = "active")
        time_drop.configure(state = "active")
    elif command_container == 'Turn Right' or command_container == 'Turn Left':
        speed_drop.configure(state = "disabled")
        time_drop.configure(state = "active")
        speed_choice.set("Speed")
    else:
        speed_drop.configure(state = "disabled")
        time_drop.configure(state = "disabled")
        speed_choice.set("Speed")
        time_choice.set("Time")

# Dropdown menu options
options = [
    "Forward",
    "Reverse",
    "Turn Left",
    "Turn Right",
    "Waist Right",
    "Waist Left",
    "Look Left",
    "Look Right",
    "Look Up",
    "Look Down",
    "Look Center",
    "Wait",
    "Speak"
]
speed_options = [1, 2, 3]
time_options = [.5,1,1.5,2,2.5,3]
position_options = [item for item in range(1, MAX_ITEMS+1)]

# datatype of menu text
command_choice = StringVar()
speed_choice = StringVar()
time_choice = StringVar()
position_choice = StringVar()

# initial menu text
command_choice.set("Commands")
speed_choice.set("Speed")
time_choice.set("Time")
position_choice.set("Position")

# Create Dropdown menu
drop = OptionMenu(root, command_choice, *options)
drop.configure(width = 30, height = 1)
drop.pack()
speed_drop = OptionMenu(root, speed_choice, *speed_options)
speed_drop.configure(width = 30, height = 1, state = "disabled")
speed_drop.pack()
time_drop = OptionMenu(root, time_choice, *time_options)
time_drop.configure(width = 30, height = 1, state = "disabled")
time_drop.pack()
position_drop = OptionMenu(root, position_choice, *position_options)
position_drop.configure(width = 30, height = 1)
position_drop.pack()

command_choice.trace("w", change_state)

# Create button, it will change label text
button = Button(root, text="Add Command", command=add, width = 32, height = 1).pack()
delete_button = Button(root, text="Delete Command", command=delete, width = 32, height = 1).pack()
reset_button = Button(root, text="Reset Commands", command=reset_commands, width = 32, height = 1).pack()
execute_label = Label(root, text=" ").pack()
execute_button = Button(root, text="Execute Commands", command=execute_commands, width = 32, height = 2).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()
