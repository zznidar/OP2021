DEBUG = false

function prinz(rest...)
    if(DEBUG)
        println(rest...)
    end
end


function eratosten(limit)
    if (limit < 3)
        return(0)
    end

    glavni = Set(2:limit)
    crtana = Set()
    prastevila = Set([2])

    #prinz(0, glavni, crtana, prastevila)

    while (maximum(prastevila)^2 < maximum(glavni))
        #prinz("pogoj", maximum(prastevila)^2, maximum(glavni))
        x = minimum(glavni)
        #prinz("x", x)
        push!(prastevila, x)
        #prinz("pra: ", prastevila)
        for i in x:x:limit
            push!(crtana, i)
        end
        #prinz("crtana", crtana)
        glavni = setdiff(glavni, crtana)
        #prinz("glavni sezna: ", glavni)
    end
    prastevila = union(prastevila, glavni)
    return(length(prastevila))

end


## methodswith(Set) vrne metode, ki se lahko izvedejo nad setom

#print("Vpiši število: ")
#a = parse(Int, readline())
@time println(eratosten(894209))