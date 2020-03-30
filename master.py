#!/usr/bin/env python3
import os
import asyncio
import signal
import sys
from subprocess import call
  
loop = asyncio.get_event_loop()

async def main(): 
    n = 0
    while n <= 5: 
        rc = call(['./slave.py'], shell=True)
        if rc == 0:
            n=n+1
        elif (rc == 2):
            rc = call(['./slave.py'], shell=True)
    exit(0)
        
def exit(int):
    try:
        loop.stop()
        signal.SIGINT
        sys.exit(int)
    except:
        pass
    
if __name__ == '__main__':
    asyncio.ensure_future(main())
    loop.run_forever()

        
    