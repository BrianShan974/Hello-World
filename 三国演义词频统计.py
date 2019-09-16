from copy import deepcopy

with open("三国演义.txt") as f:
	book = f.read()
	f.close()

string = deepcopy(book)
count = 0

for i in range(len(string) - 1):
	if string[i: i + 2] == "曹操":
		count += 1

print(count)
