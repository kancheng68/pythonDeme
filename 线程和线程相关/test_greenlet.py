

from greenlet import greenlet
import gevent
from gevent import monkey
monkey.patch_all() #改变的是整个进程的标准库行为都会被修改，所有被引用的标准库的阻塞模式变成协程
import time

def task1():
    print("step 1")
    gr2.switch()  # 手动切换至task2
    print("step 3")
def task2():
    print("step 2")
    gr1.switch()  # 切换回task1
gr1 = greenlet(task1)
gr2 = greenlet(task2)
gr1.switch()  # 启动协程

def task_gevent1():
    print("gevent step 1")
    time.sleep(2)  # 让出CPU时间片
    print("gevent step 2")

def task_gevent2():
    print("gevent step 3")
    time.sleep(3)
    print("gevent step 4")

def task_gevent_single(txtinput:str):
    print(f"gevent with input1: '{txtinput}'")
    time.sleep(2)
    print(f"gevent with input2: '{txtinput}'")

g1 = gevent.spawn(task_gevent1)
g2 = gevent.spawn(task_gevent2)
g1.join()
g2.join()


if __name__=="__main__":
    gevent.joinall([
        gevent.spawn(task_gevent_single,'第一个协程'),
        gevent.spawn(task_gevent_single,'第二个协程')
    ])


    # def process_data(name, *scores, **metadata):
    #     if scores:
    #         avg_score = sum(scores) / len(scores)
    #         print(f"姓名: {name}")
    #         print(f"平均分: {avg_score:.2f}")
    #         print("元数据:", metadata)
    #     else:
    #         print(f"姓名: {name}")
    #         print("没有分数")
    #         print("元数据:", metadata)
    # 
    # process_data("张三", 85, 90, 78, class_="二班", teacher="李老师")