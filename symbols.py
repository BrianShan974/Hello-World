#DECLARE symbol : STRING
#DECLARE number, numberOfSymbols, numberOfSpaces : INTEGER

symbol = input("enter the symbol\n")
number = eval(input("enter the number\n"))
while number % 2 == 0:
	number = eval(input("enter the number\n"))
numberOfSpaces = int((number - 1) / 2)
numberOfSymbols = 1
while numberOfSymbols <= number:
	for i in range(1, numberOfSpaces + 1):
		print(" ", end = "")
	for i in range(1, numberOfSymbols + 1):
		print(symbol, end = "")
	print("")
	numberOfSpaces -= 1
	numberOfSymbols += 2