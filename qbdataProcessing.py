with open("qbdata.txt") as f:
    lines = f.readlines()
    f.close()

Character = input("Please enter the character for substitution\n")

with open("qbdataNew.txt", "w") as f:
    for line in lines:
        for i in range(len(line)):
            if line[i] != " ":
                f.write(line[i])
            else:
                f.write(Character)
    f.close()
