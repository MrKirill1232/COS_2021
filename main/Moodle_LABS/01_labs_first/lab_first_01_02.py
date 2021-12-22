import math
k = 1
summ_f = 0
while(k <= 23):
    summ_1 = k * (math.cos(k * (3.14 / 3)))
    summ_f = summ_f + summ_1
    k = k + 1
print(summ_f)