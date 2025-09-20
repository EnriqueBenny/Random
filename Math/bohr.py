
r=1.09737e7
e0=8.854e-12
limit=8

for i in range(3, limit+1):
    n=6
    while i < n:
        l= r*((1/i**2)-(1/n**2))
        print((1/l)*1e9)
        n-=1

