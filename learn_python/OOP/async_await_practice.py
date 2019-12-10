from time import time ,sleep
def demo1():
    def washing1():
        sleep(3)
        print('washing1 finished')
    def washing2():
        sleep(2)
        print('washing2 finished')
    def washing3():
        sleep(5)
        print('washing3 finished')
    washing1()
    washing2()
    washing3()

def demo2():
    async def washing1():
        sleep(3)
        print('washing1 finished')
    async def washing2():
        sleep(2)
        print('washing2 finished')
    async def washing3():
        sleep(5)
        print('washing3 finished')
    washing1()
    washing2()
    washing3()
def demo3():
    async def washing1():
        await sleep(3)
        print('washing1 finished')
    async def washing2():
        await sleep(2)
        print('washing2 finished')
    async def washing3():
        await sleep(5)
        print('washing3 finished')
    washing1()
    washing2()
    washing3() 

def demo4():
    import asyncio
    async def washing1():
        await asyncio.sleep(3)
        print('washing1 finished')
    async def washing2():
        await asyncio.sleep(2)
        print('washing2 finished')
    async def washing3():
        await asyncio.sleep(5)
        print('washing3 finished')

    loop=asyncio.get_event_loop()
    tasks=[
        washing1(),
        washing2(),
        washing3(),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

async demo5():
    

start=time()
demo4()
end=time()
print(end-start)