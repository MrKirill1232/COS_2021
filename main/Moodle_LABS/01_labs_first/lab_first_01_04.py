import math
i = 3
summ_f = 1
while(i <= 11):
    summ_1 = i**2 + math.tan(i*(math.pi/2.34))
    summ_f = summ_1 * summ_f
    i = i + 1
print(summ_f)