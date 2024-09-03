def cor_da_casa(n):
    n.replace(" ", "")
    colum = 'abcdefgh'
    nums = '12345678'
    i = colum.find(n[0])
    j = nums.find(n[1])
    if (i+j)%2 == 0:
        return "Preto"
    else:
        return "Branco"

print(cor_da_casa("h8"))