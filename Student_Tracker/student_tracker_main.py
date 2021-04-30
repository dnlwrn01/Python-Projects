##
##
##
##
##
##
##

#import mods
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#custom mods
import student_tracker_gui
import student_tracker_func

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):

    #define master config
        self.master = master
        self.master.minsize(400,270) #height, width
        self.master.maxsize(400,270)

        #center on user display
        student_tracker_func.center_window(self, 400,270)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")

        #tkinter method if user clicks 'x' btn on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracker_func.ask_quit(self))
        arg =self.master

        #load GUI widgets from seperate mod,
        #keeping code compartmentalized
        student_tracker_gui.load_gui(self)

if __name__ == '__main__':
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        
