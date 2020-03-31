#!/usr/bin/env python3
import os
import asyncio
import signal
import sys
from subprocess import call
  
loop = asyncio.get_event_loop()

async def run(): 
    """ Program main entry """
    # Declar success number of counts (n)
    n = 0

    # Resursive loop until reach 5 success tries
    while n < 5: 
        rc = call(['./slave.py'], shell=True)
        # If exit code is 0, add to success counts
        if rc == 0:
            n=n+1
        # If exit code is 2, rerun the slave script
        elif (rc == 2):
            rc = call(['./slave.py'], shell=True)

    # Finally reached to 5 success counts, run exit function 
    exit_loop(0)
        
def exit_loop(int):
    """ Exit function """
    try:
        # Stop the loop, send SIGINT signal 
        # and try exit the program
        loop.stop()
        signal.SIGINT
        sys.exit(int)
    except:
        # No implement for exception handling yet
        pass
    
if __name__ == '__main__':
    # If running from the main script, start async loop
    asyncio.ensure_future(run())
    loop.run_forever()

        
    