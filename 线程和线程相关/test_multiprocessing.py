import queue
from multiprocessing import Process, Queue


def worker(num):
    """线程执行函数"""
    # 光标会自动定位到这里，提示可以添加更多功能
    print(f'Worker: {num} started')
    result = num * 2
    print(f'Worker: {num} finished')
    return result

if __name__ == '__main__':
    # 这里可以演示代码补全功能
    # 使用列表推导式简化进程创建
    jobs = [
        Process(target=worker, args=(i,))
        for i in range(5)
    ]
    for p in jobs:
        p.start()

    # 等待所有进程完成
    for p in jobs:
        p.join()

    print("所有进程执行完毕")

q1= Queue(3)
q1.put(1, block=False)
q1.put(2, block=False)
q1.put(3, block=False)

# q1.put(4, block=False)