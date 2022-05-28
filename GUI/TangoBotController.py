import serial
import time
import sys
import speech_recognition as sr


# Turn = 1
# Motors = 0
# Waist = 2
# Head Pan = 3
# head Tilt = 4
# Shoulder = 5
# Arm = 6

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
        self.shoulder_y = 0
        self.arm = 0

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
    def turn_right(self, runtime):
        self.turn -= int(self.max_displacement/2)
        self.encode_command(1, self.turn)
        time.sleep(runtime)
        self.turn = 0
        self.encode_command(1, 0)

    # Servo 0 Positive Servo Values for Left Turn
    def turn_left(self, runtime):
        self.turn += int(self.max_displacement/2)
        self.encode_command(1, self.turn)
        time.sleep(runtime)
        self.turn = 0
        self.encode_command(1, 0)

    # Servo 1 Negative Servo Values for Forward
    def motor_forward(self, runtime, speed):
        speeds = [1.33, 1.5, 1.67]
        speed = speeds[speed]
        if self.motor > (-1 * self.max_displacement):
            self.motor -= int(self.increment * speed)
            self.encode_command(0, self.motor)
            time.sleep(runtime)
            self.motor = 0
            self.encode_command(0, 0)

    # Servo 1 Positive Servo Values for Reversing
    def motor_reverse(self, runtime, speed):
        speeds = [1.53, 1.7, 1.87]
        speed = speeds[speed]
        if self.motor < self.max_displacement:
            self.motor += int(self.increment * speed)
            self.encode_command(0, self.motor)
            time.sleep(runtime)
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

    def attack(self):
        if self.shoulder_y > -1 * self.max_displacement:
            self.shoulder_y -= self.increment
            self.encode_command(5, self.shoulder_y)

    # Encode Commands for Robot Servos and Activate
    def encode_command(self, servo, target_position):
        target_position += self.offset

        lsb = target_position & 0x7F
        msb = (target_position >> 7) & 0x7F

        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + \
            chr(0x0 + servo) + chr(lsb) + chr(msb) + chr(0x05)
        # chr(0x05) shoulder?

        self.usb.write(cmd.encode('latin-1'))


class VoiceController:

    def __init__(self, robot):
        self.robot = robot
        self.voice = 0

    def voice_listener(self):
        listen = True
        while listen == True:
            with sr.Microphone() as source:
                speech_recognizer = sr.Recognizer()
                speech_recognizer.adjust_for_ambient_noise(source)
                speech_recognizer.dyanmic_energythreshhold = 3000
                try:
                    print("Listening Mode Engaged")
                    command = speech_recognizer.listen(source)
                    print("Understood")
                    self.voice = speech_recognizer.recognize_google(command)
                    print(self.voice)
                    listen = False
                except sr.UnknownValueError:
                    print("Could not understand command")


"""
# Create robot
robot = Tangobot()

# Create Controller and give control over to robot
controller = VoiceController(robot)
controller.voice_listener()

#controller = KeyboardController(keybind, robot)

#Bind Keyboard Keys to Controller
#keybind.bind('<w>', controller.W_key)
#keybind.bind('<a>', controller.A_key)
#keybind.bind('<s>', controller.S_key)
#keybind.bind('<d>', controller.D_key)
#keybind.bind('<z>', controller.Z_key)
#keybind.bind('<x>', controller.X_key)
#keybind.bind('<c>', controller.C_key)
#keybind.bind('<Up>', controller.Up_arrow)
#keybind.bind('<Down>', controller.Down_arrow)
#keybind.bind('<Left>', controller.Left_Arrow)
#keybind.bind('<Right>', controller.Right_Arrow)
#keybind.bind('<Return>', controller.Enter)
#keybind.bind('<space>', controller.Spacebar)
#keybind.bind('<BackSpace>', controller.Delete)

#keybind.mainloop()
"""
