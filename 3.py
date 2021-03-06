a= int(input("First Number: "))
b= int(input("Second Number: "))
def gcd(x,y):
    if y == 0:
        return int(x)
    else:
        return gcd(y,x%y)
def lcm(x,y):
    g = gcd(x,y)
    return int(g * (x/g) * (y/g))
g = gcd(a,b)
l = lcm(a,b)
print('GCD : ',g, 'LCD: ',l)