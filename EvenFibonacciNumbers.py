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

x = 1
y = 2
#max = 10
max = 4000000

print x
print y
sum = 0
new = 0

while x + y < max:
   new = x + y
   x = y
   y = new
   print new
   if (new % 2 == 0) :
      sum += new

print "The sum is ", sum




