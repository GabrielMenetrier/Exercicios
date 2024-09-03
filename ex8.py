def min_burro(n):
    for i in range (len(n)):
        b = False
        for e in range (len(n)):
            if n[i] > n[e]:
                b = True
            if not b:
                return n[i]

def min_inteligente(n):
    if len(n) == 0:
        return None
    j = n[0]
    for i in range(len(n)):
        if j > n[i]:
            j = n[i]
    return j

def p_cartesiano(n,m):
    nxm = []
    if len(n) != len(m):
        print(len(n),len(m))
    else:
        for i in range(len(n)):
            nxm.append((n[i]*m[i]))
        return nxm

def get_sum(n):
    a = 0
    if len(n) == 0:
        return None
    else:
        for i in range (len(n)):
            a += n[i]
        return a

def get (n,m):
    for i in range (len(n)):
        if n[i][0] == m:
            return n[i][1]
        else:
            return None

def filtro(f,n):
    xs = []
    for i in range (len(n)):
        if f(n[i]):
            xs.append(n[i])
    return xs

def ordenar_burro(n):
    xs = []
    j = n
    for i in range (len(n)):
        mini = min_inteligente(j)
        xs.append(mini)
        j.remove(mini)
    return xs

Lista0 = [1,2,5,3,6,4,7,8,56]
Lista1 = [1,2,3,5,6,4,8,6,7]
Lista2 = [("A1", 72), ("A2", 45), ("AS", 84)]

print(ordenar_burro(Lista1))
## print(filtro(lambda x: x % 2 == 0, [1,2,3,4]))