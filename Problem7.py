#!/usr/bin/python

import math
import time

start = time.time()

counter = 2
goal = 10001
checkNum = 3


while (counter < goal):
    checkNum += 2
    isPrime = True
    checkSize = int(math.sqrt(checkNum))+1

    for i in xrange(2, checkSize):

        if (checkNum % i == 0):
            #print checkNum, 'is not Prime'
            isPrime = False

    if (isPrime):
        counter = counter + 1


print checkNum


















end = time.time()
duration = end - start
print 'total runtime:', duration
