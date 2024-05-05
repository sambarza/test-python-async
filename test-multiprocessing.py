import multiprocessing
import time
import asyncio
import random
import ctypes

class Counter():

    def __init__(self) -> None:
        print("init")
        self.launched_operations_count = 0

    def increment(self):
        print("here", self.launched_operations_count)
        self.launched_operations_count += 1

class StoreSimulator(multiprocessing.Process):

    def __init__(self, store_id, counter, wallets):

        super().__init__()

        self.store_id = store_id
        self.wallets = wallets
        self.launched_operations_count = 0
        self.counter = counter

    async def executeOperation(self):

        self.launched_operations_count += 1

        with self.counter.get_lock():
            self.counter.value += 1

        local_counter = self.launched_operations_count

        # print(f"start {self.store_id} {local_counter}")

        # let the event loop to do other tasks
        await asyncio.sleep(0)

        print(f"end {self.store_id} {local_counter}")

    async def run_async(self):
        coroutines = []

        print(f"Prepare coroutines {self.store_id}")
        for i in range(40000):
            coroutines.append(self.executeOperation())

        print(f"Gather coroutines {self.store_id}")
        await asyncio.gather(*coroutines)

    def run(self):

        asyncio.run(self.run_async())


def main():

    counter = multiprocessing.Value(ctypes.c_long)

    storeSimulators = [StoreSimulator(i, counter, []) for i in range(2)]

    for storeSimulator in storeSimulators:
        storeSimulator.start()

    for storeSimulator in storeSimulators:
        storeSimulator.join()

    print("Launched operations:", counter.value)


if __name__ == "__main__":
    main()