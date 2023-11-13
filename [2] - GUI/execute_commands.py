import time


def execute_commands(command_dict_list):
    for command_dict in command_dict_list:
        if command_dict["command"] == "forward":
            speed = command_dict["speed"]
            move_time = command_dict["time"]
            print("Command: Forward")
            print("Speed: ", speed)
            print("Time: ", move_time)
            #self.robot.motor_forward(move_time, speed)
            time.sleep(1)
        elif command_dict["command"] == "reverse":
            speed = command_dict["speed"]
            move_time = command_dict["time"]
            print("Command: Forward")
            print("Speed: ", speed)
            print("Time: ", move_time)
            #self.robot.motor_reverse(move_time, speed)
            time.sleep(1)
        elif command_dict["command"] == "right":
            # speed = command_dict["speed"]
            # move_time = command_dict["time"]
            #self.robot.turn_right()
            time.sleep(1)
        elif command_dict["command"] == "left":
            # speed = command_dict["speed"]
            # move_time = command_dict["time"]
            #self.robot.turn_left()
            time.sleep(1)
        elif command_dict["command"] == "waist_right":
            #self.robot.turn_waist_right()
            time.sleep(1)
        elif command_dict["command"] == "waist_left":
            #self.robot.turn_waist_left()
            time.sleep(1)
        elif command_dict["command"] == "head_right":
            print("Turn Head Right")
            #self.robot.turn_head_right()
            time.sleep(1)
        elif command_dict["command"] == "head_left":
            #self.robot.turn_head_left()
            time.sleep(1)
        elif command_dict["command"] == "head_center":
            #self.robot.turn_head_center()
            time.sleep(1)
        elif command_dict["command"] == "head up":
            #self.robot.tilt_head_up()
            time.sleep(1)
        elif command_dict["command"] == "head down":
            #self.robot.tilt_head_down()
            time.sleep(1)
        elif command_dict["command"] == "wait":
            print("Waiting...")
            print("Listening for voice commands...")
            time.sleep(4)


command_dictionary_list = []
dict_1 = {"command": "forward", "speed": 1, "time": 3}
dict_2 = {"command": "reverse", "speed": 3, "time": 5}
dict_3 = {"command": "head_right"}
dict_4 = {"command": "wait"}
command_dictionary_list.append(dict_1)
command_dictionary_list.append(dict_2)
command_dictionary_list.append(dict_3)
command_dictionary_list.append(dict_4)
print(command_dictionary_list)
execute_commands(command_dictionary_list)

