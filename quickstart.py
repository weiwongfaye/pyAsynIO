import asyncio
import time

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")

async def test():
    print(f"{time.ctime()} test start!")
    await asyncio.sleep(10.0)
    print(f"{time.ctime()} test finish!")

loop = asyncio.get_event_loop()  
task = loop.create_task(main())  
task2 = loop.create_task(test())
loop.run_until_complete(task)   # run until "task" done

# When the “main” part of the program unblocks, either due to a process signal being received or the loop being stopped by some code calling loop.stop(), the code after run_until_complete() will run. The standard idiom as shown here is to gather the still-pending tasks, cancel them, and then use loop.run_until_complete() again until those tasks are done. gather() is the method for doing the gathering. Note that asyncio.run() will do all of the cancelling, gathering, and waiting for pending tasks to finish up.
pending = asyncio.all_tasks(loop=loop) # at this point "task2" still running(pending)
for task in pending: 
    task.cancel()  # cancel "task2"
group = asyncio.gather(*pending, return_exceptions=True)  
loop.run_until_complete(group)   # make sure cancel done
loop.close()
