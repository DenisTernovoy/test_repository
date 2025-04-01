import asyncio
import time

async def one():
    print('Start 1')
    await asyncio.sleep(5)
    print('End 1')

async def two():
    print('Start 2')
    await asyncio.sleep(10)
    print('End 2')

async def three():
    print('Start 3')
    await asyncio.sleep(15)
    print('End 3')

async def main():
    await asyncio.gather(one(), two(), three())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)