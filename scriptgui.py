

import os
import tkinter as tk
from tkinter import *
import tkinter.filedialog

class ParentWindow(Frame):
    
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('505x200')
        self.master.title('Check Files')
        self.master.config(bg='#eee')

        self.varFileName1 = StringVar()
        self.varFileName2 = StringVar()
        
        self.btnBrowse1 = Button(self.master, text="Browse...", command=self.OnButtonClick1, width=15, height =1)
        self.btnBrowse1.grid(row= 1, column= 1,padx=(10, 0), pady=(50, 10))
        self.txtFile1 = Entry(self.master, text=self.varFileName1, font=('Helvetica', 16), fg="#00072d",width=28)
        self.txtFile1.grid(row = 1, column = 2, columnspan = 2, padx=(25, 10), pady=(50, 10), sticky = W)
        
        self.btnBrowse2 = Button(self.master, text="Browse...", command=self.OnButtonClick2, width=15, height =1)
        self.btnBrowse2.grid(row= 2, column= 1, padx=(10, 0), pady=(10, 10))
        self.txtFile2 = Entry(self.master, text=self.varFileName2, font=('Helvetica', 16), fg="#00072d",width=28)
        self.txtFile2.grid(row = 2, column = 2, columnspan = 2, padx=(25, 10), sticky = W)
        
        self.btnCheck = Button(self.master, text="Check for Files...",width=15, height =2)
        self.btnCheck.grid(row= 3, column= 1, padx=(10, 0), pady=(10, 10))
        self.btnClose = Button(self.master, text="Close Program",width=15, height =2)
        self.btnClose.grid(row= 3, column= 3, padx=(200, 10),  pady=(10, 10), sticky = S +E)

    def OnButtonClick1(self):
        x = tkinter.filedialog.askdirectory(title='Please select data directory')
        self.txtFile1.delete(0, END)
        self.txtFile1.insert(0, x)

    def OnButtonClick2(self):
        x = tkinter.filedialog.askdirectory(title='Please select data directory')
        self.txtFile2.delete(0, END)
        self.txtFile2.insert(0, x)


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
