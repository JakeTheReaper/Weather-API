#!/usr/bin/env python3

import sys

def fileSave(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

