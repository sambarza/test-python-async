import asyncio


async def hello(name: str):
    print(f"Started {name}")
    await asyncio.sleep(5)
    print(f"Finished {name}")


def sub_main():
    print("Sub main started")


async def print_time_1():
    current_time = 0
    while True:
        current_time += 1
        print("Print time_1 ", current_time)
        await asyncio.sleep(0.125)


async def print_time_2():
    current_time = 0
    while True:
        current_time += 1
        print("Print time_2 ", current_time)
        await asyncio.sleep(0.250)


async def main():
    print("Main started")
    asyncio.create_task(print_time_1())
    asyncio.create_task(print_time_2())
    await asyncio.create_task(hello("1"))
    sub_main()
    print("Main ended")


asyncio.run(main())
