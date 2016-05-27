from __future__ import division
import math

def rotate((x1,y1),(x0,y0),l):
    """rotation CCW, angle l, around x0,y0"""
    return ((x1-x0)*math.cos(l)-(y1-y0)*math.sin(l)+x0,
            (x1-x0)*math.sin(l)+(y1-y0)*math.cos(l)+y0)
def div((x1,y1),(x2,y2),n,k):
    """point at n/k of segment"""
    return (x1+n*(x2-x1)/k,y1+n*(y2-y1)/k)
def topPoints((x1,y1),(x2,y2)):
    return rotate((x1,y1),(x2,y2),-math.pi/2), rotate((x2,y2),(x1,y1),math.pi/2)
def nextPoints((x3,y3),(x4,y4)):
    return (rotate((x4,y4),rotate(div((x3,y3),(x4,y4),1,5),(x4,y4),math.asin(0.6)),-math.pi/2),
            rotate(rotate(div((x3,y3),(x4,y4),1,5),(x4,y4),math.asin(0.6)),(x4,y4),math.pi/2),
            rotate(rotate(div((x3,y3),(x4,y4),3,5),(x3,y3),-math.asin(0.8)),(x3,y3),-math.pi/2),
            rotate((x3,y3),rotate(div((x3,y3),(x4,y4),3,5),(x3,y3),-math.asin(0.8)),math.pi/2))
            
xmin,xmax,ymin,ymax=100,0,100,0
        
def pTreeL((x1,y1),(x2,y2),n):
    global xmin,xmax,ymin,ymax
    (x3,y3),(x4,y4)=topPoints((x1,y1),(x2,y2))
    xmin=min(xmin,x1,x2,x3,x4)
    if n:
        (x5,y5),(x6,y6),(x7,y7),(x8,y8)=nextPoints((x3,y3),(x4,y4))
        if min(x5,x6)<min(x7,x8):
            pTreeL((x4,y4),rotate(div((x3,y3),(x4,y4),1,5),(x4,y4),math.asin(0.6)),n-1)
        else:                                                                                  
            pTreeL(rotate(div((x3,y3),(x4,y4),3,5),(x3,y3),-math.asin(0.8)),(x3,y3),n-1)
        
def pTreeR((x1,y1),(x2,y2),n):
    global xmin,xmax,ymin,ymax
    (x3,y3),(x4,y4)=topPoints((x1,y1),(x2,y2))
    xmax=max(xmax,x1,x2,x3,x4)
    if n:
        (x5,y5),(x6,y6),(x7,y7),(x8,y8)=nextPoints((x3,y3),(x4,y4))
        if max(x5,x6)>max(x7,x8):
            pTreeR((x4,y4),rotate(div((x3,y3),(x4,y4),1,5),(x4,y4),math.asin(0.6)),n-1)
        else:                                                                                  
            pTreeR(rotate(div((x3,y3),(x4,y4),3,5),(x3,y3),-math.asin(0.8)),(x3,y3),n-1)
        
def pTreeT((x1,y1),(x2,y2),n):
    global xmin,xmax,ymin,ymax
    (x3,y3),(x4,y4)=topPoints((x1,y1),(x2,y2))
    ymax=max(ymax,y1,y2,y3,y4)
    if n:
        (x5,y5),(x6,y6),(x7,y7),(x8,y8)=nextPoints((x3,y3),(x4,y4))
        if max(y5,y6)>max(y7,y8):
            pTreeT((x4,y4),rotate(div((x3,y3),(x4,y4),1,5),(x4,y4),math.asin(0.6)),n-1)
        else:                                                                                  
            pTreeT(rotate(div((x3,y3),(x4,y4),3,5),(x3,y3),-math.asin(0.8)),(x3,y3),n-1)
        
def pTreeB((x1,y1),(x2,y2),n):
    global xmin,xmax,ymin,ymax
    (x3,y3),(x4,y4)=topPoints((x1,y1),(x2,y2))
    ymin=min(ymin,y1,y2,y3,y4)
    if n:
        (x5,y5),(x6,y6),(x7,y7),(x8,y8)=nextPoints((x3,y3),(x4,y4))
        if n>895 or min(y5,y6)<min(y7,y8):
            pTreeB((x4,y4),rotate(div((x3,y3),(x4,y4),1,5),(x4,y4),math.asin(0.6)),n-1)
        else:                                                                                  
            pTreeB(rotate(div((x3,y3),(x4,y4),3,5),(x3,y3),-math.asin(0.8)),(x3,y3),n-1)

pTreeL((0,0),(1,0),990)
pTreeT((0,0),(1,0),990)
pTreeB((0,0),(1,0),900)
pTreeR((0,0),(1,0),990)
print xmin,xmax,ymin,ymax
print "ans =",(xmin-xmax)*(ymin-ymax)

