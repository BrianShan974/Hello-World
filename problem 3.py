letters = [chr(x) for x in range(ord("a"), ord("z") + 1)]

def cut(string, index):
    return string[: index + 1]

def cut2(string, index):
    return string[index + 1: ]

def find_longest(a_list):
    lengths = [len(x) for x in a_list]
    for element in a_list:
        if len(element) == max(lengths):
            return element

string = str(input("Please enter the string:"))
list1 = []
i = 1
while i < len(string):
    if i > 0:
        if ord(string[i]) < ord(string[i - 1]):
            list1.append(cut(string, i - 1))
            string = cut2(string, i - 1)
            i = 0
        else:
            i += 1
    else:
        i += 1

print(find_longest(list1))
