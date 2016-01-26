#!/usr/bin/python

import math

answer = 580085

factor1=0
factor2=0

for i in xrange(999, 99, -1):
  for j in xrange(999, 99, -1):

    checkNum = i*j
    length = len(str(checkNum))
    numberString = str(checkNum)
    printFlag = True

    if (length % 2 == 0):
      for k in xrange(0,length/2):
        if(numberString[k] != numberString[length-k-1]):
          printFlag = False

    else:
      for l in xrange(0,(length-1)/2):
        if (numberString[l] != numberString[length-l-1]):
          printFlag = False

    if (printFlag and checkNum > answer):
      answer = checkNum
      factor1 = i
      factor2 = j

print answer
print 'i =',factor1
print 'j =',factor2
