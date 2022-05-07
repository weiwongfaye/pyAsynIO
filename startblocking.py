import time
import asyncio
import time

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')

def blocking():  
    time.sleep(0.5)  
    print(f"{time.ctime()} Hello from a thread!")

loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, blocking)  # run blocking code in a thread
loop.run_until_complete(task) # will run both blocking and async task

pending = asyncio.all_tasks(loop=loop)   # only tasks will be included, futures will be ignored (that is the "blocking" task will be ignored )
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
