
class car:
    def __init__(self,make,color,year):
        self.make=make
        self.color=color
        self.year=year
    

    def forward(self):
        print("The car is accelerating.")

    def back(self):
        print("The car is moving backwards.")

    def left(self):
        print("The car is turning left at the next turn.")

    def right(self):
        print("The car is turning right at the next turn.")

    def park(self):
        print("The car is going to park at the next availabele place.")
   
    def stop(self):
        print("The car is stopping.")

    
    def move(self):

        choice=input(" To move forward type: forward \n To move backwards type: back \n To turn left type: left \n To turn right type: right \n To park the car type: park \n To stop the car type: stop \n \n What of the following options would you like the car to do?   ")
    
        if choice=="forward":
            self.forward()

        elif choice=="back":
            self.back()

        elif choice=="left":
            self.left()

        elif choice=="right":
            self.right()
        
        elif choice=="park":
            self.park()

        elif choice=="stop":
            self.stop()
        
        else:
            print("Wrong input. Please give the correct input: \n")


class suv(car):
    def __init__(self, make, color, year, model, engine):
        car.__init__(self,make,color,year)
        self.model=model
        self.engine=engine

    def show(self):
        print("Car make:" + self.make)
        print("Car color: " + self.color)
        print("Car year: " + self.year)
        print("Car model: " + self.model) 
        print("Car engine: " + self.engine) 





suv1=suv("Ferrari","Red","2018","SUV","V8")

suv1.show()

x=0
while x==0:
    suv1.move()