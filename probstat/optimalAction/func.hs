hoge 10 = 1
hoge 20 = 100
hoge _ = 0

hoge2 tmax x = hoge3 x
  where hoge3 x | x == tmax  = 100
                | otherwise  = 0

v t s 
  | t == 10 && s == 0  = 1000
  | t == 10  = 0
  | otherwise = 1

fib' max = go max
  where go 0 = 0
        go 1 = 1
        go n = fibs ! (n - 1) + fibs ! (n - 2)
        fibs = listArray (0, max) [go x | x <- [0..max]]

fib4 max = go 0
  where go n
          | n == max      = 0
          | n == max-1    = 1
          | otherwise     = fibs ! (n + 1) + fibs ! (n + 2)
        fibs = listArray (0, max) [go x | x <- [0..max]]

fib2 max = fibs ! max
  where fibs = array (0, max) $ [ (0, 1) ] ++ [ (1, 1) ] ++ [ (n, fibs ! (n-1) + fibs ! (n-2)) | n <- [2..max]]

twodim max = arr ! (max, max)
  where arr = listArray bounds [ go x y | (x,y) <- range bounds ]
        bounds = ((0,0), (max, max))
        go 0 _ = 1
        go _ 0 = 1
        go x y = arr ! (x-1, y) + arr ! (x, y-1)
