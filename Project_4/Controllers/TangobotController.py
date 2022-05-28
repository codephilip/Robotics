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
        #Reset Servo Values
        self.turn = 0
        self.motor = 0
        self.waist = 0
        self.head_y = 0
        self.head_x = 0

        #Reset Servos
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

    #Servo 0 Negative Servo Values for Right Turn
    def turn_right(self):
        self.turn = 0
        if(self.motor != 0):
            self.turn -= int(self.max_displacement/2)
            self.encode_command(0, self.turn)
        else:
            self.turn -= self.max_displacement
            self.encode_command(0, self.turn)

    #Servo 0 Positive Servo Values for Left Turn
    def turn_left(self):
        self.turn = 0
        if (self.motor != 0):
            self.turn += int(self.max_displacement/2)
            self.encode_command(0, self.turn)
        else:
            self.turn += self.max_displacement
            self.encode_command(0, self.turn)

    #Servo 1 Negative Servo Values for Forward
    def motor_forward(self):
        if self.motor > (-1 * self.max_displacement):
            self.motor -= self.increment
            self.encode_command(1, self.motor)

    #Servo 1 Positive Servo Values for Reversing
    def motor_reverse(self):
        if self.motor < self.max_displacement:
            self.motor += self.increment
            self.encode_command(1, self.motor)

    #Servo 2 Negative Servo Values for Waist to Move Left
    def turn_waist_left(self):
        if self.waist > -1 * self.max_displacement:
            self.waist -= (2 * self.increment)
            self.encode_command(2, self.waist)

    #Servo 2 0 Value for Waist to Center
    def turn_waist_center(self):
        self.waist = 0
        self.encode_command(2, self.waist)

    #Servo 2 Positive Servo Values for Waist to Move Right
    def turn_waist_right(self):
        if self.waist < self.max_displacement:
            self.waist += (2 * self.increment)
            self.encode_command(2, self.waist)

    #Servo 3 Negative Servo Values for Head to Turn Left
    def turn_head_left(self):
        if self.head_x > -1 * self.max_displacement:
            self.head_x -= self.increment
            self.encode_command(3, self.head_x)

    #Servo 3 0 Value for Head to Center
    def turn_head_center(self):
        self.head_x = 0
        self.encode_command(3, self.head_x)

    #Servo 3 Positive Servo Values for Head to Turn Right
    def turn_head_right(self):
        if self.head_x < self.max_displacement:
            self.head_x += self.increment
            self.encode_command(3, self.head_x)

    #Servo 4 Negative Servo Values for Head to Tilt Down
    def tilt_head_down(self):
        if self.head_y > -1 * self.max_displacement:
            self.head_y -= self.increment
            self.encode_command(4, self.head_y)

    #Servo 4 Positive Servo Values for Head to Tilt Up
    def tilt_head_up(self):
        if self.head_y < self.max_displacement:
            self.head_y += self.increment
            self.encode_command(4, self.head_y)

    #Stop Movement and Reset Servos
    def stop(self):
        if(self.motor < 0):
            self.motor_reverse()
            time.sleep(.1)
        elif(self.motor > 0):
            self.motor_forward()
            time.sleep(.1)
        else:
            self.reset_servos()
            return

        self.encode_command(1, self.motor)
        return self.stop()
        
    #Encode Commands for Robot Servos and Activate
    def encode_command(self, servo, target_position):
        target_position += self.offset
        
        lsb = target_position & 0x7F
        msb = (target_position >> 7) & 0x7F

        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x0 + servo) + chr(lsb) + chr(msb)

        self.usb.write(cmd.encode('utf-8'))

class KeyboardController:

    def __init__(self, keybind, robot):
        self.keybind = keybind
        self.robot = robot

    def reset(self):
        print("Resetting Servos, please wait...")
        self.robot.reset_servos()
        print("Reset Completed")

    def W_key(self, event):
        self.robot.motor_forward()

    def A_key(self, event):
        self.robot.turn_left()

    def S_key(self, event):
        self.robot.motor_reverse()

    def D_key(self, event):
        self.robot.turn_right()

    def Z_key(self, event):
        self.robot.turn_waist_left()

    def C_key(self, event):
        self.robot.turn_waist_right()

    def X_key(self, event):
        self.robot.turn_waist_center()

    def Up_arrow(self, event):
        self.robot.tilt_head_up()

    def Down_arrow(self, event):
        self.robot.tilt_head_down()

    def Left_Arrow(self, event):
        self.robot.turn_head_left()

    def Right_Arrow(self, event):
        self.robot.turn_head_right()

    def Enter(self, event):
        self.robot.turn_head_center()

    def Spacebar(self, event):
        self.robot.stop()

    def Delete(self, event):
        self.robot.stop()
        sys.exit(0)

keybind = Tk()

#Create robot
robot = Tangobot()

#Create Controller and give control over to robot
controller = KeyboardController(keybind, robot)

#Bind Keyboard Keys to Controller
keybind.bind('<w>', controller.W_key)
keybind.bind('<a>', controller.A_key)
keybind.bind('<s>', controller.S_key)
keybind.bind('<d>', controller.D_key)
keybind.bind('<z>', controller.Z_key)
keybind.bind('<x>', controller.X_key)
keybind.bind('<c>', controller.C_key)
keybind.bind('<Up>', controller.Up_arrow)
keybind.bind('<Down>', controller.Down_arrow)
keybind.bind('<Left>', controller.Left_Arrow)
keybind.bind('<Right>', controller.Right_Arrow)
keybind.bind('<Return>', controller.Enter)
keybind.bind('<space>', controller.Spacebar)
keybind.bind('<BackSpace>', controller.Delete)

keybind.mainloop()
