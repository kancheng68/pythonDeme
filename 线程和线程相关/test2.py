import time
from threading import Thread,Lock

a=0
b=1000000
lock=Lock()
def add():
    for i in range(b):
        global a
        with lock:
            a+=1
    print('第一次运行:',a)

def add2():
    for i in range(b):
        global a
        with lock:
            a += 1
    print('第二次运行:',a)

li=[]
def testapped():
    for i in range(5):
        li.append(i)
        time.sleep(0.2)
    print('写入后的Li的值是：',li)

def testread():
    print('读取到的Li的值是：',li)
# add()
# add2()

t1=Thread(target=testapped)
t2=Thread(target=testread)
t1.start()
t1.join()
t2.start()