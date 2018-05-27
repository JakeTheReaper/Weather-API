#!/usr/bin/env python3

import requests
import json
import sys

def sunriseSunset():
    response = requests.get('https://api.sunrise-sunset.org/json?lat=-37.71528&lng=145.15056&date=today')
    data = response.text
    return json.dumps(json.loads(data), indent=2)

def main():
    try:
        fh = "sunriseSunset.json"
        file = open(fh, "w")
    except:
        print("Error: File not found")
        sys.exit(1)
    else:
        file.write(str(sunriseSunset()))

main()
