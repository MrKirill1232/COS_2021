import math
f = 0
k = 1
x = 1
u = math.pi/7.2
while(k <= 7):
    q = (u**k)/(2 * k - 1)*(2*k + 1)
    f = f + q
    k = k + 1
print(x * (1 + f)/(1 + f)**2 - (x**2)/4)