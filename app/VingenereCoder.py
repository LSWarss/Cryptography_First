from CodingInterface import CodingInterface

class VingenereCoder(CodingInterface):

    def encode(self, inputStr: str):
        """Encodes string"""
        pass

    def decode(self, inputStr: str):
        """Decodes string"""
        pass
    
    def generateKey(self, inputStr: str, key):
        """ Generates key in loop until lenght of the key will be equal to input String"""
        key = list(key)
        if len(inputStr) == len(key):
            return key
        else: 
            for iteration in range(len(inputStr) - len(key)):
                key.append(key[iteration % len(key)])
        
        return "".join(key)