while True:

    n = int(input("digite um número: "))

    atual = 0
    primeiro = 0
    segundo = 1

    if n == 1 or n == 2:
        print("Sequencia Fibonacci: 1")
    elif n == 0:
        break
    else:
            for i in range (n - 1):
                atual = primeiro + segundo
                primeiro = segundo
                segundo = atual
            print ("Sequencia de Fibonacci: " , atual)