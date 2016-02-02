#!/usr/bin/python

import math
import time
import numpy

start = time.time()


gridSize = 4

answer = 2**gridSize + (2**gridSize-2)*2

print answer

end = time.time()
duration = end - start
print 'total runtime:', duration
