#Q.create a thread and sleep it and print a msg after sleep.
import threading
from threading import Thread
import time
def display() :
    time.sleep(5)
    print("Hello World!")
t=Thread(target=display)
t.start()
print("main thread executing :",threading.current_thread())
#Q.2.Make a Thread and print number 1-10 and wait 1 sec between.
import threading
from threading import Thread
import time
def counting():
    for i in range (1,11):
        print(i)
        time.sleep(1)
t=Thread(target=counting)
t.start()
#Q.3.Make a list have 5 elements and print every element after 2 sec.
import threading
from threading import Thread
import time
l=[2,4,6,8,10]
def list():
    i=2
    for x in l:
        if i%2==0:
            time.sleep(i)
            print(threading.current_thread().getName(),":",x)
            i=i+2
t=Thread(target=list)
t.setName("Number")
t.start()
#Q.4.Call factorial function using thread.
import threading
from threading import Thread
import time
def fact():
    num=int(input("enter a number"))
    fact=1
    while num>=1:
        fact=fact*num
        num=num-1
    print(fact)
t=Thread(target=fact)
t.start()

    
    

