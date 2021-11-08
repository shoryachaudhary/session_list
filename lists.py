#Student Data Management ProGram

class Student:
    
    def __init__(self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age
        
#function to create list of students     
    def create(self,name,rollno,age):
        ob = Student(name,rollno,age)
        ls.append(ob)
        
#function to display the list of students detail
    def display(self,ob):
        print("Name:",ob.name)
        print("Rollno",ob.rollno)
        print("Age",ob.age)
        print("\n")
        
#creating a empty list to add students data
ls = []

#creating a object for the student class
obj = Student('',0,0)
        
print("Operations used....\n")
print("1. Add the students details \n2. Display the student details \n3.Exit")

obj.create("Bob",1,10)
obj.create("Jack",2,9)

print("\n")
print("List of Students Details")
for i in range(ls.__len__()):
    obj.display(ls[i])


print("Data added successfully....")    
    


    
