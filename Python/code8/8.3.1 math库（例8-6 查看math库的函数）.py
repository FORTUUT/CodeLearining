#8.3.1 math库（例8-6 查看math库的函数）
import math
print(dir(math))
print(math.e," ",math.pi," ",math.degrees(math.pi)," ",math.radians(45))
print(math.exp(2)," ",math.log10(2)," ",math.pow(5,3)," ",math.sqrt(3))
print(math.ceil(5.2)," ",math.floor(5.8)," ",math.trunc(5.8)," ",math.fabs(-5))
print(math.fmod(5,2)," ",math.fsum([0.1,0.2,0.3])," ",math.factorial(5))
print(math.isinf(1.0e+308)," ",math.isnan(1.2e3))

