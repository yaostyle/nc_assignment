#!/usr/bin/env python3
import requests
import sys
import random

def run():
    random_num = random.randint(0,5)
    url = 'https://postman-echo.com/delay/{}'.format(random_num)
    with requests.Session() as session:
        try:
            with session.get(url) as response:
                print(response.status_code)
                if response.status_code == 200:
                    sys.exit(0)
                else:
                    sys.exit(1)
        except(requests.exceptions.ConnectionError):
            sys.exit(2)

if __name__ == '__main__':
    run()
                
            

        
        