def sort(li):
    for i in range(len(li)):
        ind = 0
        for j in range(0, len(li) - i):
            if li[j] > li[ind]:
                ind = j
        temp = li[len(li) - i - 1]
        li[len(li) - i - 1] = li[ind]
        li[ind] = temp
    return li

print(sort([4,7,982,6,7,1,7,5,6,2,7,8,9,44]))