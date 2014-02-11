
for a in range(1,999):
   for b in range(1,1000-a-1):
      c = 1000 - a - b
#      aa = a*a
#      bb = b*b
#      cc = c*c
#      print aa, bb, aa+bb, cc
      if (a*a + b*b == c*c):
         print a, b, c
