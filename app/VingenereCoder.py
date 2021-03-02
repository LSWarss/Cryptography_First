from CodingInterface import CodingInterface
import re

class VingenereCoder(CodingInterface):

    keyword = "uekatowice"

    def __init__(self, keyword):
        self.table = self.generateTable()
        self.keyword = keyword

    def encode(self, inputStr: str):
        """Encodes input string with the help of the key"""
        text = self.process_plaintext(inputStr)
        keywordrepeated = self.get_keyword_repeated(self.keyword, len(text))
        ciphertext = []

        for index, letter in enumerate(text):

            textIndex = ord(letter.upper()) - 65
            keywordindex = ord(keywordrepeated[index]) - 65

            encipheredletter = self.table[keywordindex][textIndex]

            ciphertext.append(encipheredletter)

        return "".join(ciphertext)

    def decode(self, inputStr: str):
        """Decodes input string with the help of the keyword"""

        keywordrepeated = self.get_keyword_repeated(self.keyword, len(inputStr))
        decipheredtext = []

        for index, letter in enumerate(inputStr):

            keywordindex = ord(keywordrepeated[index]) - 65

            decipheredletter = chr(self.table[keywordindex].index(letter) + 65)

            decipheredtext.append(decipheredletter)

        return "".join(decipheredtext)

    
    def generateTable(self):
        
        table = []
        for r in range(0,26):
            offset = 0
            row = []

            for c in range(0,26):
                row.append(chr(r + 65 + offset))
                offset += 1
                if offset > (25 - r):
                    offset = offset - 26
            table.append(row)
        return table

    def process_plaintext(self, plaintext):
        plaintext = plaintext.upper()
        plaintext = re.sub("[^A-Z]", "", plaintext)

        return plaintext

    def get_keyword_repeated(self, keyword, length):

        keyword = keyword.upper()
        keywordrepeated = []
        keywordlength = len(keyword)
        keywordindex = 0

        for i in range(0, length):
            keywordrepeated.append(keyword[keywordindex])
            keywordindex += 1
            if keywordindex > keywordlength - 1:
                keywordindex = 0

        return "".join(keywordrepeated)