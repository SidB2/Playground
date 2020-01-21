def recursiveFunction(n):
   if n <= 1:
       return n
   else:
       return(recursiveFunction(n-1) + recursiveFunction(n-2))

# Has to do with fibbonachi numbers.

for x in range(0, 10):
    print (recursiveFunction(x))