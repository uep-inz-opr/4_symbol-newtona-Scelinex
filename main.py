import math
dane=input().split()
n=int(dane[0])
k=int(dane[1])

if n == 0:
    print(1)
elif k == 0:
    print(1)
elif k == n:
  print(1)
elif k > n:
  print(0)        
else:
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n - k)
    wzor = a // (b*c)
    print(wzor)
