# Student data
# Complete the code with following:
# 1. Add if/elif/else statement and user will decide which operation to do
# 2. All the value must be entered by user instead of hardcode
class Student:
    def __init__(self,name,rollno,m1,m2):
        self.name = name
        self.rollno = rollno
        self.m1= m1
        self.m2= m2

    def accept(self,name,rollno,mark1,mark2):
        ob = Student(name,rollno,mark1,mark2)
        ls.append(ob)

    def display(self,ob):
        print("Name: ",ob.name)
        print("Rollno: ", ob.rollno)
        print("Mark 1: ",ob.m1)
        print("Mark 2 : ",ob.m2)

    # def search(self,rn):
    #     for i in range(ls.__len__()):
    #         if(ls[i].rollno == rn):
    #             return i 
    # def delete(self,rn):
    #     i = obj.search(rn)
    #     del ls[i]

ls = []

obj = Student("",0,0,0)
obj.accept("Student 1",1,90,95)
obj.accept("STudent 2",2,95,92)
obj.accept("Student 3",3,95,100)

for i in range(ls.__len__()):
    obj.display(ls[i])


# num = int(input("enter roll no to search"))
# s = obj.search(num)
# obj.display(ls[s])

# obj.delete(3)













