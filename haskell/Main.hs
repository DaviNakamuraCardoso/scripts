module Data.Char


expected x = error $ x ++ "expected"

expression x 
    | isDigit x = x
    | expected "Digit"
