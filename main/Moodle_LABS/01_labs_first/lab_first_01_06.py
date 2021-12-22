import math

i = 1
summ_f = 0

while ( i <= 20 ):
    upper_s = 1
    lower_s = 1
    n = i-1
    for n in range (i):
        upper_s = upper_s * math.log10(i+1)
    n = i-1
    for n in range (i):
        lower_s = lower_s * math.log10(i+1+0.2)
    summ_f = summ_f + ( upper_s / lower_s )
    i = i + 1
print (summ_f)
