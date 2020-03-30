#!/usr/bin/env python3
import requests
import sys
import random

api = 'https://postman-echo.com/delay/'

def run():
    """ Program main entry """
    # Get random num from 1-5
    random_num = random.randint(0,5) 
    url = api+'{}'.format(random_num)

    # Start requests sessions
    with requests.Session() as session:
        try:
            with session.get(url) as response:
                print(response.status_code)
                # If status code is 200, exit with 0
                if response.status_code == 200:
                    sys.exit(0)
                else:
                    # Else, exist with 1
                    sys.exit(1)
        except(requests.exceptions.ConnectionError):
            # If there's connection exception, exit with 2
            sys.exit(2)

if __name__ == '__main__':
    # If running from the main script, strat run it
    run()
                
            

        
        