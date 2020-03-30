#!/usr/bin/env python3
import os
import asyncio
import aiohttp
import json
import ssl
import subprocess as sp
  
loop = asyncio.get_event_loop()

async def main():  
    child = sp.Popen('./slave.py', stdout=sp.PIPE).communicate()[0]
    
    print(child)

# async def main():
#     client = aiohttp.ClientSession(loop=loop)
#     while True:    
#         await get_json(client, 'https://postman-echo.com/delay/1')

# async def get_json(client, url):
#     default_ssl = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
#     async with client.get(url,ssl=default_ssl) as response:
#         assert response.status == 200
#         print("200")
#         return await response.read()

if __name__ == '__main__':
    asyncio.ensure_future(main())
    loop.run_forever()

        
    