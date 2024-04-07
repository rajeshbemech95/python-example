# # f= open("test.txt","a")
# # f.write("\nGood\n")
# # f.write("\nmorning")
# # f.close()

# with open("test.txt","r") as f :
#     print(f.readline)



# f = open("test.txt","r")
# for i in f:
#     print(i)

# KeyError 
# NameError 
# ZeroDivisionError 
# ImportError 
# TypeError 
# SyntaxError 
# InterruptedError
# IndentationError



try:
    
    y = 10
    z = x + y + "dsdhj"
    print(z)

except TypeError:
    print("error is TypeError")

except NameError:
    print("error is name error")

else:
