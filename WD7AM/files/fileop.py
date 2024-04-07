
f = open("text11.txt","r")
# ls = ["monday","tuesday","wednesday"]
for i in range(0,10):
    print(i)
    i = str(i)
    f.write(i)
f.close


with open("text1.txt","w") as s:
    s.write("hello")