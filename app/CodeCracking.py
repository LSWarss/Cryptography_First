import requests
import random
import math

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

# Unigram model frequencies for letters A, B, ..., Z
english_freqs = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,
		0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

# Returns the cross-entropy of the fiven string with respect to the English unigram frequencies, which is a positive floating-point number
def getEntropy(inputStr: str):
	entropySum = 0
	ignored = 0
	for i in range(len(inputStr)):
		c = ord(inputStr[i])
  
		if( 65 <= c & c <= 90):
			entropySum += math.log(english_freqs[c - 65]); #Uppercase
		elif(97 <= c & c <= 122):
			entropySum += math.log(english_freqs[c - 97]); #Lowercase
		else: 
			ignored += 1
	return -entropySum / math.log(2) / (len(inputStr) - ignored)

# Returns the entropies when the given string is decrypted with all 26 possible shifts,
# where the result is an array of pairs (int shift, float enptroy) - e.g. [[0, 2.01], [1, 4.95], ..., [25, 3.73]].
def getAllEntropies(inputStr: str):
	result = []
	for i in range(26):
		coder = CaesarCoder(i)
		result.append([i, getEntropy(coder.decode(inputStr))])
	return result

def getTheLowestEntropy(inputStr: str):
	result = 5000
	resultStride = 0
	entropiesList = getAllEntropies(inputStr)
	for i in range(len(entropiesList)):
		if(entropiesList[i][1] < result):
			result = entropiesList[i][1]
			resultStride = entropiesList[i][0]
	coder = CaesarCoder(resultStride)
	print(f"Best guess 🤖: {result}")
	print(f"Decoded string: {coder.decode(inputStr)}")

