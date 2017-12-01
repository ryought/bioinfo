-- http://jelv.is/blog/Lazy-Dynamic-Programming/
-- https://wiki.haskell.org/Lazy_evaluation
-- http://www.geocities.jp/m_hiroi/func/haskell03.html
import Data.Array

fib n = fibs !! n
  where fibs = 0 : 1 : zipWith (+) fibs (drop 1 fibs)


fib' max = go max
  where go 0 = 0
        go 1 = 1
        go n = fibs ! (n - 1) + fibs ! (n - 2)
        fibs = listArray (0, max) [go x | x <- [0..max]]


naive a b = d (length a) (length b)
  where d i 0 = i
        d 0 j = j
        d i j 
          | a !! (i - 1) == b !! (j - 1) = d (i - 1) (j - 1)
          | otherwise = minimum [ d (i - 1) j  + 1
                                , d i (j - 1)  + 1
                                , d (i - 1) (j - 1) + 1
                                ]

basic a b = d m n
  where (m, n) = (length a, length b)
        d i 0 = i
        d 0 j = j
        d i j 
          | a !! (i - 1) == b !! (j - 1) = ds ! (i - 1, j - 1)
          | otherwise = minimum [ ds ! (i - 1, j)   + 1
                                , ds ! (i, j - 1)   + 1
                                , ds ! (i - 1, j - 1) + 1
                                ]
        ds = listArray bounds
              [d i j | (i, j) <- range bounds ]
        bounds = ((0, 0), (m, n))

data Action = None | Add | Remove | Modify

script :: Eq a => (Action -> Distance) -> [a] -> [a] -> [Action]
