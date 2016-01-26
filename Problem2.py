#!/usr/bin/python

import cmath

nMinus1 = 1
n = 2
answer = 0


while n < 4000000:

  if (n % 2 == 0):
    answer = answer + n
  
  n = n + nMinus1
  nMinus1 = n - nMinus1
  


print answer


