f=[]
a,b=1,1
while a<10**17:
    f.append(a)
    a,b=b,a+b

	
f.append(f[-1]+f[-2])
class c(dict):
    def __missing__(self,keys):
            return 0

	
z=c()
z[0]=1
z[1]=2
for i in range(2,84):
    z[i]=f[i]+z[i-2]+z[i-1]
def q(x):
    if x+1 in f:
            return z[f.index(x+1)-2]
    i=0
    while f[i]-1<x:
            i+=1
    i-=1
    return z[i-2]+x-f[i]+1+q(x-f[i])
print q(10**17-1)
