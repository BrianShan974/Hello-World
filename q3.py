#a
Tally = ["" for i in range(5)]

#b
Choice = int(input("choice"))
while Choice != 0:
	Tally[Choice] += 1
	Choice = int(input("choice"))
for x in Tally:
	print(x)

#c
Title = ["reading books","playing computer games","sport","programming","watching TV"]
for i in range(5):
	print(Title[i])
	print(Tally[i])

#d
with open("survey.txt", "w") as f:
	for i in range(5):
		f.write(Title[i] + "\n")
		f.write(Title[i] + "\n")
	f.close()

#e
with open("survey.txt") as f:
	for i in range(5):
		Title.append(f.readline())
		Tally.append(f.readline())
	f.close()