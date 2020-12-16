solve xs = head [x * y * z | x <- xs, y <- xs, z <- xs, x + y + z == 2020]

main = interact $ show . solve . map (read :: String -> Int) . lines