require 'prime'
i=gets.chomp.to_i
a=i.prime_division.map{|p,n|[p]*n}.flatten
puts i==1?"1 1":"#{a[0]} #{a.inject{|s,n|s*n}/a[0]}"