def bobcheck(string):
    count = 0
    length = len(string)
    for start in range(length - 2):
        if string[start: start + 3] == "bob":
            count += 1
    return count

print(bobcheck(input("Please enter the string:")))