with open("AS_CS_opt2_gradebook.txt") as f:
	lines = []
	fileLines = f.readlines()
	for i in range(1, 13):
		lines.append(f"{i} " + fileLines[i - 1])
	f.close()

with open("AS_CS_opt2_gradebook.txt", "w") as f:
	for line in lines:
		f.write(line)
	f.close()