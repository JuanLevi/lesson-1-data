
class student:
    def __init__(self,name,number,yclass):
        self.name=name
        self.number=number
        self.yclass=yclass
    

class studentInfo(student):
    def __init__(self,name,number,yclass,subject,teacher):
        student.__init__(self,name,number,yclass)
        self.subject=subject
        self.teacher=teacher

    def show(self):
        print("Student Name:" + self.name)
        print("Student Number:" + self.number)
        print("Student Class:" + self.yclass)
        print("Student Subject:" + self.subject)
        print("Student Teacher:" + self.teacher)

def input():
    input1=input('Would you like to add another student? ')
    if input1 =='Yes':
        addStudent()
            

    
def addStudent():
    nameIp=input('What is the students name? ')
    numberIp=input('What is the students number? ')
    yclassIp=input('What is the students class? ')
    subjectIp=input('What is the students subject? ')
    teacherIp=input('What is the students teacher? ')
    x=studentInfo(nameIp,numberIp,yclassIp,subjectIp,teacherIp)
    x.show()



student1=studentInfo("Adam",'2794','11D','Ciencies','Mr. Steven')

student1.show()

addStudent()

