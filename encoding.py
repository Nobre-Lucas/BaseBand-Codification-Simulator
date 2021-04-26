from abc import abstractmethod

class Encoding:
    def __init__(self, bits:str):
        valid = True
        for i in bits:
            if (i != '0') and (i != '1'):
                valid = False

        if valid == True:
            self.bits = [int(bit) for bit in bits]
            self.code = ()
        else:
            raise ValueError ("Available entry: characters 1 or 0")
    
    def get_bits(self) -> list:
        return self.bits
    
    def get_code(self) -> list:
        return self.code[0]
    
    @abstractmethod
    def encode(self):
        pass
    
    @abstractmethod
    def plot(self):
        pass