solve xs = head [x * y | x <- xs, y <- xs, x + y == 2020]

main = interact $ show . solve . map (read :: String -> Int) . lines