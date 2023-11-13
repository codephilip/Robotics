# Import module
from tkinter import *
import time
#import TangoBotController as tango
#from TangoBotController import VoiceController
from gtts import gTTS
from playsound import playsound

# Create object
root = Tk()
#robot = tango.Tangobot()

# Adjust size
root.geometry("400x400")
command_list = []
list_box = Listbox(root)
list_box.pack(pady=25)


def text_to_speech(string):
    voice = gTTS(text=string)
    voice.save('AudioOutput.mp3')
    playsound('AudioOutput.mp3')


def execute_commands():
    for command_dict in command_list:
        if command_dict["command"] == "Forward":
            speed = command_dict["speed"]
            move_time = command_dict["time"]
            print("Command: Forward")
            print("Speed: ", speed)
            print("Time: ", move_time)
            #robot.motor_forward(move_time, speed)
            time.sleep(1)
        elif command_dict["command"] == "Reverse":
            speed = command_dict["speed"]
            move_time = command_dict["time"]
            print("Command: Forward")
            print("Speed: ", speed)
            print("Time: ", move_time)
            #self.robot.motor_reverse(move_time, speed)
            time.sleep(1)
        elif command_dict["command"] == "Turn Right":
            # speed = command_dict["speed"]
            move_time = command_dict["time"]
            # self.robot.turn_right()
            time.sleep(1)
        elif command_dict["command"] == "Turn Left":
            # speed = command_dict["speed"]
            move_time = command_dict["time"]
            # self.robot.turn_left()
            time.sleep(1)
        elif command_dict["command"] == "Waist Right":
            # self.robot.turn_waist_right()
            time.sleep(1)
        elif command_dict["command"] == "Waist Left":
            # self.robot.turn_waist_left()
            time.sleep(1)
        elif command_dict["command"] == "Look Right":
            print("Turn Head Right")
            # self.robot.turn_head_right()
            time.sleep(1)
        elif command_dict["command"] == "Look Left":
            # self.robot.turn_head_left()
            time.sleep(1)
        elif command_dict["command"] == "Look Center":
            # self.robot.turn_head_center()
            time.sleep(1)
        elif command_dict["command"] == "Look Up":
            # self.robot.tilt_head_up()
            time.sleep(1)
        elif command_dict["command"] == "Look Down":
            # self.robot.tilt_head_down()
            time.sleep(1)
        elif command_dict["command"] == "Speak":
            text_to_speech("Hello World")

        elif command_dict["command"] == "Wait":
            print("Waiting...")
            print("Listening for voice commands...")
            #controller = VoiceController(robot)
            # controller.voice_listener()
            time.sleep(4)


# Change the label text
def show():
    label.config(text=command_choice.get())


def add():
    command_dict = {}
    choice = command_choice.get()
    print(choice)
    speed = 0
    if len(command_list) < 8 and choice != "Commands":
        if choice == 'Forward' or choice == 'Reverse':

            #print("Choice is here")
            speed = speed_choice.get()
            time = time_choice.get()
            try:
                command_dict = {"command": choice,
                                "speed": int(speed), "time": float(time)}
                message = choice + " Speed: " + speed + ", Time: " + time
                command_list.append(command_dict)
                list_box.insert(END, message)
                command_choice.set("Commands")
                speed_choice.set("Speed")
                time_choice.set("Time")
            except Exception as e:
                if "could not convert string to float: 'Time'" in e.args:
                    print("Error: Must select a time for this command")
                    label.config(
                        text="Error: Must select a time for this command")
                else:
                    print("Error: Must select a speed for this command")
                    label.config(
                        text="Error: Must select a speed for this command")
            #message = choice + " Speed: " + speed
        elif choice == 'Turn Left' or choice == 'Turn Right':

            #print("Choice is here")
            time = time_choice.get()
            try:
                command_dict = {"command": choice, "time": float(time)}
                message = choice + ", Time: " + time
                command_list.append(command_dict)
                list_box.insert(END, message)
                command_choice.set("Commands")
                speed_choice.set("Speed")
                time_choice.set("Time")
            except Exception as e:
                if "could not convert string to float: 'Time'" in e.args:
                    print("Error: Must select a time for this command")
                    label.config(
                        text="Error: Must select a time for this command")
        else:
            #speed = int(speed_choice.get())
            command_dict = {"command": choice}
            message = choice
            command_list.append(command_dict)
            list_box.insert(END, message)
            command_choice.set("Commands")
            speed_choice.set("Speed")
            time_choice.set("Time")
        # if action == "forward":
    # if len(command_list) < 8 and command_dict != {}:
        # command_list.append(command_dict)
        #message = choice + " Speed: " + speed
            #list_box.insert(END, message)
        print(command_list)
    else:
        if len(command_list) >= 8:
            label.config(text="Too many commands!")
        else:
            label.config(text="Invalid Command")


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
    "Speak",
    "Shoulder"
]
speed_options = [1, 2, 3]
time_options = [.5, 1, 1.5, 2, 2.5, 3]

# datatype of menu text
command_choice = StringVar()
speed_choice = StringVar()
time_choice = StringVar()


# initial menu text
command_choice.set("Commands")
speed_choice.set("Speed")
time_choice.set("Time")

# Create Dropdown menu
drop = OptionMenu(root, command_choice, *options)
drop.pack()
speed_drop = OptionMenu(root, speed_choice, *speed_options)
speed_drop.pack()
time_drop = OptionMenu(root, time_choice, *time_options)
time_drop.pack()
# Create button, it will change label text
button = Button(root, text="Add Command", command=add).pack()
execute_button = Button(root, text="Execute Commands",
                        command=execute_commands).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()
