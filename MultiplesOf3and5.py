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

x = 3
y = 5
max = 1000

sum = 0
for i in range(max) :
   if ((i % x  == 0) or (i % y == 0)) :
      print i
      sum += i

print "The sum is ", sum




