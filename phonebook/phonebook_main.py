#
# Author:        Daniel Warren
#
# Purpose:      Phonebook demonstrating OOP, tkinter GUI Module, using
#                      tkinter Parent and Child Relationships
#
# Tested OS:   This code was written and tested to run on Windows 10


from tkinter import *
import tkinter as tk
from tkinter import messagebox


#import mods
import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):

        #define master config
        self.master = master
        self.master.minsize(500,300) #height, width
        self.master.maxsize(500,300)

        #center on user display
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")

        #tkinter method if user clicks 'x' btn on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg =self.master

        #load GUI widgets from seperate mod,
        #keeping code compartmentalized
        phonebook_gui.load_gui(self)




if __name__ == '__main__':
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



    
