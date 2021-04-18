
#import modules
import os
import sqlite3

#variable for db connection
conn = sqlite3.connect('temp.db')

#create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_FileName(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_File TEXT \
        )")
    conn.commit()
conn.close()

#re-connect to db
conn = sqlite3.connect('temp.db')

#var file list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#iterate through list
for x in fileList:

    #find txt files
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()

            #insert x value into table
            cur.execute("INSERT INTO tbl_FileName (col_File) VALUES (?)", (x,))
            print(x)

#close connection
conn.close()













    

