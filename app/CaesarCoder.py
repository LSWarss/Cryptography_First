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
        for letter in inputStr.lower():
            outputStr = outputStr + self.strideDown(letter)
        return outputStr
    
    def strideUp(self, letter: str):
        """Encodes letter by given stride in the class"""
        if(letter.isspace()):
            return chr(ord(letter))
        if(ord(letter) < 97 or ord(letter) > 122):
            return chr(ord(letter))
        elif(ord(letter) + self.stride > 122):
            return chr(ord(letter) - 26 + self.stride)
        else:
            return chr(ord(letter) + self.stride)
    
    def strideDown(self, letter: str):
        """Decodes letter by given stride in the class"""
        if(letter.isspace()):
            return chr(ord(letter))
        elif(ord(letter) < 97 or ord(letter) > 122):
            return chr(ord(letter))
        elif(ord(letter) - self.stride < 97):
            return chr(ord(letter) + 26 - self.stride)
        else:
            return chr(ord(letter) - self.stride)
    