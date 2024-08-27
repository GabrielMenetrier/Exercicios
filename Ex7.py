import math

def palindromo (palavra): #confere se a palavra é um políndromo
    leng = len(palavra)
    z = True
    for i in range (leng):
        if palavra[i] != palavra[leng-i-1]:
            z = False
    return z

def senha(palavra): #confere se a palavra inputada respeita algumas características
    a = False
    b = False
    c = False
    leng = len(palavra)
    for i in range(leng):
        if str.isupper(palavra[i]) == True:
            a = True
        if not str.isalnum(palavra[i]) and not str.isspace(palavra[i]):
            b = True
        if str.isnumeric(palavra[i]):
            c = True
    if not a or not b or not c:
        print("Sua senha não é válida")
    else:
        print("Senha Válida")

def validar_cpf (n): # confere se o CPF inserido é válido
    k = n.replace(".","")
    j = k.replace("-","")
    x = int(j)
    v1_passo1 = 0
    for i in range (8):
        v1_passo1 += int(j[i])*(9-((8-i)%10))
    v1 = (v1_passo1%11)%10

    v2_passo1 = 0
    for i in range (8):
        v2_passo1 += int(j[i])*(9-((9-i)%10))
    v2 = ((v2_passo1+v1*9)%11)%10
    if v1 != int(j[len(j)-2]) or v2 != int(j[len(j)-1]):
        print("CPF inválido")
        print(v1,v2)
        return False
    else:
        print("CPF Válido")
        print(v1,v2)
        return True