#!/usr/bin/env python3
import re

echo = "Input is $$"

replace = re.sub(r'\$\$', 'NOW', echo)

print(replace)


