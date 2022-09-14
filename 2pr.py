n,m = int(input()), int(input())
def fractional(n):
    c =1 
    for i in range(1,int(n)+1):
        c *= int(i)
    return c
if (n>m):
    print(fractional(n)/(fractional(m)*fractional(n-m)))
