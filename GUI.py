import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.logo = tk.Label(self, text="TangoBot GUI", background="orange")
        

        self.other0 = tk.Text(self, width = 30, height = 10, background="white", takefocus=0)        
        self.other1 = tk.Label(self,text="HEAD", background="purple")
        self.other2 = tk.Label(self,text="WAIST", background="yellow")
        self.other3 = tk.Label(self,text="MOTOR", background="pink")
        self.other4 = tk.Label(self, background="pink")
        self.other5 = tk.Label(self, background="gray")
        self.other6 = tk.Label(self, background="blue")
        self.main = tk.Frame(self, background="blue")
        

        self.button1 = tk.Button(self, text="Stop", background="red")
        self.button2 = tk.Button(self, text="Execute Queue", background="green")

        # self.buttons = []
        # for i in range(3):
        #     self.buttons.append(tk.Button(self, text="Button %s" % (i+1,), background="green"))


        self.logo.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.other0.grid(row=2, column=0, rowspan=5, sticky="nsew")
        self.other1.grid(row=0, column=1, rowspan=3, sticky="nsew")
        self.other2.grid(row=3, column=1, rowspan=3, sticky="nsew")
        self.other3.grid(row=6, column=1, rowspan=3,  sticky="nsew")
        self.other4.grid(row=0, column=2, rowspan=3,sticky="nsew")
        self.other5.grid(row=3, column=2, rowspan=3,sticky="nsew")
        self.other6.grid(row=6, column=2, rowspan=3,  sticky="nsew")
        self.button1.grid(row=7, column=0, sticky="nsew")
        self.button2.grid(row=8, column=0, sticky="nsew")

        # self.buttons[3].grid(row=5, column=0, sticky="nsew")
        # self.buttons[4].grid(row=6, column=0, sticky="nsew")
        # self.buttons[5].grid(row=7, column=0, sticky="nsew")
        # self.buttons[6].grid(row=8, column=0, sticky="nsew")
        self.main.grid(row=2, column=2, columnspan=2, rowspan=8)

        for row in range(9):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)

        # colorLog = Text(self.other0, width = 30, height = 10, takefocus=0, bg='white')
        # # colorLog.grid(row=0, column=1, padx=10, pady=20)





if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.geometry("800x400")
    root.mainloop()