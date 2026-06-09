p = 0
n = 1
while p < 50:
    print(p, end=" ")
    t = n
    n = p + n
    p = t
