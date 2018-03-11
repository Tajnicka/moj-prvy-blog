print('Hello, Django girls!')

#def hi(meno):
#	if meno == "Tana":
#		print("Ahoj Tana")
#	elif meno == "Matej": 
#		print("Ahoj Matej")
#	else:
#		print("Ahoj neznama")
#hi("Mima")


def hi(meno):
	print("Ahoj " + meno + "!")

dievcata = ["Tana","Mima","Zuzka","Alex","Ty"]
for meno in dievcata:
		hi(meno)
		print("Dalsie dievca")


