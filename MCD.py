def MCD(x):
    res = 1
    for i in range(1,10):
        if x%i==0:
            res = res+1
            continue
        else:
            res = res+1
            break
    return res



def mcd2(n,m):
    ind = 0
    try:
        primos = [2,3]
    
        r = 1
        for i in [2,3,4,5,6,7,8,9]:
            v = primos[ind]
            print(v)
            print('modulo',n%v)
            if n%v==0 and m%v==0:
                r=r*v
                n = n/v
                m = m/v
            else:
                ind = ind + 1
            print(n,m)
    except IndexError:
        print()
    return r


print(mcd2(48,60))
