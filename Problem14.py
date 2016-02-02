#!/usr/bin/python

import math
import time
import numpy

start = time.time()

limit = 1000000


def collatzSequence(parm):
    current = parm
    sequence = [current]

    while (current != 1):

        if (current % 2 == 0):
            current = current / 2
        else:
            current = 3 * current + 1

        sequence.append(current)

    return sequence

longestStart = 1
maxLength = 1

for i in xrange(1, limit):

    seq = collatzSequence(i)
    length = len(seq)

    if (length > maxLength):
        longestStart = i
        maxLength = length

    if (i % 10000 == 0):
        print longestStart
        print len(collatzSequence(i))

print longestStart

end = time.time()
duration = end - start
print 'total runtime:', duration
