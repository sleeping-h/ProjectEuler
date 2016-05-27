x=1000000000000

rotate::(Integer,Integer) -> (Integer,Integer) -> Integer -> (Integer,Integer)
rotate (x,y) (x0,y0) p = (x0-(y-y0)*p,y0+(x-x0)*p)

mid::(Integer,Integer) -> (Integer,Integer) -> (Integer,Integer)
mid (x1,y1) (x2,y2) = ((x1+x2) `div` 2,(y1+y2) `div` 2)

next::((Integer,Integer),Integer) -> ((Integer,Integer),Integer) -> Integer -> ((Integer,Integer),Integer)
next (p1,s1) (p2,s2) p = (rotate p2 (mid p1 p2) p, (s1+s2) `div` 2)

dr::((Integer,Integer),Integer) -> ((Integer,Integer),Integer) -> Integer -> (Integer,Integer)
dr (p1,1000000000000) _ _ =  p1 
dr _ (p2 ,1000000000000) _ =  p2 
dr (p1,s1) (p2 ,s2) p = if ((s1+s2) `div` 2>=x) then (dr (p1,s1) (next (p1,s1) (p2 ,s2) p) 1) else (dr (next (p1,s1) (p2 ,s2) p) (p2,s2) (-1))

main = print $ dr ((0,0),0) ((33554432,0),1125899906842624) 1