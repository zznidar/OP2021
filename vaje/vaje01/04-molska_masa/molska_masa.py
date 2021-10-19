## Periodni sys
ps = {"Cu": 63.5,
"S": 32.1,
"O": 16.0,
"H": 1.0}

stopnja_hidratacije = float(input("Stopnja hidratacije: "))

## Molska masa
M = (ps["Cu"] + 
ps["S"] + 
ps["O"]*4 +
stopnja_hidratacije * (
    ps["H"]*2 +
    ps["O"]
) 
)

print(f"Molska masa je {M} g/mol.")