def balance(initialBalance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12
    for month in range(12):
        initialBalance -= monthlyPaymentRate * initialBalance
        updatedBalance = (1 + monthlyInterestRate) * initialBalance
    return updatedBalance