
def f (x):
    if 0<= x <= 10:
        print(x)
    else:
        if 0 <= (z := int(input("Nota inválida, digite novamente: "))) <= 10:
            print(z)
        else:
            f (x)

n = int(input("Digite uma nota entre 0 e 10: "))

f(n)