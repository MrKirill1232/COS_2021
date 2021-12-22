import math
import scipy.integrate as integrate
x = 1

for_1_1 = 1 + 2.34 * x + 4.71 * x**2

for_1_2 = ( 1 + x**2 )**( 1 / 4 )

print ( integrate.quad( lambda x: (for_1_1 / for_1_2),1.23,9.87) )