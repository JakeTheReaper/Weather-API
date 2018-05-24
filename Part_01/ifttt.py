#!/usr/bin/env python3

import datetime
import requests
import json
import sys
from subprocess import run, PIPE
import time
import re

filename = "ifttt.json"

try:
    fh = open(filename, 'r')
    datastore = json.load(fh)
except IOError:
    print("Error: File not found")
    sys.exit(0)
else:
    print(filename + ": opened successfully")
    fh.close()

class Services():
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

    def morning():
        now = datetime.datetime.now()
        datastore['services']['morning']['parameters'] = now.strftime('%H:%M:%S')
        time = datastore['services']['morning']['parameters']
        if(time >= "00:00:00" and time < "11:59:59"):
            return True
        else:
            return False         
    
    def afternoon():
        now = datetime.datetime.now()
        datastore['services']['morning']['parameters'] = now.strftime('%H:%M:%S')
        time = datastore['services']['morning']['parameters']
        if(time >= "12:00:00" and time < "17:59:59"):
            return True
        else:
            return False

    def evening():
        now = datetime.datetime.now()
        datastore['services']['morning']['parameters'] = now.strftime('%H:%M:%S')
        time = datastore['services']['morning']['parameters']
        if(time >= "18:00:00" and time < "23:59:59"):
            return True
        else:
            return False

class Flows():
    def appendTimeOfDay():
        try:
            fh = "times.txt"
            file = open(fh, "a")
        except IOError:
            print("Error: File not found")
            sys.exit(1)
        else:
            for flow in datastore['flows']['Append time of day']:
                if flow == 'time of day':
                    pEcho = re.sub(r'\$\$', flow, Services.echo())
                    print(pEcho)
                    file.write(str(Services.timeofday())+'\n')
                    time.sleep(1)
                elif flow == 'geolocation':
                    pEcho = re.sub(r'\$\$', flow, Services.echo())
                    print(pEcho)
                    file.write(str(Services.geolocation()))
                    time.sleep(1)
                elif flow == 'append to file':
                    pEcho = re.sub(r'\$\$', flow, Services.echo())
                    print(pEcho)
                    time.sleep(1)
                else:
                    print(flow + ": Is Not a Valid Service - SKIPPING...")
                    time.sleep(1)
                    pass

            print("Data written to " + fh + " successfully")
            file.close()

def main():
    count = 0
    while (count < 2):
        time.sleep(60 - time.time() %60)
        print(Services.timeofday())
        Flows.appendTimeOfDay()
        count += 1
    sys.exit(0)

try:
    if(Services.morning()):
        print("Time of day is " + datastore['services']['morning']['program'])
        main()
    elif(Services.afternoon()):
        print("Time of day is " + datastore['services']['afternoon']['program'])
        main()
    elif(Services.evening()):
        print("Time of day is " + datastore['services']['evening']['program'])
        main()
    else:
        sys.exit(1)
except:
    sys.exit(1)

sys.exit(0)
