number = input("Please enter the number\n")

with open("qbdataNew2.txt") as f:
	lines = f.readlines()
	f.close()

for line in lines:
	if line[:4] == number:
		print(line)