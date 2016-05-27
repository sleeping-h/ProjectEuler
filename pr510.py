ans,x,y=0,1,1
from fractions import gcd 
p=10**9
while (x+y)**2*y**2<=p: 
    while (x+y)**2*y**2<=p:
        if gcd(x,y)==1:
            k=p/((y+x)*y)**2
            if k==0: break
            ans+=((x*y)**2+(x*(x+y))**2+(y*(x+y))**2)*k*(k+1)/2
        y+=1
    y=x+1
    x+=1
print ans
