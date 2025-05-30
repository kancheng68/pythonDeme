from queue import Queue
import threading

def worker(q:Queue):
    while True:
        item = q.get()  # 这里会阻塞直到有数据
        print(f"处理: {item}")
        q.task_done()

# 创建容量为3的队列
q = Queue(3)
print("队列创建成功")  # 这行应该会执行

# 启动工作线程
threading.Thread(target=worker, daemon=True, args=(q,)).start()

# 测试打印
print("开始添加数据")
for i in range(5):
    q.put(i)  # 当队列满时会阻塞
    print(f"已添加: {i}")  # 这里可能被阻塞

print("等待队列完成")
q.join()
print("所有任务完成")
