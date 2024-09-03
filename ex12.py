def vogais(palavra):
    v = 0
    c = 0

    for i in range(len(palavra)):
        if palavra[i] in ('a','e','i','o','u'):
            v += 1
        elif palavra[i].isalpha():
            c+= 1
    return v,c

print(vogais("91378463178946!(*&@#¨*!@&#!@&*aebghHGA"))