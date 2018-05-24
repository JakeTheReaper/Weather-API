#!/usr/bin/env python3

import sys
from ifttt import timeofday, geolocation

try:
    file = open("times.txt", "w")
except IOError:
    print("Error: File not found")
    sys.exit(0)
else:
    print("File opened successfully")
    file.write(str(timeofday())+'\n')
    file.write(str(geolocation()))
    file.close()
