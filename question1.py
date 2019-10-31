ticketType = input("Enter the ticket type:\n")
while ticketType not in ['E', 'S']:
	ticketType = input("Enter the ticket type:\n")

if ticketType == 'E':
	baggageAllowance = 16
	chargeRate = 3.5
elif ticketType == 'S':
	baggageAllowance = 20
	chargeRate = 5.75
else:
	print("Go away")

if ticketType in ['E', 'S']:
	baggageWeight = eval(input("Enter the baggage weight:\n"))
	while (not (type(baggageWeight) == type(1) or type(baggageWeight) == type(0.5))) or baggageWeight < 0:
		baggageWeight = eval(input("Enter the baggage weight:\n"))
	excessWeight = baggageWeight - baggageAllowance
	if excessWeight > 0:
		charge = excessWeight * chargeRate
	else:
		charge = 0
	print("The charge is %.2f in total." % charge)