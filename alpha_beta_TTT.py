import math

def ab(d, i, maxp, v, a, b):
    if d == 0: return v[i]
    for j in (0,1):
        val = ab(d-1, i*2+j, not maxp, v, a, b)
        if maxp:
            a = max(a, val)
        else:
            b = min(b, val)
        if a >= b: break
    return a if maxp else b

vals = [3,5,6,9,1,2,0,-1]
print("Optimal value:", ab(3, 0, True, vals, -math.inf, math.inf))
