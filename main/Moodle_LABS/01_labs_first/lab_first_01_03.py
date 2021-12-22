import math
k = 0
summ_f = 0
while(k <= 12):
    f1 = math.factorial(k)
    f2 = math.factorial(3 + k)
    summ_1 = (math.sin(7/4 + k/2)* math.pi)/(f1 * f2)
    summ_f = summ_1 + summ_f
    k = k + 1
print(summ_f)