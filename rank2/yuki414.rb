require 'prime'

i = gets.chomp.to_i
if Prime.prime?(i) || i == 1
  puts "1 #{i}"
else
  arr = i.prime_division.map {|p,n| [p]*n }.flatten
  a = arr.inject {|sum, n| sum * n } / arr[0]
  puts "#{arr[0]} #{a}"
end