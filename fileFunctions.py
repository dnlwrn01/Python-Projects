#import modules
import os
import time
import shutil
import datetime
import tkinter
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('350x200')
        self.master.title('Check Files')
        self.master.config(bg='#eee')

        self.varFileName1 = StringVar()
        self.varFileName2 = StringVar()

        self.lblMain = Label(self.master, text="Select a folder to check, \n& another folder to accept the copied files.")
        self.lblMain.grid(row =1, column = 1, columnspan = 3, pady = (0, 45))
        self.btnBrowse1 = Button(self.master, text="Browse...", command=self.OnButtonClick1, width=8, height =1)
        self.btnBrowse1.grid(row= 1, column= 1,padx=(1, 0), pady=(50, 10))
        self.txtFile1 = Entry(self.master, text=self.varFileName1, font=('Helvetica', 16), fg="#00072d",width= 17)
        self.txtFile1.grid(row = 1, column = 2, columnspan = 2, padx=(1, 5), pady=(50, 10), sticky = W)
        
        self.btnBrowse2 = Button(self.master, text="Browse...", command=self.OnButtonClick2, width=8, height =1)
        self.btnBrowse2.grid(row= 2, column= 1, padx=(1, 0), pady=(10, 10))
        self.txtFile2 = Entry(self.master, text=self.varFileName2, font=('Helvetica', 16), fg="#00072d",width=17)
        self.txtFile2.grid(row = 2, column = 2, columnspan = 2, padx=(1, 5), sticky = W)
        
        self.btnClose = Button(self.master, text="Exit",command=self.askQuit, width=12, height =2)
        self.btnClose.grid(row= 5, column= 1, padx=(20, 5), pady=(5, 10), sticky = S + E)
        self.btnMove = Button(self.master, text="Move Files",command=self.moveFiles, width=12, height =2)
        self.btnMove.grid(row= 5, column= 3, padx=(120, 5),  pady=(5, 10), sticky = S + W)

    def OnButtonClick1(self):
        self.startPath = tkinter.filedialog.askdirectory(title='Please select data directory')
        self.txtFile1.delete(0, END)
        self.txtFile1.insert(0, self.startPath)

    def OnButtonClick2(self):
        self.endPath = tkinter.filedialog.askdirectory(title='Please select data directory')
        self.txtFile2.delete(0, END)
        self.txtFile2.insert(0, self.endPath)

    def askQuit(self):
        if messagebox.askokcancel("Exit program", "Do you want to exit?"):
            #this closes app
            self.master.destroy()
            os._exit(0)
        
    def moveFiles(self):
        # Path to the file/directory
        path = self.startPath + "/"
        destination = self.endPath
        files = os.listdir(path)

        HourDateTime = datetime.datetime.now() - datetime.timedelta(hours = 1)
        ft = HourDateTime.strftime("%a %b  %#d %H:%M:%S %Y")

        for i in files:

            #get modification time and format
            ti_m = os.path.getmtime(path + i)
            m_ti = datetime.datetime.fromtimestamp(ti_m)

            #if modified within 24 hours, move files
            if m_ti < HourDateTime:
                shutil.move(path+i, destination)
                
if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
