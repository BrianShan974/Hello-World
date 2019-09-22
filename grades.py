from random import shuffle

def grade(average):
	if average != 95:
		grades = [average + (i-6) for i in range(11)] + [average + 6]
		shuffle(grades)
		return grades
	else:
		grades = [average + (i-5) for i in range(11)] + [95]
		shuffle(grades)
		return grades

names = ["Daniel", "Harry", "Nico", "Jack", "James", "Brian", "Tim", "Lisa", "Cathy", "Julian", "Shirley", "Andy"]
lastNames = ["Chu", "Fang", "Jiang", "Jin", "Liu", "Shan", "Xing", "Xu", "Yang", "Ye", "Zeng", "Zhang"]
mathGrade = grade(90)
CSGrade = grade(95)
phyGrade = grade(88)

with open("AS_CS_opt2_gradebook.txt", "w") as f:
	for i in range(len(names)):
		line = str(names[i]) + " " + str(lastNames[i]) + " " + str(mathGrade[i]) + " " + str(CSGrade[i]) + " " + str(phyGrade[i])
		f.write(line + "\n")
	f.close()

