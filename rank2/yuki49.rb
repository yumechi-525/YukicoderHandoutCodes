s = gets.chomp
first, second = 0, 0
lastmark = ""
flag = false
for c in s.split(//) do
    if c == "*"
        if flag
            if lastmark == "*"
                first = first + second
            else
                first = first * second
            end
            second = 0
        else
            flag = true
        end
        lastmark = c
    elsif c == "+"
        if flag
            if lastmark == "*"
                first = first + second
            else
                first = first * second
            end
            second = 0
        else
            flag = true
        end
        lastmark = c
    else
        if flag
            second *= 10
            second += c.to_i
        else
            first *= 10
            first += c.to_i
        end
    end
end
puts (lastmark == "*") ? (first + second) : (first * second)
