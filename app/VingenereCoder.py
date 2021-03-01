from CodingInterface import CodingInterface

class VingenereCoder(CodingInterface):

    key = "uekatowice"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    def __init__(self, key):
        self.key = key

    def encode(self, inputStr: str):
        """Encodes input string with the help of the key"""
        encrypted = ""
        split_message = [
            inputStr[i : i + len(self.key)] for i in range(0, len(inputStr), len(self.key))]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (self.letter_to_index[letter] + self.letter_to_index[self.key[i]]) % len(self.alphabet)
                encrypted += self.index_to_letter[number]
                i += 1

        return encrypted

    def decode(self, inputStr: str):
        """Decodes input string with the help of the key"""
        decrypted = ""
        split_encrypted = [
            inputStr[i : i + len(self.key)] for i in range(0, len(inputStr), len(self.key))]
            
        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (self.letter_to_index[letter] - self.letter_to_index[self.key[i]]) % len(self.alphabet)
                decrypted += self.index_to_letter[number]
                i += 1

        return decrypted
    
    def generateKey(self, inputStr: str, key):
        """ Generates key in loop until lenght of the key will be equal to input String"""
        key = list(key)
        if len(inputStr) == len(key):
            return key
        else: 
            for iteration in range(len(inputStr) - len(key)):
                key.append(key[iteration % len(key)])
        
        return "".join(key)