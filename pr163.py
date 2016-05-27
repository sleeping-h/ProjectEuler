from __future__ import division
l={} ## (a,b,c)
n=36
def intersect(q,w):
    a1,b1,c1=q[0],q[1],q[2]
    a2,b2,c2=w[0],w[1],w[2]
    if a1*b2==b1*a2:
        return False
    return True
def intersection(q,w):
    a1,b1,c1=q[0],q[1],q[2]
    a2,b2,c2=w[0],w[1],w[2]
    return ( -(c1*b2-c2*b1)/(a1*b2-a2*b1),-(c2*a1-a2*c1)/(a1*b2-a2*b1))

for x in range(n):
    for y in range(n-x):
        l[(1,0,-x)]=1
        l[(0,1,-y)]=1
        l[(1,1,-(x+y+1))]=1
        l[(1,-1,-(x-y))]=1
        l[(1,2,-(x+2*y+1))]=1
        l[(2,1,-(2*x+y+1))]=1
        
def inTriangle((x,y),l): ## l == n
    if x>=0 and y>=0 and x+y<=l:
        return True
    return False

a = l.keys()
t=len(a)
ans = 0
for i in range(t-2):
    for j in range(i+1,t-1):
        for k in range(j+1,t):
            if intersect(a[i],a[j]) and intersect(a[k],a[j]) and intersect(a[i],a[k]):
                q=intersection(a[i],a[j])
                w=intersection(a[k],a[j])
                e=intersection(a[i],a[k])
                if q==w==e:
                    continue
                if inTriangle(q,n) and inTriangle(w,n) and inTriangle(e,n): ans+=1
print ans
