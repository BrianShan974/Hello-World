with open("AS_CS_opt2_gradebook.txt") as f:
	lines = f.readlines()
	f.close()

minPhysGrades = min([line.split()[-1].strip() for line in lines])

with open("AS_CS_opt2_gradebook.txt", "w") as f:
	for line in lines:
		if not line.split()[-1].strip() == minPhysGrades:
			f.write(line)
	f.close()