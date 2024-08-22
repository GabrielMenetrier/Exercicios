def integral(f,a,b,dx=0.001):
    if a>b:
        return 0
    else:
        return dx*f(a) + integral(f,a+dx,b,dx=0.001)
    
def integral2(f,a,b,dx=0.001):
    z = 0
    i = 0
    while a+i*dx < b:
        z = z + dx*f(a+i*dx)
        i = i+1
    return z

def integral_for(f,a,b,dx=0.001):
    z = 0
    for i in range(int((b-a)/dx)):
        z = z + dx*f(a+i*dx)
    return z



print(integral(lambda x: x+x**4+35, 0, 1, 0.01))
print(integral2(lambda x: x+x**4+35, 0, 1,0.01))
print(integral_for(lambda x: x+x**4+35, 0, 1,0.01))
