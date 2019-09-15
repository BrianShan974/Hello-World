with open("qbdata.txt") as f:
	lines = [line.strip() for line in f.readlines()]
	f.close()

def takeScore(String):
	for i in range(1, len(String) + 1):
		if String[-i] == " ":
			return eval(String[1 - i:])

def takeName(String):
	for i in range(len(String)):
		if String[i] == " ":
			for a in range(len(String)):
				if String[i+1:][a] == " ":
					return String[:i + a]

nameList = []
scoreList = []

for line in lines:
	if takeScore(line) >= 60:
		scoreList.append(takeScore(line))
		nameList.append(takeName(line))

with open("processed.txt", "w") as f:
	for i in range(len(nameList)):
		f.write(f"{nameList[i]} has a rating of {scoreList[i]}" + "\n")
	f.close()