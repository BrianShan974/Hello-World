def balance(initialBalance, annualInterestRate, monthlyPayment, months):
    monthlyInterestRate = annualInterestRate / 12
    for month in range(months):
        initialBalance -= monthlyPayment
        updatedBalance = (1 + monthlyInterestRate) * initialBalance
    return updatedBalance

def payment(debt, months, annualInterestRate):
    cannot = True
    pay = 1
    while cannot:
        newDebt = debt
        if newDebt <= 0:
            cannot = False
            break
        else:
            for month in months:
                newDebt = balance(newDebt, annualInterestRate, pay * 10, 1)
            if newDebt > 0:
                pay += 1
    return pay