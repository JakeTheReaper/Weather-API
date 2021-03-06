#!/usr/bin/env python3

#Student Name: Jake Duran Zerafa
#Student No: s3679109

import datetime
import requests
import json
import sys
from subprocess import run, PIPE
from append import fileSave
import time
import re

#Function to open JSON File.
def openFile(filename):
    fh = open(filename, 'r')
    datastore = json.load(fh)
    fh.close()
    return datastore
  
try:
    datastore = openFile(sys.argv[1])
except:
    datastore = openFile("ifttt.json")

#Create Services class.
class Services():
    
    def timeofday():
        #Get the time of day, format and return the output. 
        now = datetime.datetime.now()
        datastore['services']['time of day']['parameters'] = now.strftime('%d/%m/%Y %H:%M:%S')
        date = datastore['services']['time of day']['parameters']
        return date
    
    def geolocation():
        #Try open program to get location metadata
        #If file can't be opened, print error and exit process.
        #Otherwise return output
        try:
            command = datastore['services']['geolocation']['program']
            p = run(command, stdout=PIPE, input='', encoding='utf-8')
        except:
            print("Error: Cannot open file")
            sys.exit(1)
        else:
            return p.stdout

    def echo():
        #Echo current flow name.
        echo = datastore['services']['echo']['parameters']
        return echo

    def morning():
        #Check to see if service is run in the morning.
        #Get current time and return True or False if it is within the specified parameters.
        now = datetime.datetime.now()
        datastore['services']['morning']['parameters'] = now.strftime('%H:%M:%S')
        time = datastore['services']['morning']['parameters']
        if(time >= "00:00:00" and time < "12:00:00"):
            return True
        else:
            return False         
    
    def afternoon():
        #Check to see if service is run in the afternoon.
        #Get current time and return True or False if it is within the specified parameters.
        now = datetime.datetime.now()
        datastore['services']['morning']['parameters'] = now.strftime('%H:%M:%S')
        time = datastore['services']['morning']['parameters']
        if(time >= "12:00:00" and time < "18:00:00"):
            return True
        else:
            return False

    def evening():
        #Check to see if service is run in the evening.
        #Get current time and return True or False if it is within the specified parameters.
        now = datetime.datetime.now()
        datastore['services']['morning']['parameters'] = now.strftime('%H:%M:%S')
        time = datastore['services']['morning']['parameters']
        if(time >= "18:00:00" and time < "00:00:00"):
            return True
        else:
            return False

    def sunriseSunset():
        #Try open program to get sunrise metadata
        #If file can't be opened, print error and exit process.
        try:
            command = "./sunriseSunset.py"
            run(command, stdout=PIPE, input='', encoding='utf-8')
        except:
            print("Error: Cannot open file")
            sys.exit(1)

    def openSunriseSunset(filename):
        fh = open(filename, 'r')
        results = json.load(fh)
        fh.close()
        return results

    def sunrise():
        try:
            results = Services.openSunriseSunset("sunriseSunset.json")
        except:
            sys.exit(1)
        #Assign sunrise result and return output.
        sunrise = results['results']['sunrise']   
        return sunrise
        
    def sunset():
        try:
            results = Services.openSunriseSunset("sunriseSunset.json")
        except:
            sys.exit(1)
        #Assign sunset result and return output.
        sunset = results['results']['sunset']   
        return sunset

#Create Flows class.
class Flows():
    def appendTimeOfDay():
        #Check which flow is running.
        #Substitute $$ Special symbols with current flow
        #Write to file 
        for flow in datastore['flows']['Append time of day']:
            if flow == 'sunrise':
                pEcho = re.sub(r'\$\$', flow, Services.echo())
                print(pEcho)
                fileSave("times.txt", "Sunrise: " + str(Services.sunrise()) + ' UTC\n')
                time.sleep(1)
            elif flow == 'sunset':
                pEcho = re.sub(r'\$\$', flow, Services.echo())
                print(pEcho)
                fileSave("times.txt", "Sunset: " + str(Services.sunset()) + ' UTC\n')
                time.sleep(1)
            elif flow == 'time of day':
                pEcho = re.sub(r'\$\$', flow, Services.echo())
                print(pEcho)
                fileSave("times.txt", str(Services.timeofday())+'\n')
                time.sleep(1)
            elif flow == 'geolocation':
                pEcho = re.sub(r'\$\$', flow, Services.echo())
                print(pEcho)
                fileSave("times.txt", str(Services.geolocation()))
                time.sleep(1)
            elif flow == 'append to file':
                pEcho = re.sub(r'\$\$', flow, Services.echo())
                print(pEcho)
                time.sleep(1)
            else:
                print(flow + ": Is Not a Valid Service - SKIPPING...")
                time.sleep(1)
                pass

        print("Data written successfully")

def main():
    Services.sunriseSunset()
    count = 0
    #Run service every minute.
    #For 2 mins in this example
    while (count < 2):
        time.sleep(60 - time.time() % 60)
        print(Services.timeofday())
        print("Sunrise: " + Services.sunrise() + " UTC")
        print("Sunset: " + Services.sunset() + " UTC")
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
except:
    sys.exit(1)

sys.exit(0)
