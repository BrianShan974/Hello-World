with open("AS_CS_opt2_gradebook.txt") as f:
	lines = f.readlines()
	f.close()

with open("AS_CS_opt2_gradebook.txt", "w") as f:
	for i in lines:
		if i.split()[1] != "Daniel":
			f.write(i)
		else:
			line = i.split()
			line[3] = line[3] * 1.1
			String = " "
			f.write(String.join(line))
	f.close()