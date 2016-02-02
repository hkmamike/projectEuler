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


lines = [int(i) for i in array]

answer = sum(lines)

shortAnswer = str(answer)[0:10]

print answer
print shortAnswer


end = time.time()
duration = end - start
print 'total runtime:', duration
