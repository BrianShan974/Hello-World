with open("qbdataNew.txt") as f:
    lines = f.readlines()
    f.close()

name = input("Please enter the name\n")

with open("qbdataNew2.txt", "w") as f:
	count = 0
    for line in range(len(lines)):
        if lines[line][:len(name)] == name or lines[line] == "\n":
        	pass
        else:
            f.write("%.4d " % count + lines[line])
            count += 1
    f.close()
