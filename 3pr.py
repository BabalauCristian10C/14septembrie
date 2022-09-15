a,b,c,d = int(input()), int(input()),int(input()), int(input())

def fract(a,b,c,d):
    return [((a*d+c*b)/(b*d))]

print(fract(a,b,c,d))
