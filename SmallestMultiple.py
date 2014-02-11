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


options(sys.argv[1:])

max = 20
#max = 10
target = max

sum = 1
for i in range (2, max+1):
   sum += i * sum
print sum

while (1):
   found = True
   target += 1
#   print target
   for i in range(2, max + 1):
      if (target % i != 0):
         found = False
         break
   if (found):
      print "The largest multiple is", target
      break



