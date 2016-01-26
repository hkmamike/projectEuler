#!/usr/bin/python

import math

sumAnswer = 0

sqAnswer = 0

sqTemp = 0

for i in xrange(1, 101):
    sqTemp = sqTemp + i

sqAnswer = sqTemp**2

for j in xrange(1, 101):
    sumAnswer = sumAnswer + j**2

print 'Sq of Sum', sqAnswer
print 'Sum of Sq', sumAnswer

answer = sqAnswer - sumAnswer

print 'answer', answer
