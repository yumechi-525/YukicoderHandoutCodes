a, b, x, y = gets.split(" ").map(&:to_f)
p  x * b >= y * a ? y + y * a / b : x + x * b / a
