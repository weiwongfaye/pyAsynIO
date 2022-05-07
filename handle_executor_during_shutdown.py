# Waiting for the Executor During Shutdown

# asyncio.run() will call run_until_complete underneath, however, run_until_complete will only check the tasks, not the future
# for excutor with thread, we need to change future to task as workaround
# the other way is to use a try...catch... to wait future in coroutine




import time
import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor

async def make_coro(future):  
    try:
        return await future
    except asyncio.CancelledError:
        return await future

async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    asyncio.create_task(make_coro(future))  
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')

def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread!")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Bye!')
