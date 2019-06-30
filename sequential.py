def search(alist, item, sorted = False):
    if not sorted:
        for pos in range(len(alist)):
            if alist[pos] == item:
                return pos
    else:
        for pos in range(len(alist)):
            if alist[pos] == item:
                return pos
            elif alist[pos] > item:
                break