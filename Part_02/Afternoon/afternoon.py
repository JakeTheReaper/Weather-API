#!/usr/bin/env python3

import datetime
import json
import sys

#Function to open JSON File.
def openFile(filename):
    fh = open(filename, 'r')
    datastore = json.load(fh)
    if('name' in datastore and 'program' in datastore and 'description' in datastore):
        fh.close()
        return datastore
    else:
        print("Error found in JSON config file")
        sys.exit(1)
try:
    datastore = openFile("./Afternoon/config.json")
except:
    sys.exit(1)

def afternoon(): 
    #Check to see if service is run in the afternoon.
    #Get current time and return True or False if it is within the specified parameters.
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    start = datastore['configuration']['starttime']
    end = datastore['configuration']['endtime']
    if(time >= start and time < end):
        return True 
    else:
        return False

def main():
    print(str(afternoon()))

main()