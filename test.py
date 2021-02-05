def mystery(alist):
    for index in range(1, len(alist)):
        pos = index
        current = alist[index]
        while pos > 0 and alist[pos-1] > current:
            alist[pos] = alist[pos-1]
            pos = pos - 1
        alist[pos] = current

    return alist


a = [1, 5, 4, 3, 2]
b = [5, 4, 3, 2, 1] 
print(mystery(b))