import Data.Array

routeCount :: Int -> Int -> Integer
routeCount width height =
  routes ! (width, height)
    where routes = array ((0, 0), (width, height)) $
            -- 一番下の行の経路数はすべて1
            [ ((x, 0), 1) | x <- [0..width] ] ++
            -- 一番左の列の経路数はすべて1
            [ ((0, y), 1) | y <- [1..height] ] ++
            -- 残りは、左と下の点までの経路数の和
            [ ((x, y), routes ! (x - 1, y) + routes ! (x, y - 1))
              | x <- [1..width], y <- [1..height] ]

main = print $ routeCount 5 4
