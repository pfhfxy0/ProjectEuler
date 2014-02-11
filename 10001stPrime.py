limit = 10001
count = 6
candidate = 14
primes = [2,3,5,7,11,13]


while (count < limit):
   for divisor in primes:
      if (candidate % divisor == 0):
         candidate += 1
         continue
   primes.append(candidate)
   candidate += 1
   count += 1
print "The ", count, "th prime number is ", max(primes)

