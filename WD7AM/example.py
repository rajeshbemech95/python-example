# Program for addition
# a = int(input("enter the first number:")) # first no
# b = int(input("enter the second  number:"))
# print("value of a is:",a,"value of b:",b)
# print(type(a))
# print(type(b))
# c = a/b
# print(c)

# Operators

# +-/*%
# <> <= >= !=
# and or not

# Data Structure

# l = ["hello","world"]
# tuple = ("hello","world")
# set = {"hello","world"}

# if elif else
# a = int(input("enter value of a:"))
# if a==10:
#     print("value of a is:",a)
# elif a<=10:
#     print("a is less than 10 and value is",a)

# else:
#     print("a is not 10")


print("welcome")
while True:
    choice = input("Enter your choice:1.Add 2.Sub 3.Multi 4.Dive:") # 1 or 2 or 3 or 4
    a  = int(input("enter first no:"))
    b = int(input("enter second no"))
    if choice=="1":
        print(a+b)
    elif choice=="2":
        print(a-b)
    elif choice=="3":
        print(a*b)
    elif choice=="4":
        if b!=0:
            print(a/b)   
        else:
            print("Cannot divide by zero")
            
    else:
        print("Sorry you entered wrong option")

    

    








