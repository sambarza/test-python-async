import asyncio
import datetime


async def print_current_time():
    while True:
        print(datetime.datetime.now())
        await asyncio.sleep(0.5)

async def print_hello():
    while True:
        print(datetime.datetime.now(), "hello")
        await asyncio.sleep(1)

async def main():

    print("prima")
    task_first = asyncio.create_task(print_current_time)
    task_second = asyncio.create_task(print_hello)
    print("dopo")

    await asyncio.wait([task_first, task_second])


asyncio.run(main())
