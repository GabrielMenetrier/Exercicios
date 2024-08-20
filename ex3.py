def collatz_next(x):
    if x%2 == 0:
        return x//2
    else:
        return 3*x+1
    
def collatz_steps(k):
    if k == 1:
        return 0
    if k%2 != 0:
        return 3 + collatz_steps(collatz_next((3*k+1)//2))
    else:
        return 1 + collatz_steps(collatz_next(k))
    
def collatz_steps_std(x):
    if x == 1:
        return 0
    else:
        return 1 + collatz_steps(collatz_next(x))

n = int(input("Digite um número: "))
print(collatz_steps(n))
print(collatz_steps_std(n))
