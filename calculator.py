#!/usr/bin/env python3
import sys

i = int(sys.argv[1])
t = i - 5000
if  0<= t <=3000:
    r = t*0.03-0
    print(format(r,".2f"))
elif 3000 < t <=12000:
    r = t*0.1-210
    print(format(r,".2f"))
elif 12000 < t <=25000:
    r = t*0.2-1410
    print(format(r,".2f"))
elif 25000 < t <=35000:
    r = t*0.25-2660
    print(format(r,".2f"))
elif 35000 < t <=55000:
    r = t*0.3-4410
    print(format(r,".2f"))
elif 55000 < t <=80000:
    r = t*0.35-7160
    print(format(r,".2f"))
elif t >80000:
    r = t*0.45-15160
    print(format(r,".2f"))
