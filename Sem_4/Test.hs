{-
        cowsay like
-}

main :: IO ()
main = do
    putStr "Da el valor de n: "
    linea <- getLine
    let n = read linea :: Int
        r = esPrimo n
        fact = factPrimos n 2
    putStrLn $ "Es primo? " ++ show r
    putStrLn $ "Factores primos: " ++ show fact

esPrimo :: Int -> Bool
esPrimo n = (length [x | x <- [1..n], n `mod` x == 0]) == 2

factPrimos :: Int -> Int -> [Int]
factPrimos 1 _ = []
factPrimos n p
    | mod n p == 0 = p : factPrimos (div n p) p
    | otherwise = factPrimos n (sigPrimo p)

sigPrimo :: Int -> Int
sigPrimo n
    | esPrimo (n+1) = n+1
    | otherwise = sigPrimo (n+1)
