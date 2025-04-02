import asyncio
import time
import re


async def one():
    print('Start 1')
    await asyncio.sleep(2)
    print('End 1')

async def two():
    print('Start 2')
    await asyncio.sleep(5)
    print('End 2')

async def three():
    print('Start 3')
    await asyncio.sleep(10)
    print('End 3')

async def four():
    print('Start 3')
    await asyncio.sleep(20)
    print('End 3')

async def main():
    await asyncio.gather(one(), two(), three(), four())

def check_phone_number():
    num = input()
    res = re.search(r'\+?([7, 8])\s?\(?(9\d{2})\s?\)?-?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})', num)
    if res:
        num = res.group(1) + res.group(2) + res.group(3) + res.group(4) + res.group(5)
        print(num)

if __name__ == '__main__':
    check_phone_number()
    # start = time.time()
    # asyncio.run(main())
    # print(time.time() - start)