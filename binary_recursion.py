def search(alist, item):
    try:
        pos = len(alist) // 2
        if alist[pos] == item:
            return True
        elif alist[pos] > item:
            return search(alist[:pos], item)
        else:
            return search(alist[pos + 1:], item)
    except IndexError:
        return False