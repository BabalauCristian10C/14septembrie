a,b = int(input("Nr 1: ")), int(input("Nr 2: "))

#a

def suma(x,y):
    return x+b;

#b

def prod(x,y):
    return x*y;

#c

def med(x,y):
    return (x+y)/2;

#d 

def divizor(x,y):
    a,b = [],[]
    for i in range(1,x+1):
        if (x%i == 0):
            a.append(i)
    for i in range(1,y+1):
        if (y%i == 0):
            b.append(i)   
    d = [a,b]
    return d;

def cmmdiv(l):
    c = []
    for i in l[0]:
        if(i in l[1]):
            c.append(i)
    return max(c)

#e - dl

def multiplii(x,y):
    #while 
    d = [a,b]
    return d;

#f
def minf(x,y):
    return min([x,y])

#g
def maxf(x,y):
    return  max([x,y])

#h 

def sumg(x,y):
    return f'{x} + {y} = {x+y}'

#i  
def prodg(x,y):
    return f'{x} * {y} = {x*y}'

#j

def div_com(l):
    c = []
    for i in l[0]:
        if(i in l[1]):
            c.append(i)
    return c

#k - 


#l

def cif_com(x,y):
    a,b,d = set(), set(), set()
    for i in str(x):
        a.add(i)
    for l in str(y):
        b.add(l)
    for i in a:
        if i in b:
            d.add(i)
    return d;

#m

def cif_dif(x,y):
    a,b,d = set(), set(), set()
    for i in str(x):
        a.add(i)
    for l in str(y):
        b.add(l)
    for i in a:
        if i not in b:
            d.add(i)
    return d;

#n

def friends(l):
    if (len(l[0]) == len(l[1])):
        print("numerele sunt prieteni")

divizori = divizor(a,b)
print(suma(a,b))
print(prod(a,b))
print(med(a,b))
print(cmmdiv(divizori))
print(minf(a,b))
print(maxf(a,b))
print(sumg(a,b))
print(prodg(a,b))
print(div_com(divizori))
print(cif_com(a,b))
print(cif_dif(a,b))
friends(divizori)
