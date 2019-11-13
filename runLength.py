string = "AAAAAAABBBBBBBBBBBBBCCC"

preOutput = string[0]
counter = 0
i = 1
counterList = []
for character in string:
	if character != preOutput[i - 1]:
		preOutput += character
		i += 1
		counterList.append(counter)
		counter = 1
	else:
		counter += 1
counterList.append(counter)

output = ""

print(counterList)
for i in range(len(preOutput)):
	output += str(counterList[i])
	output += preOutput[i]

print(output)