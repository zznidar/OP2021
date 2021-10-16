a = 1
def scope():
    a = 5
    print("notranji", a)
scope()
print("zunanji", a)

a = 1
def scope():
    a = 7
    print("notranji", a)
scope()
print("zunanji", a)

## To je ekvivalent js 
## let a = 5
## Ampak je nelagodno, ker notranji scope ne more 
## dostopati do zunanjih spremenljivk