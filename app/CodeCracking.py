import requests
import random

from CaesarCoder import CaesarCoder


def set_up():
	randomStride = random.randint(1,20)
	coder = CaesarCoder(randomStride)
	response = requests.get('http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote', verify=False)
	return [coder, response.json()["content"], randomStride]


def maunal_caesar_cracking():
	dataSetup = set_up()
	encodedString = dataSetup[0].encode(dataSetup[1])
	decodedString = dataSetup[0].decode(encodedString)
	guessesNumber = 0
	codeCracked = False

	print("Encoded string ❌: " + encodedString)
	while codeCracked == False:
		print('Type in stride number for decoding: ')
		num = input("Stride: ")
		if(int(num) == dataSetup[2]):
			print("That's good stride. Decoded string is ✅: " + decodedString)
			print(f"You've cracked the code after {guessesNumber} guesses")
			codeCracked = True
		else:
			coder = CaesarCoder(int(num))
			print("That's not good stide. Try once more. Decoded string is ❌: " + coder.decode(encodedString))
			guessesNumber += 1

