def MakeNewFile(FileName, NewFileName):
	with open(FileName) as f:
		lines = [x.strip() for x in f.readlines()]
		f.close()

	with open(NewFileName, "w") as NewFileName:
		for i in lines:
			f.write("00" + i)
		f.close()

	return NewFileName