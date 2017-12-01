import Data.Array
import Data.List
import Data.Ord

optAct sd sc alpha b l e tmax = [ vs ! (0, s) | s <- [sd..sc]]
  where vs = listArray bounds [v t s | (t,s) <- range bounds]
        bounds = ((0,0), (tmax, sc))
        clip s = maximum [sd, minimum [s, sc]]
        v t s -- (prob, action) 
          | t == tmax && s == sd   = (0, -1) -- 最初は生きてる
          | t == tmax  = (1, -1) -- 最初のエネルギーは等確率に割り振る
          | s == sd    = (0, -1) -- 死んだら0
          | otherwise  = maximum' [ ( q t s a, a ) | a <- [0..4] ]
          where maximum' = maximumBy (comparing fst)
        q t s a = ( v1 * la + v2 * (1-la) ) * (1-ba) 
          where ea = e !! a
                la = l !! a
                ba = b !! a
                v1 = fst $ vs ! (t+1, clip (s-alpha+ea))
                v2 = fst $ vs ! (t+1, clip (s-alpha))

optActCombined sd sc alpha b l e tmax = [ optAct sd sc alpha b l e t | t <- [1..tmax]]

-- パラメータの例
-- b  = [0.01, 0.05, 0.1, 0.15, 0.0] -- 死ぬ確率
-- l  = [0.3, 0.5, 0.7, 0.9, 0] -- えさを見つける確率
-- e  = [2, 2, 2, 2, 0] -- もらえるえさのエネルギー

-- 参考
-- http://jelv.is/blog/Lazy-Dynamic-Programming/
