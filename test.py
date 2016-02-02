#!/usr/bin/python

import math
import time
import numpy
from customFunctions import *

start = time.time()

print numberOfFactors(1000)

end = time.time()
duration = end - start
print 'total runtime:', duration
