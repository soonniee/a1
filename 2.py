a = [3,2,1]
b= [0,0,0]
c=[0,0,0]
step = 0
def num(rods):
    cnt = 0
    for r in rods:
        if r != 0:
            cnt+=1
    return cnt
def hanoi(n, x, y, z):
    global step
    step+=1
    if n == 1:
        # print('a: ',a[0],'->','c: ',c[0])
        y_rods = num(y)
        x_rods = num(x)
        y[y_rods]=x[x_rods-1]
        x[x_rods-1]=0
        print('a:', a, 'b:', b, 'c: ',c)
        return
    hanoi(n-1,x,z,y)
    x_rods = num(x)
    y_rods = num(y)
    # print('a: ',a[a_rods],'->','b')
    y[y_rods] =x[x_rods-1]
    x[x_rods-1] = 0
    print('a:', a, 'b:', b, 'c: ',c)
    hanoi(n-1,z,y,x)
print('Initial:','a:', a, 'b:', b, 'c: ',c)
hanoi(3,a,b,c)
print('Total',step,'steps')