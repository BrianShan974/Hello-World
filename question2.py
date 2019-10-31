pCode = []
pDescription = []
pRetailPrice = []
i = 1

with open("PRODUCTS.txt") as f:
	try:
		while i <= 1000:
			pCode.append(f.readline())
			pDescription.append(f.readline())
			pRetailPrice.append(f.readline())
			i += 1
		f.close()
	except:
		f.close()

print("Product file contents written to arrays")

def productCodeSearch(searchCode):
	for i in range(len(pCode)):
		if pCode[i] == searchCode:
			return i
	return -1

def split(string):
	if " " not in string:
		return string
	else:
		output = []
		for i in string:
			if i == " ":
				output.append(string[:i])
		return output + split(string[i:])

i = 1

with open("PRODUCTS2.txt") as f:
	try:
		while i <= 1000:
			line = split(f.readline())
			pCode.append(line[0])
			pDescription.append(line[1])
			pRetailPrice.append(line[2])
		f.close()
	except:
		f.close()