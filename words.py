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

with open("/Users/brianshan/Desktop/School Sh*t/Computer Science/其他/课堂/vocab.txt") as vocab:
    words = [word.strip() for word in vocab.readlines()]
    vocab.close()

with open("/Users/brianshan/Desktop/School Sh*t/Computer Science/其他/课堂/alice_in_wonderland.txt") as book:
    booklines = book.readlines()
    book.close()

booklist = []
for line in booklines:
    booklist += line.split()
booklist1 = [word.lower().strip() for word in booklist]

count = 0
for element in booklist1:
    if search(words, element):
        count += 1

print(count / len(booklist1))