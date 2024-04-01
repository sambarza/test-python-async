# example of using python asyncio gather
import asyncio

global_counter = 0


async def run_async():
    # increment global counter
    global global_counter
    global_counter += 1

    local_counter = global_counter

    print(f"start {local_counter}")
    # let the event loop to do other tasks
    await asyncio.sleep(0)
    print(f"end {local_counter}")


async def main():
    await asyncio.gather(run_async(), run_async())


asyncio.run(main())
