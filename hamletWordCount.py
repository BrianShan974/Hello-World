with open("hamlet.txt") as f:
	words = [word.strip().lower() for word in f.read().split()]
	f.close()

for char in (",", ".", ":", ";", "\n", ">"):
	words = [word.strip(char) for word in words]

output = []
noRepetition = set(words)

for word in noRepetition:
	output.append(str(words.count(word)) + word)

output.sort()
output.reverse()

print(output[:20])