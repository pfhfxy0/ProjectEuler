#!/usr/bin/python

import math

primes = []
prime = 2
#target = 200
target = 2000000
flag = 1

while (prime < target):
   for i in primes:
      limit = math.sqrt(prime)
#      print "Trying ", i, " while limit is ", limit
      if (i > limit):
         break
      if ((prime % i) == 0):
#         print "Not prime: ", prime
         flag = 0
         break
   if (flag):
#      print "Found a prime ", prime
      primes.append(prime)
#      print "List of primes: ", primes
   flag = 1
   prime += 1

for i in primes:
   print i
