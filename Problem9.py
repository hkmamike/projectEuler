#!/usr/bin/python

import math
import time

start = time.time()

def genTriplet(parm1, parm2):

#example if you want the 4th triplet for k < 1000
#print genTriplet(4, 1000)

    count = 0

    for i in xrange(1, int(math.ceil(parm2/2))):
        j = i + 1
        k = j + 1

        while (k <= parm2):
            while (k*k < i*i + j*j):
                k = k + 1

            if (k*k == i*i + j*j):
                count += 1

            if (k*k == i*i + j*j and count == parm1):
                return (i,j,k)

            j = j + 1


# This is super inefficient, I could have done the checking in the function
for x in xrange(1, 500):
    if (sum(genTriplet(x, 1000))==1000):
        print genTriplet(x, 1000)


end = time.time()
duration = end - start
print 'total runtime:', duration
