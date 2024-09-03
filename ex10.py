lista0 = [3,4,8]
lista1 = [10,5,0]
lista2 = [2,6,7]

matrix = []

matrix.append(lista0)
matrix.append(lista1)
matrix.append(lista2)

def quadrado_magico(matriz):
    a = True
    soma_linha = []
    soma_coluna = []
    soma_diagonal1 = 0
    soma_diagonal2 = 0

    for i in range(len(matriz)):
        soma_coluna.append(0)
        soma_linha.append(0)
    
    for i in range (len(matriz)):
        soma_diagonal1 += matriz[i][i]
        soma_diagonal2 += matriz[len(matriz)-i-1][len(matriz)-i-1]
        for j in range(len(matriz)):
            soma_linha[i] += matriz[i][j]
            soma_coluna[i] += matriz[j][i]
    
    h = soma_coluna[0]
    for i in range(len(matriz)):
        if h != soma_coluna[i] or h != soma_linha[i] or h != soma_diagonal1 or h != soma_diagonal2:
            a = False
        if a == False:
            break
    return a

print(quadrado_magico(matrix))