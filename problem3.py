def balance(initialBalance, annualInterestRate, monthlyPayment, months):
    monthlyInterestRate = annualInterestRate / 12
    for month in range(months):
        initialBalance -= monthlyPayment
        updatedBalance = (1 + monthlyInterestRate) * initialBalance
    return updatedBalance

def bisection(lowerBound, upperBound):
    return 0.5 * (lowerBound + upperBound)

def payment(debt, months, annualInterestRate):
    cannot = True
    lowerBound = 0
    upperBound = debt
    pay = 1
    while cannot:
        newDebt = debt
        if newDebt <= 0:
            cannot = False
            break
        else:
            for month in months:
                newDebt = balance(newDebt, annualInterestRate, pay, 1)
            if newDebt > 0:
                pay = bisection(lowerBound, upperBound)
                lowerBound = pay
                upperBound = bisection(pay, upperBound)
            elif newDebt <= -0.001:
                pay = bisection(lowerBound, upperBound)
                lowerBound = bisection(0, pay)
                upperBound = pay
    return pay

