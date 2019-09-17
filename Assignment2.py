import sys


alphabetDict = {
	"a" : 1,
	"b" : 2,
	"c" : 3,
	"d" : 4,
	"e" : 5,
	"f" : 6,
	"g" : 7,
	"h" : 8,
	"i" : 9,
	"j" : 10,
	"k" : 11,
	"l" : 12,
	"m" : 13,
	"n" : 14,
	"o" : 15,
	"p" : 16,
	"q" : 17,
	"r" : 18,
	"s" : 19,
	"t" : 20,
	"u" : 21,
	"v" : 22,
	"w" : 23,
	"x" : 24,
	"y" : 25,
	"z" : 26,
	"z" : 0,
	" " : 27
}

numberDict = {
	0 : "z",
	1 : "a",
	2 : "b", 
	3 : "c",
	4 : "d",
	5 : "e",
	6 : "f",
	7 : "g",
	8 : "h",
	9 : "i",
	10 : "j",
	11 : "k",
	12 : "l",
	13 : "m",
	14 : "n",
	15 : "o",
	16 : "p",
	17 : "q",
	18 : "r",
	19 : "s",
	20 : "t",
	21 : "u",
	22 : "v",
	23 : "w",
	24 : "x",
	25 : "y",
	26 : "z",
	27 : " "
}



encode = sys.argv[1]
keyword = sys.argv[2].replace(" ", "")

print(list(alphabetDict.values()))

while(True):
	codeWord = input()

	encodingWord = ""

	numberCode = []
	numberKey = []

	postCipher = []
	output = ""
	
	capitalization = []

	i = 0
	for x in codeWord:
		keywordLetter = keyword[i % len(keyword)]
		encodingWord += keywordLetter
		if x not in alphabetDict:
			postCipher.append(str(x))
			capitalization.append(False)
		else:
			let0 = alphabetDict[x.lower()]
			let1 = alphabetDict[keywordLetter.lower()]	
			numberCode.append(let0)
			numberKey.append(let1)
			if(x == " "):
				postCipher.append(27)
			elif(encode == "-e"):
				postCipher.append(((let0 + let1) % 26) - 1)
			elif(encode == "-d"):
				postCipher.append(((let0 - let1) % 26) + 1)
			else:
				print("The first argument should be -e or -d.")
				exit()
			if(not x.islower() and x != " "):
				capitalization.append(True)
			else:
				capitalization.append(False)
		i += 1

	i = 0
	for x in postCipher:
		if(isinstance(x, str)):
			outputLetter = x
			output += outputLetter
		else:
			#outputLetter = list(alphabetDict.keys())[list(alphabetDict.values()).index(x)]
			outputLetter = numberDict[x]
			if(capitalization[i]):
				outputLetter = outputLetter.upper()
			output += outputLetter
		i += 1

	print(output)


print("Exiting...")