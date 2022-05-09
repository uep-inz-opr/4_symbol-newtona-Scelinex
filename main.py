import math
dane_czyste=input().strip()
# dane_czyste=dane.replace(" ","")
n=int(float(dane_czyste[0]))
k=int(float(dane_czyste[2]))

if k == 1 or k == n:
  print(1)

if k > n:
    print(0)
           
else:
    a = math.factorial(n)
    b = math.factorial(k)
    wzor = a // (b*(n-k))
    print(wzor)