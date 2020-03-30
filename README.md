# nc assignment

An assignement to create Master and Slave applications

What does it do?
 - The slave app sends a GET request to an api with a parameter random number from 1 to 5.

 - Slave app will exit with zero if api returned status code of 200.
 - For other status code, exit with 1.
 - The salve app should use exit code 2 in case of any network errors.
 - The Master app should asyncchronously run 5 slave apps and wait until all application are finished with zero exit code. If the slave app finished with a non-zero exit code, the Master app should restart the slave app.

## Environement
This app is runnning on Python 3.5+

## Dependencies
Install all dependencies via requirements.txt
    
    pip3 install -r requirements.txt


## Usage
Run the Master app by

    ./master.py

## Unit Tests
A few of simple unittests are included:

    master_test.py
    slave_test.py

## Concept of Tests
To observe network request status and logic result, the following scenarios are my methods to ensure the program logic.

 - Scenario #1: First run the master.py with default API setting. Observe the status code returned from slave.py which you should be getting five (5) times of "200" echo to the screen. Then the master app will be exited.

 - Scenario #2: Run the master.py with default API setting. Right after the first 200 status code apprears, change the API URL from slave.py to something else to observe a different status code returned. (e.g. add or remove a few words from the endpoint.) Observe the master app will now keep trying to re-run the slave app until it reached five (5) times of 200 status code (if you undo the API setting to default).

 - Scenario #3: Change the API setting from slave.py either use a none valid http protocols such as "htt://" or change a different endpoint. Run the master.py and obverse the app will now result in an infinity loop because our API will never reach to 200 status code.