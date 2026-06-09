def is_dif(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] == li[j]: return False
    return True

print(is_dif([1,5,7,9]))
print(is_dif([2,4,5,5,7,9]))