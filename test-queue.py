import asyncio


async def hello(name: str):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Bye {name}")
    return "Finished " + name


async def queue_processor():
    while True:
        try:
            name = await my_queue.get()
        except asyncio.CancelledError:
            print("Queue processor cancelled")
            return

        newname = await hello(name)
        print(newname)
        await asyncio.sleep(0.125)


async def processor_stopper(processor_task):
    await asyncio.sleep(15)
    processor_task.cancel()


async def main():
    processor_task = asyncio.create_task(queue_processor())
    asyncio.create_task(processor_stopper(processor_task))
    print("Main started")
    for name in ["1", "2", "3", "4", "5"]:
        my_queue.put_nowait(name)
    await processor_task
    print("Main ended")


my_queue = asyncio.Queue()
asyncio.run(main())
