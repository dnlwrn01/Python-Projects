

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

    
