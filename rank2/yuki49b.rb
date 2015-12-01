nums = []
marks = []
line = gets.chomp
num = 0
for c in line.split(//) do
    if c == "*" or c == "+"
        marks.push(c)
        nums.push(num)
        num = 0
        else
        num = num * 10 + c.to_i
    end
end
nums.push(num)

for i in 0...marks.length do
    nums[0] = marks[i] == "*" ? nums[0] + nums[i+1] : nums[0] * nums[i+1]
end
puts nums[0]