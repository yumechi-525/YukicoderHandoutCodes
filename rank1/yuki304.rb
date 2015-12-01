res = ""
cnt = 0
while res != "unlocked" do
    key = format("%03d", cnt)
    puts key
    STDOUT.flush
    res = gets.chomp
    if res == "locked"
        cnt += 1
    end
end