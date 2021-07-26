# Python/Django Projects
*Developed for educational purposes*
## Overview
These are Python and Django Projects/Applications. This repository covers python fundamentals, a few projects, and an MVT application. Explore the code below:

### Basics
- [Abstraction](#abstraction)
- [Class Enheritance](#class-enheritance)
- [Encapsulation](#encapsulation)
- [File Functions](#file-functions)
- [Polymorphism](#polymorphism)
- [Timezones](#timezones)

### Python Projects
-  [Mean Game](#mean-game)
-  [Student Tracker](#student-tracker)
-  [Phonebook](#phonebook)

### Django Framework Applications
- [Checkbook](#checkbook)


### Abstraction
```python
#import abc mod
from abc import ABC, abstractmethod

#parent class
class payment(ABC):
def saleTotal(self, total):
print(f"Item Cost: {total}")
#abstract method

@abstractmethod

def calcTotal (self, total):
pass

#calculate and print
class taxCalc(payment):
def calcTotal (self, total):
tax = (total * .055) #clac tax
salePrice = round(total + tax, 2) #round total to hundreths place
print(f"Tax: {tax}")
print(f'Your total is {salePrice} today. ')

#set var values
obj = taxCalc()
obj.saleTotal(5.00)
obj.calcTotal(5.00)
```
### Class Enheritance
```python
#create class
class User:
fname = 'Daniel'
lname = ''
email = 'test@email.com'
password = 'helloWorld'

#def login function
def login(self):

#user input
userEmail = input("Enter your email >>> ")
userPassword = input('Enter your password >>> ')

#check for eqality
if (userEmail == self.email and userPassword == self.password):
print(f'Welcome Back, {self.fname}!')
else:
print('GET OUT ME SWAMP')
class Student:
studentID = 000000
overallGPA = 3.14
class Staff:
staffID = ''
courseNum = 3
new_user = User()
new_user.login()
```
### Encapsulation
```python
#create class
class Protected:
def __init__(self):
self.__userName = 'marioCartHero' #define private var
self._age = 25 #define public var
def getPrivate(self):
print(self.__userName)
def setPrivate(self):
self.__userName = private

#return private and protected values
obj = Protected()
obj.getPrivate()
print(obj._age)
```
### File Functions
```python
def moveFiles(self):

# Path to the file/directory
path = self.startPath + "/"
destination = self.endPath
files = os.listdir(path)
HourDateTime = datetime.datetime.now() - datetime.timedelta(hours = 1)
ft = HourDateTime.strftime("%a %b %#d %H:%M:%S %Y")

for i in files:
#get modification time and format
ti_m = os.path.getmtime(path + i)
m_ti = datetime.datetime.fromtimestamp(ti_m)

#if modified within 24 hours, move files
if m_ti < HourDateTime:
shutil.move(path+i, destination)
```
### Polymorphism
```python
#parent class
class User:
name = "Tom"
email = "test@email.com"
password = "helloworld"
accessLevel = 1

#login fuction
def getLoginInfo(self):
print("Login Below\n-------------")
entry_email = input("Enter Email: \n>>> ")
entry_pass = input("Enter Password: \n>>> ")

#check equality
if(entry_email == self.email and entry_pass == self.password and self.accessLevel == 1):
print(f"Welcome back, {self.name}!")

#check access level
elif (self.accessLevel != 1):
print("You do not have clearance to view this information. Contact Admin.")

#print if notmatch
else:
print("The password or email entered are incorrect.")

#child class
class Manager(User):
name = "Jake"
pinNum = '1111'
accessLevel = 2
def getLoginInfo(self):
print("Login Below\n-------------")
entry_email = input("Enter Email: \n>>> ")
entry_pin = input("Enter Pin: \n>>> ")
if(entry_email == self.email and entry_pin == self.pinNum and self.accessLevel == 2):
print(f"Welcome back, {self.name}!")
elif (self.accessLevel != 2):
print("You do not have clearance to view this information. Contact Admin.")
else:
print("The password or email entered are incorrect.")

#child class
class Admin(User):
name = "Daniel"
pinNum = '0000'
accessLevel = 0
def getLoginInfo(self):
print("Login Below\n-------------")
entry_email = input("Enter Email: \n>>> ")
entry_pin = input("Enter Pin: \n>>> ")
if(entry_email == self.email and entry_pin == self.pinNum and self.accessLevel == 0):
print(f"Welcome back, {self.name}!")
elif (self.accessLevel != 0):
print("You do not have clearance to view this information. Contact Admin.")
else:
print("The password or email entered are incorrect.")


if __name__ == '__main__':
u = User()
u.getLoginInfo()
m = Manager()
m.getLoginInfo()
a = Admin()
a.getLoginInfo()
```
### Timezones
```python
from datetime import datetime
import pytz

##NEW YORK Current Time
tzNYC = pytz.timezone('America/New_York')
timeNYC = datetime.now(tzNYC)

#format NYC time
nHour = timeNYC.strftime("%H")
nMin = timeNYC.strftime("%M")
nPeriod = timeNYC.strftime("%p")

##PORTLAND Current Time
tzPORT = pytz.timezone('Etc/GMT+7')
timePORT = datetime.now(tzPORT)

#format NYC time
pHour = timePORT.strftime("%H")
pMin = timePORT.strftime("%M")
pPeriod = timePORT.strftime("%p")

##LONDON Current Time
tzLOND = pytz.timezone('Europe/London')
timeLOND = datetime.now(tzLOND)

#format NYC time
lHour = timeLOND.strftime("%H")
lMin = timeLOND.strftime("%M")
lPeriod = timeLOND.strftime("%p")
if int(pHour) > 9 and int(pHour) < 17:
print("The time is {} : {} {}. Our Portland location is OPEN.".format(pHour, pMin, pPeriod))

else:
print("Our Portland location is currently CLOSED.")
if int(lHour) > 9 and int(lHour) < 17:
print("The time is {} : {} {}. Our London location is OPEN.".format(lHour, lMin, lPeriod))
else:
print("Our London location is currently CLOSED.")
if int(nHour) > 9 and int(nHour) < 17:
print("The time is {} : {} {}. Our New York location is OPEN.".format(nHour, nMin, nPeriod))
else:
print("Our New York location is currently CLOSED.")
```
### Mean Game
```python
def start(nice=0, mean=0, name=""):
#get users name
name = describe_game(name)
nice,mean,name = nice_mean (nice,mean,name)
```
```python
def win(nice,mean,name):
print(f"\nNice job {name}, you WIN! \nEveryone loves you and you've \nmade lots of friends along the way!")
again(nice,mean,name)
```
```python
def lose(nice,mean,name):
print(f"\nAhhh, game over {name}, you LOSE! \nYou are destined to be alone forever. That's called karma, {name}. Karma...")
again(nice,mean,name)
```
### Student Tracker
```python
# main
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
```

### Phonebook
```python
# main
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
```
### Checkbook
```python
# sample model
from django.db import models

class Account(models.Model):
first_name = models.CharField(max_length=50)
last_name = models.CharField(max_length=50)
initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

Accounts = models.Manager()

def __srt__(self):
return self.first_name + ' ' + self.last_name

TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

class Transaction(models.Model):
date = models.DateField()
type = models.CharField(max_length=10, choices=TransactionTypes)
amount = models.DecimalField(max_digits=15, decimal_places=2)
description = models.CharField(max_length=100)
account = models.ForeignKey(Account, on_delete=models.CASCADE)

Transactions = models.Manager()
```
```python
# sample view
def balance(request, pk):
account = get_object_or_404(Account, pk = pk)
transactions = Transaction.Transactions.filter(account=pk)
current_total = account.initial_deposit
table_contents = { }
for t in transactions:
if t.type == 'Deposit':
current_total += t.amount
table_contents.update({t: current_total})
else:
current_total -= t.amount
table_contents.update({t: current_total})
content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
return render(request, 'checkbook/BalanceSheet.html', content)
```
