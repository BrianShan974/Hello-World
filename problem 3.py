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
for character in string:
    if ord(string[string.index(character)]) > ord(string[string.index(character) + 1]):
        list1.append(cut(string, string.index(character)))
        string = cut2(string, string.index(character))

print(find_longest(list1))