def vowelcheck(string):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for character in string:
        if character in vowels:
            count += 1
    return count

print(vowelcheck(input("Please enter the string:")))