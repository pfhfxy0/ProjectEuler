limit = 100
SumOfSquare = 0
SquareOfSum = 0
for i in range(1,limit+1):
   SumOfSquare += i*i
   SquareOfSum += i
SquareOfSum = SquareOfSum * SquareOfSum 
print "Difference between the sum of the squares and the square of the sum of 1 through ", limit, " is: ", SquareOfSum - SumOfSquare
