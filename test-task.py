import asyncio


async def print_time_each_second():
    print(f"print_time_each_second started")

    seconds = 0
    while True:
        print("Seconds:", seconds)
        await asyncio.sleep(1)
        seconds += 1


async def print_hello_world(number: int):
    print(f"Hello world from task {number}!")
    return number


async def say_after(delay, what):
    print(f"say_after started: {what} {delay}")
    await asyncio.sleep(delay)
    print(what)


def on_finished_task_callback(future):
    print(f"Finished task {future.result()}")


async def sub_main():
    print("Main2 started")
    task_time = asyncio.create_task(print_time_each_second())

    task1 = asyncio.create_task(say_after(5, "hello"))
    await task1
    task2 = asyncio.create_task(say_after(2, "world"))
    task3 = asyncio.create_task(say_after(20, "not printed"))
    task4 = await say_after(10, "await secco")

    asyncio.create_task(print_hello_world(1))
    task_cancelled = asyncio.create_task(print_hello_world(100))
    task_callback = asyncio.create_task(print_hello_world(2))
    asyncio.create_task(print_hello_world(3))
    asyncio.create_task(print_hello_world(4))
    asyncio.create_task(print_hello_world(5))

    print("1")
    print("2")
    task_cancelled.cancel()
    task1
    print("3")

    print(f"Main2 finished")
    task_callback.add_done_callback(on_finished_task_callback)

    return task1


async def main():
    print("Main started")
    long_task = await sub_main()
    print("Main ended")
    await long_task


asyncio.run(main())
