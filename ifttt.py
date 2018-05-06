#!/usr/bin/env python3

import datetime
import requests
import json
import sys
from subprocess import run, PIPE
import time

filename = "./ifttt.json"

try:
    fh = open(filename, 'r')
    datastore = json.load(fh)
except IOError:
    print("Error: File not found")
    sys.exit(0)
else:
    print("File opened successfully")
    fh.close()

def timeofday():
    now = datetime.datetime.now()
    datastore['services']['time of day']['parameters'] = now.strftime('%d/%m/%Y %H:%M:%S')
    date = datastore['services']['time of day']['parameters']
    return date

def geolocation():
    command = datastore['services']['geolocation']['program']
    p = run(command, stdout=PIPE, input='', encoding='utf-8')
    return p.stdout

def echo():
    echo = datastore['services']['echo']['parameters']
    return echo

def appendTimeOfDay():
    try:
        file = open("times.txt", "w")
    except IOError:
        print("Error: File not found")
        sys.exit(0)
    else:
        for flow in datastore['flows']['Append time of day']:
            if flow == 'time of day':
                print(echo() + flow)
                file.write(str(timeofday())+'\n')
                time.sleep(1)
            elif flow == 'geolocation':
                print(echo() + flow)
                file.write(str(geolocation()))
                time.sleep(1)
            elif flow == 'append to file':
                print(echo() + flow)
                time.sleep(1)
            else:
                print("Not a Valid Service")

        print("File written successfully")
        file.close()

def main():
    appendTimeOfDay()
    sys.exit(0)

main()
