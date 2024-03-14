import tkinter as tk
import random


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("275x250")
        self.master.title("Lab 9")
        self.button_name = tk.Button(self.master, text="Enter",
                                     command=self.button_function)
    
        self.button_name.place(x=100, y=65)

        self.hello_label = tk.Label(self.master,
                                    text="Enter your name to get a salutation")
        self.hello_label.place(x=25, y=125)

        self.app_str = tk.StringVar()
        self.app_entry = tk.Entry (self.master,
                                   width=27, textvariable=self.app_str)
        self.app_entry.place(x=20, y=25)


    def button_function(self):
        greetings = ["Hello", "Howdy", "Salutations"]
        salute = random.choice(greetings) + " " + self.app_str.get()
        self.hello_label["text"] = salute
        
        
         
                       

app = Application(master=tk.Tk())

app.mainloop()
        
