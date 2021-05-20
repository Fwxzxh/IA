{-
    Programa: neuronal0.hs
    Función:  Reconocer objetos de un conjunto, de acuerdo
              a valores de características
              Por ejemplo ancho y alto de frutas
-}

import Text.Printf

main :: IO ()
main = do
    putStr "Ancho: "
    entrada1 <- getLine
    putStr "Alto: "
    entrada2 <- getLine
    let
        ancho = read entrada1 :: Double
        alto = read entrada2 :: Double
    proyeccion "Tipo A" 4.0 6.0 ancho alto
    proyeccion "Tipo B" (-10.0) 12.0 ancho alto
    proyeccion "Tipo C" 17.0 (-20.0) ancho alto
    proyeccion "Tipo D" (-35.0) (-22.0) ancho alto

prodEscalar :: Num a => a -> a -> a -> a -> a
prodEscalar x1 y1 x2 y2 = x1*x2 + y1*y2

norma :: Floating a => a -> a -> a
norma x y = sqrt (x**2 + y**2)

proyeccion :: (PrintfArg t, Floating t) => [Char] -> t -> t -> t -> t -> IO ()
proyeccion categoria anchoTip altoTip ancho alto = do
    let
        normaTip = norma anchoTip altoTip
        normaAct = norma ancho alto
        proyeccion = prodEscalar anchoTip altoTip ancho alto
        proyUnit = proyeccion / normaTip / normaAct
    putStrLn $ categoria ++ ": " ++ printf "%7.4f" proyUnit
