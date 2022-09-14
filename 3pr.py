a,b,c,d = int(input()), int(input()),int(input()), int(input())

def fract(a,b,c,d):
    return [((a*c)/(b*d)), ((a*d)/(b*c))]

print(fract(a,b,c,d))
