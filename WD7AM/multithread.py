import threading
import time


def printnum():
    i = 0
    while i<1000:
        i = i+1
        print(i)
        time.sleep(1)

def printalpha():
    ls = ["daweed","wed","SDASDD","ZSDAS","fqrewfq","eweq","fqewwf","wefwrf"]
    for i in ls:
        print(i)
        time.sleep(2)

# printnum()
# printalpha()
t1= threading.Thread(target=printnum()) #30sec
t2 = threading.Thread(target=printalpha) #30sec
t1.start()
t2.start()
t1.join()
t2.join()
# import threading
# import time
# def print_num():
#     for i in range(1,10):
#         print(i)
#         time.sleep(1)
# def print_alp():
#     for letter in "abcde":
#         print(letter)
#         time.sleep(1)

# thread1 = threading.Thread(target=print_num)
# thread2 = threading.Thread(target=print_alp)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

















