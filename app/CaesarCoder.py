from CodingInterface import CodingInterface

class CaesarCoder(CodingInterface):
    """ Caesar code encoding and decoing class"""

    stride = 2

    def __init__(self, stride):
        self.stride = stride

    def encode(self, inputStr: str):
        """Encodes string"""
        outputStr = ""
        for letter in inputStr.lower():
            outputStr = outputStr + self.strideUp(letter)
        return outputStr

    def decode(self, inputStr: str):
        """Decodes string"""
        outputStr = ""
        for letter in inputStr:
            outputStr = outputStr + self.strideDown(letter)
        return outputStr
    
    def strideUp(self, letter: str):
        if(ord(letter) + self.stride > 122):
            return chr(ord(letter) - 26 + self.stride)
        elif(ord(letter) == 32):
            return " "
        else:
            return chr(ord(letter) + self.stride)
    
    def strideDown(self, letter: str):
        if(ord(letter) - self.stride < 97):
            return chr(ord(letter) + 26 - self.stride)
        elif(ord(letter) == 32):
            return " "
        else:
            return chr(ord(letter) - self.stride)
    