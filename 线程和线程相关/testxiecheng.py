import asyncio
import time


async def astest_input(q):
    while True:
        print('写入队列值---')
        await q.put(time.time())
        await asyncio.sleep(5)
async def astest_output(q):
    while True:
        value = await q.get()
        print("读取队列值：",value)

async def main():
    q1=asyncio.Queue()
    await asyncio.gather(astest_input(q1), astest_output(q1))

asyncio.run(main())
