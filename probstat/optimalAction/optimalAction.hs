import Data.Array


optAct tmax sd sc = [ vs ! (0, s) | s <- [sd..sc]]
  where vs = listArray bounds [v t s | (t,s) <- range bounds]
        bounds = ((0,0), (tmax, sc))
        clip s = maximum [sd, minimum [s, sc]]
        v t s
          | t == tmax && s == sd   = 0 -- 最初は生きてる
          | t == tmax  = 1 -- エネルギーは等確率
          | s == sd    = 0 -- 死んだら0
          | otherwise  = maximum [ q t s a | a <- [0..4] ]
        q t s a = ( v1 * la + v2 * (1-la) ) * (1-ba) 
          where ea = e !! a
                la = l !! a
                ba = b !! a
                v1 = vs ! (t+1, clip (s-1+ea))
                v2 = vs ! (t+1, clip (s-1))
                b = [0.01, 0.05, 0.1, 0.15, 0]
                l = [0.3, 0.5, 0.7, 0.9, 0]
                e = [2, 2, 2, 2, 0]

-- optAction tf sd sc ss = v 0 ss
--   where v tf s 
--           | s == sd   = 0
--           | otherwise = 1
--         v _ sd = 0 
--         v t s = maximum [ q t s aa | aa <- [sd..sc] ]
--         q t sd a = 0
--         q t s a = (v1 * la + v2 * (1 - la)) * (1-ba)
--           where ea = e !! a
--                 v1 = vs ! ((t+1), clip (s-a-ea))
--                 v2 = vs ! ((t+1), clip (s-a))
--                 ba = b !! a 
--                 la = l !! a
--         vs = listArray bounds [v t s | (t, s) <- range bounds]
--         bounds = ((0, sd), (tf, sc))

--optAct :: Int -> Int -> Integer

-- main = do
    -- print $ fib2 100
    -- print (optAction 6 0 20 10)

