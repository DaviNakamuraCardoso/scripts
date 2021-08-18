module main where

main :: IO ()

factorial :: (Integral a) => a -> a

factorial n = product [1..n]


