from tkinter import *
import serial, time, sys


# Turn = 0
# Motors = 1
# Waist = 2
# Head Pan = 3
# head Tilt = 4


class TangoController:

    def __init__(self, window):
        self.window = window
        self.waist = 6000
        self.head_vert = 6000
        self.head_horiz = 6000
        self.motor_forward = 6000
        self.motor_turn = 6000

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
        print("Resetting Servos, please wait")
        self.waist = 6000
        self.head_vert = 6000
        self.head_horiz = 6000
        self.motor_forward = 6000
        self.motor_turn = 6000
        self.usb_write(0, self.waist)
        time.sleep(.1)
        self.usb_write(1, self.motor_forward)
        time.sleep(.1)
        self.usb_write(2, self.motor_turn)
        time.sleep(.1)
        self.usb_write(3, self.head_horiz)
        time.sleep(.1)
        self.usb_write(4, self.head_vert)
        time.sleep(.1)
        print("Reset Completed")

    def forward(self, event):
        if self.motor_forward > 4000:
            self.motor_forward -= 500
            self.usb_write(1, self.motor_forward)

    def backward(self, event):
        if self.motor_forward < 8000:
            self.motor_forward += 500
            self.usb_write(1, self.motor_forward)

    def turn_right(self, event):
        self.motor_turn = 6000
        if(self.motor_forward != 6000):
            self.motor_turn -= 1000
            self.usb_write(0, self.motor_turn)
        else:
            self.motor_turn -= 2000
            self.usb_write(0, self.motor_turn)
        return

    def turn_left(self, event):
        self.motor_turn = 6000
        if (self.motor_forward != 6000):
            self.motor_turn += 1000
            self.usb_write(0, self.motor_turn)
        else:
            self.motor_turn += 2000
            self.usb_write(0, self.motor_turn)

    def head_up(self, event):
        if self.head_vert < 8000:
            self.head_vert += 500
            self.usb_write(4, self.head_vert)

    def head_down(self, event):
        if self.head_vert > 4000:
            self.head_vert -= 500
            self.usb_write(4, self.head_vert)

    def head_left(self, event):
        if self.head_horiz > 4000:
            self.head_horiz -= 500
            self.usb_write(3, self.head_horiz)
            

    def head_right(self, event):
        if self.head_horiz < 8000:
            self.head_horiz += 500
            self.usb_write(3, self.head_horiz)
            

    def waist_left(self, event):
        self.waist -= 500
        self.usb_write(2, self.waist)

    def waist_right(self, event):
        self.waist += 500
        self.usb_write(2, self.waist)

    def stop_action(self, event):
        # stop the robot slowly
        self.stop()
        
    def stop(self):
        if(self.motor_forward > 6000):
            self.motor_forward -= 500
            time.sleep(.1)
        elif(self.motor_forward < 6000):
            self.motor_forward += 500
            time.sleep(.1)
        else:
            self.reset_servos()
            return
        
        print(self.motor_forward)

        self.usb_write(1, self.motor_forward)
        return self.stop()
        

    def usb_write(self, servo, target):

        lsb = target & 0x7F
        msb = (target >> 7) & 0x7F

        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x0 + servo) + chr(lsb) + chr(msb)

        print("writing")
        self.usb.write(cmd.encode('utf-8'))


win = Tk()
# New instance of TangoController
controller = TangoController(win)

# Robot moving and turning
win.bind('<Up>', controller.forward)
win.bind('<Down>', controller.backward)
win.bind('<Left>', controller.turn_left)
win.bind('<Right>', controller.turn_right)

# Robot head and waist movement
win.bind('<Key-w>', controller.head_up)
win.bind('<Key-s>', controller.head_down)
win.bind('<Key-a>', controller.head_left)
win.bind('<Key-d>', controller.head_right)
win.bind('<Key-q>', controller.waist_left)
win.bind('<Key-e>', controller.waist_right)

# Stop function that slows the robot down
win.bind('<space>', controller.stop_action)

win.mainloop()
