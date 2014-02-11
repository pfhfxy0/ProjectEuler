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

x = 999
y = 999

while (x >= 100 and y >= 100):
   multiple = x * y
   multiple_string = str(multiple)
   length = len(multiple_string)
   isPalindrome = True
   for i in range(length/2):
      if (multiple_string[i] != multiple_string[length - 1 - i]):
         isPalindrome = False
         break
   if (isPalindrome):
      print "The largest palindrome number", multiple, "can be created with three digit numbers", x, "and", y
      break
   if (x == y):
      x-=1
   else:
      y-=1



