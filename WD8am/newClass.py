# Database system 

# Collect
# Display
# Search 
# Delete

class Student():
   
    def __init__(self,name,rollno,m1,m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    def getting(self,name,rollno,m1,m2):
        db = Student(name,rollno,m1,m2)
        ls.append(db)
        
    def display(self,db):
        print("List of details is: \n")
        print("Name :",db.name)
        print("Roll no :",db.rollno)
        print("Mark 1: ",db.m1)
        print("Mark 2:",db.m2)
        print("\n")

    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
    # def searchName(self,m):
    #     for i in range(ls.__len__()):
    #         if(ls[i].m1 == m) or (ls[i].m2 == m):
    #             return i
            
    def delete(self,rn):
        i = stu.search(rn)
        del ls[i]


ls = []
# Add choice from user to select option 
stu = Student("",0,0,0)
# Collecting student data 
stu.getting("Name1",1,95,100)
stu.getting("Name2",2,97,99)
stu.getting("Name3",3,92,98)
stu.getting("Name4",4,92,98)
# Displaying data 
for i in range(ls.__len__()):
     stu.display(ls[i])
#  Search with rollno 
print("search result ")
res = stu.search(3)
stu.display(ls[res])
# Delete the data 
stu.delete(2)
print("display after seletion")
for i in range(ls.__len__()):
     stu.display(ls[i])


