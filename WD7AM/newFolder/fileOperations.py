# read "r"
# write "w"
# append "a"


# Append
f = open("test.txt","w")
f.write(" \nworld\n")
f.write("\nAwsome")
f.close()

# Write
with open("test_1.txt","w+") as f:
    f.write(" \nworld\n")
    f.close()

# Read
# f = open("test.txt","r")
# print(f.readline(1))

