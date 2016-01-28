#!/usr/bin/python

import math
import time
import numpy

start = time.time()




filename = "problem11prompt.txt"

with open(filename, "r") as feed:
    array = []
    for line in feed:
        array.append(line)

#print array

array2 = []

for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    array2.append(k)
#print array2

promptMatrix = numpy.matrix(array2)

print promptMatrix

answer = 1

for i in range(17):
    for j in range(17):
        prodHorizon = promptMatrix[i,j] * promptMatrix[i+1,j] * promptMatrix[i+2,j] * promptMatrix[i+3,j]
        if (prodHorizon > answer):
            answer = prodHorizon

        prodVert = promptMatrix[i,j] * promptMatrix[i,j+1] * promptMatrix[i,j+2] * promptMatrix[i,j+3] 
        if (prodVert > answer):
            answer = prodVert

        prodDiag = promptMatrix[i,j] * promptMatrix[i+1,j+1] * promptMatrix[i+2,j+2] * promptMatrix[i+3,j+3]
        if (prodDiag > answer):
            answer = prodDiag

for i in range(19,2,-1):
    for j in range(17):
        prodDiag2 = promptMatrix[i,j] * promptMatrix[i-1,j+1] * promptMatrix[i-2,j+2] * promptMatrix[i-3,j+3]
        if (prodDiag2 > answer):
            answer = prodDiag2

for i in range(15, 20):
    for j in range(17):
        prodVert2 = promptMatrix[i,j] * promptMatrix[i,j+1] * promptMatrix[i,j+2] * promptMatrix[i,j+3] 
        if (prodVert2 > answer):
            answer = prodVert2

for i in range(17):
    for j in range(15,20):
        prodHorizon2 = promptMatrix[i,j] * promptMatrix[i+1,j] * promptMatrix[i+2,j] * promptMatrix[i+3,j]
        if (prodHorizon2 > answer):
            answer = prodHorizon2

print answer


end = time.time()
duration = end - start
print 'total runtime:', duration
