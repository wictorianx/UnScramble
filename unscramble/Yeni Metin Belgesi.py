theBool = True
a = 1
wordsFile = open('myfile.txt', 'r')
words = wordsFile.read().splitlines()
while(theBool):
	scrambledWord = input()
	while(theBool):
		wordsList = []
		scrambledList = []
		if a <= len(words):
			print(scrambledWord)
			word = words[a-1].lower()
			print(word)
		a += 1
		if len(scrambledWord) == len(word):
			for i in range(len(word)):
				wordsList.append(word[i])
				scrambledList.append(scrambledWord[i])
				wordsList.sort()
				scrambledList.sort()
				if wordsList != scrambledList:
					break
			if wordsList == scrambledList:
				theBool = False