#!/usr/bin/python

import math


# 12252240 is the solution for LCM up to 18, which can be achieved by changing the j loop
for i in xrange(12252240, 100000000000, 20):

    flag = True

    for j in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        if (i % j != 0):
            flag = False

    if (flag):
        print i
        exit()
