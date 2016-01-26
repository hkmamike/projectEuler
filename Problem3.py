#!/usr/bin/python

import math

prompt = 600851475143

bestAnswer = 1

n = 1

while n < math.sqrt(prompt):

  nPrime = True

  for i in xrange(2,int(round(math.sqrt(n)))):
    
    if (n % i == 0):

      nPrime = False



  if (prompt % n == 0 and nPrime == True):    

    bestAnswer = n

  n = n + 1

print bestAnswer


