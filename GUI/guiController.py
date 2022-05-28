from tkinter import *
import serial, time, sys


# Turn = 0
# Motors = 1
# Waist = 2
# Head Pan = 3
# head Tilt = 4


class Tangobot:

    def __init__(self):
        self.max_displacement = 2000
        self.offset = 6000
        self.increment = 500
        self.waist = 0
        self.head_y = 0
        self.head_x = 0
        self.motor = 0
        self.turn = 0
        self.voice = "0"

        try:
            self.usb = serial.Serial('/dev/ttyACM0')
            print(self.usb.name)
            print(self.usb.baudrate)

        except:
            try:
                self.usb = serial.Serial('/dev/ttyACM1')
                print(self.usb.name)
                print(self.usb.baudrate)
            except:
                print("No servo serial port")
                sys.exit(0)

        self.reset_servos()

    def reset_servos(self):
        # Reset Servo Values
        self.turn = 0
        self.motor = 0
        self.waist = 0
        self.head_y = 0
        self.head_x = 0

        # Reset Servos
        self.encode_command(0, 0)
        time.sleep(.1)
        self.encode_command(1, 0)
        time.sleep(.1)
        self.encode_command(2, 0)
        time.sleep(.1)
        self.encode_command(3, 0)
        time.sleep(.1)
        self.encode_command(4, 0)
        time.sleep(.1)

    # Servo 0 Negative Servo Values for Right Turn
    def turn_right(self):
        self.turn = 0
        if (self.motor != 0):
            self.turn -= int(self.max_displacement / 2)
            self.encode_command(0, self.turn)
        else:
            self.turn -= self.max_displacement
            self.encode_command(0, self.turn)

    # Servo 0 Positive Servo Values for Left Turn
    def turn_left(self):
        self.turn = 0
        if (self.motor != 0):
            self.turn += int(self.max_displacement / 2)
            self.encode_command(0, self.turn)
        else:
            self.turn += self.max_displacement
            self.encode_command(0, self.turn)

    # Servo 1 Negative Servo Values for Forward
    #def motor_forward(self):
    #    if self.motor > (-1 * self.max_displacement):
    #        self.motor -= self.increment
    #        self.encode_command(1, self.motor)

        # Servo 1 Negative Servo Values for Forward
    def motor_forward(self, move_time, speed):
        speeds = [1.33, 1.5, 1.67]
        speed = speeds[speed]
        if self.motor > (-1 * self.max_displacement):
            self.motor -= int(self.increment * speed)
            self.encode_command(0, self.motor)
            time.sleep(move_time)
            self.motor = 0
            self.encode_command(0, 0)

    # Servo 1 Positive Servo Values for Reversing
    #def motor_reverse(self):
    #    if self.motor < self.max_displacement:
    #        self.motor += self.increment
    #        self.encode_command(1, self.motor)

    def motor_reverse(self, move_time, speed):
        speeds = [1.53, 1.7, 1.87]
        speed = speeds[speed]
        if self.motor < self.max_displacement:
            self.motor += int(self.increment * speed)
            self.encode_command(0, self.motor)
            time.sleep(move_time)
            self.motor = 0
            self.encode_command(0, 0)

    # Servo 2 Negative Servo Values for Waist to Move Left
    def turn_waist_right(self):
        if self.waist > -1 * self.max_displacement:
            self.waist -= (2 * self.increment)
            self.encode_command(2, self.waist)

    # Servo 2 0 Value for Waist to Center
    def turn_waist_center(self):
        self.waist = 0
        self.encode_command(2, self.waist)

    # Servo 2 Positive Servo Values for Waist to Move Right
    def turn_waist_left(self):
        if self.waist < self.max_displacement:
            self.waist += (2 * self.increment)
            self.encode_command(2, self.waist)

    # Servo 3 Negative Servo Values for Head to Turn Left
    def turn_head_right(self):
        if self.head_x > -1 * self.max_displacement:
            self.head_x -= self.increment
            self.encode_command(3, self.head_x)

    # Servo 3 0 Value for Head to Center
    def turn_head_center(self):
        self.head_x = 0
        self.encode_command(3, self.head_x)

    # Servo 3 Positive Servo Values for Head to Turn Right
    def turn_head_left(self):
        if self.head_x < self.max_displacement:
            self.head_x += self.increment
            self.encode_command(3, self.head_x)

    # Servo 4 Negative Servo Values for Head to Tilt Down
    def tilt_head_down(self):
        if self.head_y > -1 * self.max_displacement:
            self.head_y -= self.increment
            self.encode_command(4, self.head_y)

    # Servo 4 Positive Servo Values for Head to Tilt Up
    def tilt_head_up(self):
        if self.head_y < self.max_displacement:
            self.head_y += self.increment
            self.encode_command(4, self.head_y)

    # Stop Movement and Reset Servos
    def stop(self):
        if (self.motor < 0):
            self.motor_reverse()
            time.sleep(.1)
        elif (self.motor > 0):
            self.motor_forward()
            time.sleep(.1)
        else:
            self.reset_servos()
            return

        self.encode_command(1, self.motor)
        return self.stop()

    # Encode Commands for Robot Servos and Activate
    def encode_command(self, servo, target_position):
        target_position += self.offset

        lsb = target_position & 0x7F
        msb = (target_position >> 7) & 0x7F

        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x0 + servo) + chr(lsb) + chr(msb)

        self.usb.write(cmd.encode('latin-1'))


class GUIController:

    def __init__(self, robot):
        self.robot = robot

    def execute_commands(self, command_dict_list):
        for command_dict in command_dict_list:
            if command_dict["command"] == "forward":
                speed = command_dict["speed"]
                move_time = command_dict["time"]
                print("Command: Forward")
                print("Speed: ", speed)
                print("Time: ", move_time)
                self.robot.motor_forward(move_time, speed)
                time.sleep(1)
            elif command_dict["command"] == "reverse":
                speed = command_dict["speed"]
                move_time = command_dict["time"]
                print("Command: Forward")
                print("Speed: ", speed)
                print("Time: ", move_time)
                self.robot.motor_reverse(move_time, speed)
                time.sleep(1)
            elif command_dict["command"] == "right":
                #speed = command_dict["speed"]
                #move_time = command_dict["time"]
                self.robot.turn_right()
                time.sleep(1)
            elif command_dict["command"] == "left":
                #speed = command_dict["speed"]
                #move_time = command_dict["time"]
                self.robot.turn_left()
                time.sleep(1)
            elif command_dict["command"] == "waist_right":
                self.robot.turn_waist_right()
                time.sleep(1)
            elif command_dict["command"] == "waist_left":
                self.robot.turn_waist_left()
                time.sleep(1)
            elif command_dict["command"] == "head_right":
                self.robot.turn_head_right()
                time.sleep(1)
            elif command_dict["command"] == "head_left":
                self.robot.turn_head_left()
                time.sleep(1)
            elif command_dict["command"] == "head_center":
                self.robot.turn_head_center()
                time.sleep(1)
            elif command_dict["command"] == "head up":
                self.robot.tilt_head_up()
                time.sleep(1)
            elif command_dict["command"] == "head down":
                self.robot.tilt_head_down()
                time.sleep(1)
            elif command_dict["command"] == "wait":
                time.sleep(3)


