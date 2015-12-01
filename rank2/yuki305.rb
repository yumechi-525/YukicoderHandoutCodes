res = ""
cnt = 0
curdigit = 0
lastnum = -1
while res != "unlocked" do
    inp = format("%010d", cnt)
    puts inp
    STDOUT.flush
    num, res = gets.chomp.split(" ")
    num = num.to_i
    if num == 10
        break
    end
    if lastnum == -1
        cnt += 10 ** curdigit
        lastnum = num
        elsif lastnum < num
        curdigit += 1
        lastnum = -1
        elsif lastnum > num
        cnt -= 10 ** curdigit
        curdigit += 1
        lastnum = -1
        else
        cnt += 10 ** curdigit
        lastnum = num
    end
end