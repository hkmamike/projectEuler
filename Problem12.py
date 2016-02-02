#!/usr/bin/python

import math
import time
import numpy
from customFunctions import *

start = time.time()

goal = 500
number = 0
i = 1


def nDivisors(parm):
    nod = 0
    sqrt = int(math.sqrt(parm))

    for i in xrange(1, sqrt):

        if (number % i == 0):
            nod += 2

    if (sqrt*sqrt == number):
        nod = nod - 1

    return nod

while (nDivisors(number) < goal):
    number += i
    i += 1

print number

end = time.time()
duration = end - start
print 'total runtime:', duration
