#!/usr/bin/python

import math
import time
import numpy


def triGen(parm):
    total = (parm+1) * parm / 2
    return total


def countDivisor(parm):
    count = 0

    for i in xrange(1, int(math.sqrt(parm+1))+1):

        if (parm % i == 0):

            count += 2

    return count


def factoring(parm):
    checkList = atkinSieve(parm)
    remainder = parm
    result = []

    while (remainder != 1):

        for i in checkList:
            if (remainder % i == 0):
                remainder = remainder / i
                result.append(i)
                break
    return result


def nDivisors(parm):
    nod = 0
    sqrt = int(math.sqrt(parm))

    for i in xrange(1, sqrt):

        if (number % i == 0):
            nod += 2

    if (sqrt*sqrt == number):
        nod = nod - 1

    return nod


#not sure if correct
def atkinSieve(parm):
    primes = [2, 3, 5]

    #position zero is never used
    sieve = [False] * (parm + 1)

    checkLim = int(math.sqrt(parm))+1

    for i in xrange(1, checkLim):
        for j in xrange(1, checkLim):
            n = 4*i**2 + j**2
            if (n <= parm) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3*i**2 + j**2
            if (n <= parm) and (n % 12 == 7):
                sieve[n] = not sieve[n]

            if i > j:
                n = 3*i**2-j**2
                if (n <= parm) and (n % 12 == 11):
                    sieve[n] = not sieve[n]

    for k in range(5, checkLim):
        if sieve[k]:
            for l in range(k**2, parm, k):
                sieve[l] = False

    for k in range(7, parm):
        if sieve[k]:
            primes.append(k)

    return primes
