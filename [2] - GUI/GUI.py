from tkinter import *

class Example():
    def __init__(self):
        self.root = Tk()
        self.root.title("TangoBot GUI")
        #self.Tangobot()

        #self.e = Entry(self.root, width=50, borderwidth=10)
        #self.e.grid(row=0, column=0, columnspan=4,padx=10, pady=10)
        # menu left
        self.menu_left = Frame(self.root, width=150, bg="#ababab")
        self.menu_left_upper = Frame(self.menu_left, width=200, height=150, bg="red")
        self.menu_left_lower = Frame(self.menu_left, width=200, bg="blue")
        self.test = Label(self.menu_left_upper, text="Head")
        self.test.pack()
        
        self.button_head_up = Button(self.menu_left_upper, text="Up", pady=10)
        self.button_head_up.pack()
        self.button_head_down = Button(self.menu_left_upper, text="Down",pady=10)
        self.button_head_down.pack()
        self.button_head_left = Button(self.menu_left_upper, text="Left",pady=10)
        self.button_head_left.pack()
        self.button_head_right = Button(self.menu_left_upper, text="Right",pady=10)
        self.button_head_right.pack()
        self.menu_left_upper.pack(side="top", fill="both", expand=True)
        self.menu_left_lower.pack(side="bottom", fill="both", expand=True)

        #center area
        self.menu_center = Frame(self.root, width=150, bg="#ababab")
        self.menu_center_upper = Frame(self.menu_center, width=200, height=150, bg="blue")
        self.menu_center_lower = Frame(self.menu_center, width=200, bg="red")
        self.test = Label(self.menu_center_upper, text="Motor")
        self.test.pack()
        self.button_motor_forward = Button(self.menu_center_upper, text="Forward", pady=10, command=self.stop)
        self.button_motor_forward.pack()
        self.button_motor_backward = Button(self.menu_center_upper, text="Backward",  pady=10)
        self.button_motor_backward.pack()
        self.menu_center_upper.pack(side="top", fill="both", expand=True)
        self.menu_center_lower.pack(side="bottom", fill="both", expand=True)

        #right area
        self.menu_right = Frame(self.root, width=150, bg="#ababab")
        self.menu_right_upper = Frame(self.menu_right, width=200, height=150, bg="red")
        self.menu_right_lower = Frame(self.menu_right, width=200, bg="blue")
        self.test = Label(self.menu_right_upper, text="Waist")
        self.test.pack()

        self.button_waist_right = Button(self.menu_right_upper, text="Right", pady=10)
        self.button_waist_right.pack()
        self.button_waist_left = Button(self.menu_right_upper, text="Left",  pady=10)
        self.button_waist_left.pack()

        self.menu_right_upper.pack(side="top", fill="both", expand=True)
        self.menu_right_lower.pack(side="bottom", fill="both", expand=True)

        # canvas area
        self.some_title_frame =Frame(self.root, bg="#dfdfdf")
        self.some_title = Label(self.some_title_frame, text="GUI", bg="#dfdfdf")
        self.some_title.pack()
        self.text_log = Text(self.root, width=50, height=400)

        # status bar
        self.status_frame = Frame(self.root)
        self.status = Label(self.status_frame, text="Thank you!")
        self.status.pack(fill="both", expand=True)
        
        #the grid
        self.menu_left.grid(row=1, column=0, rowspan=2, sticky="nsew")
        self.menu_center.grid(row=1, column=1, rowspan=2, sticky="nsew")
        self.menu_right.grid(row=1, column=2, rowspan=2, sticky="nsew")
        
        self.some_title_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.status_frame.grid(row=3, column=0, columnspan=3, sticky="ew")
        
        self.text_log.grid(row=0, column=3, rowspan=2, sticky="ew") 
        self.button_execute = Button(self.menu_left_upper, text="HeaderButton", pady=10)
        self.button_execute.pack()

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

    def executeQueue():
        return
        #root.insert(0.0, "EXECUTE\n")

    def stop(self):
        self.text_log.insert(0.0, "STOP\n")


x = Example()
x.stop()
