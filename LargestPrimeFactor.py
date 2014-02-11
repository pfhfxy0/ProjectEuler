#!/usr/bin/python

import sys, getopt

def options(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile


def find_prime(x):
   while (1):
      x += 1
      i = 2
      isPrime = True
      while (x > i):
         if (x % i == 0):
            isPrime = False
            break
         i += 1
      if (isPrime):
         return x


options(sys.argv[1:])

prime = 2
orig = 600851475143
num = orig

sum = 0

while (prime < num):
   prime = find_prime(prime)
   if (num % prime == 0) :
      print prime
      num /= prime

print "The largest prime number for ", orig, " is ", prime


