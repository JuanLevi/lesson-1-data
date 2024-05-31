# Object Oriented Programming
#Focus on real life entities to write code

#Object - Any real Life entity represented in code
#for example - student, cars, fruits

#Class - Blueprint of an object
#(apple, banana, mango ) (objects) - > Fruits (class)

class Fruit:
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste
    
    def changeName(self):
        self.name=input("What is the name of this fruit?")

    def changeColor(self):
        self.color=input("What is the color of this fruit?")   

    def changeTaste(self):
        self.taste=input("What is the taste of this fruit?") 

    def show(self):
        print("The fruit is:")
        print("Name: " + self.name)
        print("Color: " + self.color)
        print("Taste: " + self.taste)
    


apple=Fruit("Banana","Green","Sweet")

apple.show()

apple.changeColor()

apple.changeName()

apple.show()

