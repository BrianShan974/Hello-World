def average(List):
	outList = []
	for i in List:
		outList.append(eval(i))
	average = sum(outList) / len(outList)
	return average

with open("AS_CS_opt2_gradebook.txt") as f:
	fileLines = f.readlines()
	scores = [line.strip().split()[-3:] for line in fileLines]
	f.close()

with open("AS_CS_opt2_gradebook.txt", "w") as f:
	for i in range(12):
		line = fileLines[i].strip() + " " + str(round(average(scores[i]), 2)) + "\n"
		f.write(line)
	f.close()