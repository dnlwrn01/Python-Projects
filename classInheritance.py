

class User:
    fname = 'Daniel'
    lname = ''
    email = 'test@email.com'
    password = 'helloWorld'

    def login(self):
        userEmail = input("Enter your email >>> ")
        userPassword = input('Enter your password >>> ')
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


    
