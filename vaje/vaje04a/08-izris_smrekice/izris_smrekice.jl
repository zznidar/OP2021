print("Vpiši višino: ")
h = parse(Int, readline())

for let_i in 0:h-1
    #println(h-1-let_i)
    println(" " ^ (h-1-let_i) * "*" ^ (let_i*2 + 1))
end
