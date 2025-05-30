import os
import threading
import time
import asyncio
import aiofiles

def writetxt(filename:str,txtinput:str):
    with open(filename,'w') as fileObj:
        for i in txtinput:
            fileObj.write(i)
            time.sleep(1)

def readtxt(filename:str):
    with open(filename,'r') as fileObj:
        str = fileObj.read()
        print('读取的内容是：',str)
        return str

async def async_write(filename: str, content: str):
    async with aiofiles.open(filename, mode='w') as f:
        for char in content:
            await f.write(char)
            await asyncio.sleep(0.5)  # 模拟耗时操作
        print(f"异步写入完成: {filename}")

async def async_read(filename: str):
    async with aiofiles.open(filename, mode='r') as f:
        content = await f.read()
        print(f"异步读取内容: {content}")
        return content

async def main_async_operations():
    base_directory = os.path.dirname(os.path.dirname(__file__))
    filename = os.path.join(base_directory, 'document','子文件夹','async_test.txt')

    # 运行异步写入和读取
    await async_write(filename, "这是异步写入的测试内容")
    await async_read(filename)

# 原有线程操作
base_directory = os.path.dirname(os.path.dirname(__file__))
filename=os.path.join(base_directory, 'document','子文件夹','testfile.txt')
t1=threading.Thread(target=writetxt,args=(filename,'测试'))
t2=threading.Thread(target=readtxt,args=(filename,))
t1.start()
t1.join()
t2.start()
t2.join()

# 运行异步操作
asyncio.run(main_async_operations())
print(__name__)
# lock=asyncio.Lock()

