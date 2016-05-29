type Point = (Integer,Integer)
type PointStep = (Point,Integer)

x=1000000000000
a25=33554432
a50=1125899906842624

rotate::Point -> Point -> Integer -> Point
rotate (x,y) (x0,y0) p = (x0-(y-y0)*p,y0+(x-x0)*p)

mid::Point -> Point -> Point
mid (x1,y1) (x2,y2) = ((x1+x2) `div` 2,(y1+y2) `div` 2)

next::PointStep -> PointStep -> Integer -> PointStep
next (p1,s1) (p2,s2) p = (rotate p2 (mid p1 p2) p, (s1+s2) `div` 2)

dr::PointStep -> PointStep -> Integer -> Point
dr (p1,s1) (p2 ,s2) p 
  |s1==x = p1
  |s2==x = p2
  |otherwise = let newPt = (next (p1,s1) (p2 ,s2) p)
	       in if ((s1+s2) `div` 2>=x) then (dr (p1,s1) newPt 1) else (dr newPt (p2,s2) (-1)) 

main = print $ dr ((0,0),0) ((a25,0),a50) 1