def red(li):
    out = []
    out.append(li[0])
    for i in li:
        if i == out[-1]:
            continue
        out.append(i)
    return out

print(red([1,2,3,3]))