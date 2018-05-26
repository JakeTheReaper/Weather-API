#!/usr/bin/env python3
#Student Name: Jake Duran Zerafa
#Student No: s3679109

import datetime

def timeofday():
    #Get the time of day, format and return the output. 
    now = datetime.datetime.now()
    formattedDate = now.strftime('%d/%m/%Y %H:%M:%S')
    return formattedDate

def main():
    print(timeofday())

main()


