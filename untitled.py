def getInfo():
	alphabet = [chr(x) for x in range(65, 91)]
	numbers = [y for y in range(10)]
	lengthCheck = False
	letterCheck = False
	numberCheck = True
	while not letterCheck or not numberCheck or not lengthCheck:
		inputID = input("Please enter a valid ID:")
		if len(inputID) == 5:
			if inputID[0] in alphabet:
				letterCheck = True
			else:
				letterCheck = False
			for number in inputID[1:]:
				if number not in numberCheck:
					numberCheck = False
			lengthCheck = True
		else:
			lengthCheck = False
	inputName = input("Please enter the name:")
	return inputID + "*" + inputName

def topLevel():
	string = getInfo()
	if "A" <= string[0] <= "M":
		success = writeInfo(string, "File1.txt")
	else:
		success = writeInfo(string, "File2.txt")
	if not success:
		return 0
	if input("Continue? [Y/N]") in ["N", "n"]:
		return 0