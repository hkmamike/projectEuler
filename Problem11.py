#!/usr/bin/python

import math
import time
import numpy

start = time.time()


filename = "problem13prompt.txt"

with open(filename, "r") as feed:
    array = []
    for line in feed:
        array.append(line)




end = time.time()
duration = end - start
print 'total runtime:', duration
