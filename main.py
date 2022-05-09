import math
dane=input().strip()
dane_czyste=dane.replace(" ","")
n=int(dane_czyste[0])
k=int(dane_czyste[1])

if k == 1 or n == k:
  print(1)
if k > n:
    print(0)        
else:
    a = math.factorial(n)
    b = math.factorial(k)
    wzor = a // (b*(n-k))
    print(wzor)