digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
mAndDs = [str(i) for i in range(1, 17)]

m = eval(input("Enter the base you want to convert from:\n"))
n = eval(input("Enter the base you want to convert to:\n"))

number = input("Enter the number:\n")

output = ""

def index(List, item):
	for i in range(len(List)):
		if List[i] == item:
			return i

def denary(string, m):
	output = 0
	for i in range(len(string)):
		output += (m ** i) * index(digits, string[-i])
	return output

numberDenary = denary(number, m)

def log(base, number):
	i = 0
	while base ** i < number:
		i += 1
	if base ** i == number:
		return i
	else:
		return i - 1

digit = 1

if n == 10:
	print(numberDenary)
else:
	while digit != 0:
		theHighestPowerBelow = n ** log(n, numberDenary)
		digit = numberDenary // theHighestPowerBelow
		output = digits[digit] + output
		numberDenary %= theHighestPowerBelow
	print(output)
