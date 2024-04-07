import time
import threading
def printnum():
    for i in range(0,1000):
        print(i)
        time.sleep(1) # 50 s

def printalph():
    ls = ["a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d"]
    for i in ls:
        print(i)
        time.sleep(1)  # 50 s
thread1 = threading.Thread(target=printnum)
thread2 = threading.Thread(target=printalph)
thread3 = threading.Thread(target=printnum)
thread4 = threading.Thread(target=printalph)
thread5 = threading.Thread(target=printnum)
thread6 = threading.Thread(target=printalph)
thread7 = threading.Thread(target=printnum)
thread8 = threading.Thread(target=printalph)
thread9 = threading.Thread(target=printnum)
thread10 = threading.Thread(target=printalph)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread7.start()
thread6.start()
thread9.start()
thread1.join()
thread2.join()
