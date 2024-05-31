

class accountInfo:

    def __init__(self,user,password,dob):
            self.user=user
            self.password=password
            self.dob=dob

    def changeUser(self):
          self.user=input("What username would you like to input?")

    def showUser(self):
          print("This is your current username: "+ self.user)



    def changePassword(self):
          self.password=input("What password would you like to input?")

    def showPassword(self):
          print("This is your current password: "+ self.password)



    def changeDob(self):
          self.dob=input("What date of birth would you like to input?")

    def showDob(self):
          print("This is your current Date of birth: "+ self.dob)

    def show(self):
        print("Your account info:")
        print("Username: " + self.user)
        print("Password: " + self.password)
        print("Date of birth: " + self.dob)    


user1=accountInfo("Jhon","apple123","10/06/1992")

user1.showDob()

user1.changePassword()

user1.changeUser()

user1.show()

