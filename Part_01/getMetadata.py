#!/usr/bin/env python3

import requests
import json
import sys

def getMetadata():
    response = requests.get('https://api.darksky.net/forecast/8022842c05a3738bb882a93cf7d09d98/-37.71528,145.15056')
    data = response.text
    return json.dumps(json.loads(data), indent=2)

def main():
    print(str(getMetadata()))

main()
