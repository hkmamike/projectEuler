#!/usr/bin/python

import math
import time

start = time.time()

counter = 2
goal = 2000000
checkNum = 3
total = 5


while (checkNum < goal):
    checkNum += 2
    isPrime = True
    checkSize = int(math.sqrt(checkNum))+1

    for i in xrange(2, checkSize):

        if (checkNum % i == 0):
            #print checkNum, 'is not Prime'
            isPrime = False

    if (isPrime):
        total = total + checkNum

print total



end = time.time()
duration = end - start
print 'total runtime:', duration
