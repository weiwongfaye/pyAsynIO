# communication between coroutine and threads
import asyncio
import random
import time

import janus

async def main():
    loop = asyncio.get_running_loop()
    queue = janus.Queue()  
    future = loop.run_in_executor(None, data_source, queue)
    while (data := await queue.async_q.get()) is not None:  
        print(f'Got {data} off queue')  
    print('Done.')

def data_source(queue):
    for i in range(10):
        r = random.randint(0, 4)
        time.sleep(r)  
        queue.sync_q.put(r) 
    queue.sync_q.put(None)

asyncio.run(main())
