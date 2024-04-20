# example of using python asyncio gather
import asyncio
import random

global_counter = 0


async def run_async():
    # increment global counter
    global global_counter
    global_counter += 1

    local_counter = global_counter

    random_sleep_time = random.randint(0, 5)

    print(f"start {local_counter} {random_sleep_time}")

    # let the event loop to do other tasks
    await asyncio.sleep(random_sleep_time)

    print(f"end {local_counter}")


async def main():

    coroutines = []

    print("Prepare coroutines")
    for i in range(100):
        coroutines.append(run_async())

    print("Gather coroutines")
    await asyncio.gather(*coroutines)


asyncio.run(main())
