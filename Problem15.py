#!/usr/bin/python

import math
import time
import numpy

start = time.time()


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print nCr(40, 20)

end = time.time()
duration = end - start
print 'total runtime:', duration
