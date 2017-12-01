main = do
    putStrLn "hello your name please"
    name <- getLine
    putStrLn ("hey " ++ name ++ ", !")
