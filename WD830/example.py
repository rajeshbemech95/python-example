# this is a sample program for variable
print("Choose from below \n1.Add\n2.Sub")
choice = int(input("enter your choice"))
num1 = float(input("Enter No : "))
num2 = float(input("Enter No : "))
def add():
    return num1+num2
def sub():
    print(num1-num2)

if choice==1:
    print(add())
elif choice==2:
    sub()
    












