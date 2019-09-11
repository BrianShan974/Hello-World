UserID = input("enter the user ID")
UpperOK = False
DigitOK = True
Upper = UserID[:3]
Digits = UserID[3:]
if Upper = Upper.upper():
	UpperOK = True
for digit in Digits:
	if digit not in list(range(10)):
		DigitOK = False
		break
if UpperOK and DigitOK:
	print("OK")
else:
	print("NO")