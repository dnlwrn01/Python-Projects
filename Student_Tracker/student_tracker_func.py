
#import mods
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

#custom
import student_tracker_main
import student_tracker_gui

def center_window(self, w, h): #pass in tkinter frame (master) reference, and the w and h
    #get users screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calc x and y coords to paint app center on user display
    x = int ((screen_width/2) - (w/2))
    y = int ((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

#catch if user clicks on upper right 'x' to close window
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Do you want to exit?"):
        #this closes app
        self.master.destroy()
        os._exit(0)

#==================================================

def create_db(self):
    conn = sqlite3.connect('student_tracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student_tracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        #commit/save changes & close db conn
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com', 'Math 120')
    conn = sqlite3.connect('student_tracker.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_student_tracker (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?, ?, ?, ?, ?)""", (data))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
    count = cur.fetchone() [0]
    return cur,count

#Select items in listbox
def onSelect(self,event):
    #calling the event is self.lstList1
    varList = event.widget
    select = varList.curselection() [0]
    value = varList.get(select)
    conn = sqlite3.connect('student_tracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course FROM tbl_student_tracker WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        #this returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize the data to keep consistant in database
    var_fname = var_fname.strip() #remove whitespace from user entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() #ensure first letter is capitalized
    var_lname = var_lname.title()
    var_fullname = (f"{var_fname} {var_lname}") #combinne normalized names into fullname
    print(f"var_fullname: {var_fullname}")
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if not '@' or not "." in var_email: #check email format
        print("Incorrect Email Format. Please Try Again.")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): #ensure user entry for each field
        conn = sqlite3.connect('student_tracker.db')
        with conn:
            cursor = conn.cursor()
            #check if database for existance of the fullname, if so we will alert the user and disreguard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_student_tracker WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone() [0]
            chkName = count
            if chkName == 0: #if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_student_tracker (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?, ?, ?, ?, ?)""", (var_fname,var_lname,var_fullname,var_phone,var_email, var_course))
                self.lstList1.insert(END, var_fullname) #update listbox with the new fullname
                onClear(self) #call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) #call the function to clear all of the textboxes
            conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #list boxes selected value
    conn = sqlite3.connect('student_tracker.db')
    with conn:
        cur = conn.cursor()
        #check count to ensure that this is not the last record in
        #the database... cannot delete last record or error will occur
        cur.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
        count = cur.fetchone() [0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('student_tracker.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student_tracker WHERE col_fullname = '{}'""".format(var_select))
                    onDeleted(self) #call the function to clear all of the textboxes and selected index of listbox onRefresh(self) #update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)
    #onRefresh(self) #update the lsitbox of the changes
    try:
        index = self.lstList1.curselection() [0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)

def onRefresh(self):
    #populate the listbox, coinciding with the db
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student_tracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_student_tracker""")
        count = cursor.fetchone() [0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_student_tracker""")
            varList = cursor.fetchall() [i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i +1
    conn.close()

if __name__ == '__main__':
    pass














