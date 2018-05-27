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
    
    def timeofday(filename):
        fh = open(filename, 'r')
        datastore = json.load(fh)
        if('name' in datastore and 'program' in datastore and 'description' in datastore):
            fh.close()
            return datastore
        else:
            print("Error found in JSON config file")
            sys.exit(1)
    
    def getTimeofday():
        #Try open program to get location metadata
        #If file can't be opened, print error and exit process.
        #Otherwise return output
        try:
            datastore = Services.timeofday("./Time of day/config.json")
            command = "./Time of day" + datastore['program']
            p = run(command, stdout=PIPE, input='', encoding='utf-8')
        except:
            print("Error: Cannot open file")
            sys.exit(1)
        else:
            return p.stdout

    def geolocation(filename):
        fh = open(filename, 'r')
        datastore = json.load(fh)
        if('name' in datastore and 'program' in datastore and 'description' in datastore):
            fh.close()
            return datastore
        else:
            print("Error found in JSON config file")
            sys.exit(1)
        
    def getGeolocation():
        #Try open program to get location metadata
        #If file can't be opened, print error and exit process.
        #Otherwise return output
        try:
            datastore = Services.geolocation("./Geolocation/config.json")
            command = "./Geolocation" + datastore['program']
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

    def morning(filename):
        #Function to open JSON File.
        fh = open(filename, 'r')
        datastore = json.load(fh)
        if('name' in datastore and 'program' in datastore and 'description' in datastore):
            fh.close()
            return datastore
        else:
            print("Error found in JSON config file")
            sys.exit(1)
        
    def getMorning():
        #Try open program to get location metadata
        #If file can't be opened, print error and exit process.
        #Otherwise return output
        try:
            datastore = Services.morning("./Morning/config.json")
            command = "./Morning" + datastore['program']
            p = run(command, stdout=PIPE, input='', encoding='utf-8')
        except:
            print("Error: Cannot open file")
            sys.exit(1)
        else:
            return p.stdout
    
    def afternoon(filename):
        #Function to open JSON File.
        fh = open(filename, 'r')
        datastore = json.load(fh)
        if('name' in datastore and 'program' in datastore and 'description' in datastore):
            fh.close()
            return datastore
        else:
            print("Error found in JSON config file")
            sys.exit(1)
        
    def getAfternoon():
        #Try open program to get location metadata
        #If file can't be opened, print error and exit process.
        #Otherwise return output
        try:
            datastore = Services.morning("./Afternoon/config.json")
            command = "./Afternoon" + datastore['program']
            p = run(command, stdout=PIPE, input='', encoding='utf-8')
        except:
            print("Error: Cannot open file")
            sys.exit(1)
        else:
            return p.stdout

    def evening(filename):
        #Function to open JSON File.
        fh = open(filename, 'r')
        datastore = json.load(fh)
        if('name' in datastore and 'program' in datastore and 'description' in datastore):
            fh.close()
            return datastore
        else:
            print("Error found in JSON config file")
            sys.exit(1)
        
    def getEvening():
        #Try open program to get location metadata
        #If file can't be opened, print error and exit process.
        #Otherwise return output
        try:
            datastore = Services.morning("./Evening/config.json")
            command = "./Evening" + datastore['program']
            p = run(command, stdout=PIPE, input='', encoding='utf-8')
        except:
            print("Error: Cannot open file")
            sys.exit(1)
        else:
            return p.stdout

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
                fileSave("times.txt", str(Services.getTimeofday())+'\n')
                time.sleep(1)
            elif flow == 'geolocation':
                pEcho = re.sub(r'\$\$', flow, Services.echo())
                print(pEcho)
                fileSave("times.txt", str(Services.getGeolocation()))
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
    while (count < 1):
        time.sleep(60 - time.time() % 60)
        print(Services.getTimeofday())
        print("Sunrise: " + Services.sunrise() + " UTC")
        print("Sunset: " + Services.sunset() + " UTC")
        Flows.appendTimeOfDay()
        count += 1
    sys.exit(0)
main()

sys.exit(0)

