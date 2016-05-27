from __future__ import division
from math import factorial as f

n=30
ans=1
s=1
for i in range(1,n+1): # magic goes here
        ans=i*ans+(2**(i-1)-1)*s
        s*=i
print ans/f(n)
