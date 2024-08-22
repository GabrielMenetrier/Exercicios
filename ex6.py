def mult_lent(x,y):
    z = 0
    if x > 0 or y > 0:
        for i in range(y):
            z = z + x
        return z
    elif x == 0 or y ==0:
        return 0
    elif x < 0 & y < 0:
        return mult_lent(-x,-y)
    elif x<0:
        return -mult_lent(-x,y)
    else:
        return -mult_lent(x,-y)

print (mult_lent(-4,5))
