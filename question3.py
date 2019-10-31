dailyHoursWorked = [5, 10, 10]
productionData = [[10, 20, 9], [11, 16, 11], [10, 24, 13], [14, 20, 17]]

workerTotal = []

for workerNum in range(3):
	workerTotal.append(0)

for workerNum in range(3):
	for dayNum in range(4):
		workerTotal[workerNum] = workerTotal[workerNum] + productionData[dayNum][workerNum]

for workerNum in range(3):
	workerAverage = workerTotal[workerNum] / (4 * dailyHoursWorked[workerNum])
	if workerAverage < 2:
		print("Investigate", workerNum + 1)