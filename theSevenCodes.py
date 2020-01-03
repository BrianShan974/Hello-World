def AddNewScores():
	file = open("ScoreDetails.txt", "a")
	while True:
		date = input("Please enter the date of the scores:\n")
		membershipNumber = input("Please enter the membership number:\n")
		if membershipNumber == "":
			return
		score = input("Please enter the score:\n")
		while score > 99 or score < 50:
			score = input("Please enter the score:\n")
		line = membershipNumber + date + score
		file.write(line + "\n")

def Lighten():
	rows = len(Picture)
	columns = len(Picture[0])
	burnt = False
	for i in range(rows):
		for j in range(columns):
			Picture[i][j] *= 1.1
			if Picture[i][j] >= 255:
				Picture[i][j] = 255
				burnt = True
	return burnt

def ProcessMarks(Mark):
	index = 0
	highest = 0
	partialSum = 0
	for i in range(20):
		partialSum += Mark[i]
		if Mark[i] > highest:
			highest = Mark[i]
	average = partialSum / 20
	print("The average mark is %.3f and the highest mark is %d.")
	for i in range(20):
		if Mark[i] == highest:
			return i

def StringClean(string_):
	outString = ""
	for i in range(len(string_)):
		nextChar = string_[i]
		nextChar = nextChar.lower()
		if "a" <= nextChar <= "z":
			outString += nextChar
	return outString

def CheckSensor():
	sensorID = int(input("Please enter the sensor ID:\n"))
	while not 1 <= sensorID <= 10:
		sensorID = int(input("Please enter the sensor ID:\n"))
	temperature = GetTemp(sensorID)
	if temperature < LowTemp:
		print("Cold")
	elif temperature > HighTemp:
		Alarm()
	else:
		print("Normal")

def ValidatePassword(password):
	valid = True
	lowercaseCount = 0
	uppercaseCount = 0
	numberCount = 0
	for character in password:
		if "a" <= character <= "z":
			lowercaseCount += 1
		elif "A" <= character <= "Z":
			uppercaseCount += 1
		elif character in [str(x) for x in range(10)]:
			numberCount += 1
		else:
			return False
	if (lowercaseCount < 2) or (uppercaseCount < 2) or (numberCount < 3):
		valid = False
	return valid

def SearchFile():
	for event in range(len(LoginEvents)):
		if LoginEvents[event] != ["", ""]:
			index = event + 1
			break
	filelines = [line[:-1] for line in open("LoginFile.txt").readlines()]
	userID = input("Please enter the userID:\n")
	for line in filelines:
		if userID == line[:5]:
			line[index] = [line[5:9], line[9:]]