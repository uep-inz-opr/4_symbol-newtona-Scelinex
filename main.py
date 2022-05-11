import math
dane=input().split()
n=int(dane[0])
k=int(dane[1])

if k == n:
  print(1)
elif k > n:
  print(0)        
else:
    a = math.factorial(n)
    b = math.factorial(k)
    wzor = a // (b*(n-k))
    print(wzor)
