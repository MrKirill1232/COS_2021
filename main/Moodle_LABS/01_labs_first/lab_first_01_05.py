import math

i = 1
summ_f = 1

while(i <= 12):
    step = ( ( 0.72 / math.sqrt(i) ) + ( ( 0.49 / 2 * i ) ) )
    summ_w = ( 1 - ( 0.72 / math.sqrt(i) )) * math.e**(step)
    summ_f = summ_f * summ_w
    i = i + 1
print(summ_f)