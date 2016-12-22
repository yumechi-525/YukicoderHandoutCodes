require 'prime'

MAX_NUMBER = 20001
dp = Array.new(MAX_NUMBER, 0)
primes_list = Prime.each(MAX_NUMBER).to_a.reverse
n = gets.chomp.to_i
for i in primes_list do
    dp[i] = 1
end

for i in primes_list do
    (MAX_NUMBER-i-1).downto(i+1) do |j|
        if dp[j] > 0
            if dp[j]+1 > dp[j+i]
                dp[j+i] = dp[j]+1
            end
        end
    end
end

puts dp[n] > 0 ? dp[n] : -1
