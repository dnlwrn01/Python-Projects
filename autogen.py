
import webbrowser
import tkinter as tk
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('200x200')
        self.master.title('Custom Website')
        self.master.config(bg='lightgrey')

        self.varCustomText = StringVar()
        
        self.txtCustomText = Entry(self.master,text=self.varCustomText, font=('Helvetica', 16), fg="#00072d")
        self.txtCustomText.pack(side=TOP)
        self.btnCreate = Button(self.master, text="Create", command=self.openWeb)
        self.btnCreate.pack(side=BOTTOM)

    def openWeb(self):
        newFile = open("auto.html", "w")

        newFile.write(f"<html><body><h1>{self.txtCustomText.get()}</h1></body></html>")

        newFile.close()

        webbrowser.open("auto.html")


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
