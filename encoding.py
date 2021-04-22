import matplotlib.pyplot as plt
import numpy as np


class Encoding:

    def __init__(self, bits):

        valid = True
        for i in bits:
            if (i != '0') and (i != '1'):
                valid = False

        if valid == True:
            self.codes = {"Bits": [int(bit) for bit in bits],
                          "NRZI": [],
                        # "HDB3": [],
                        # "Manchester": [],
                          "2B1Q": []}
        else:
            raise ValueError ("Os dados só podem possuir bits 0 ou 1")

    def get_bits(self):
        return self.codes["Bits"]

    def get_code(self, scheme: str) -> list:
        return self.codes[scheme]

    def nrzi(self) -> list:
        code = [1, 1]
        timestamp = [0]

        counter = 0
        states = (1, -1)
        state = 0

        for i in self.codes["Bits"]: #10110010

            counter += 1

            if i == 1:
                state = 1 if (state == 0) else 0
                code.append(states[state])
                code.append(states[state])

                timestamp.append(counter)
                timestamp.append(counter)

            elif i == 0:
                code.append(states[state])
                timestamp.append(counter)

        code.pop()

        return code, timestamp


    def tboq(self):
        pass
    
    def encode(self):
        self.codes["NRZI"] = self.nrzi()[0]
        self.codes["2B1Q"] = self.tboq()

    def plot(self, scheme: str):
        
        x_axis = []
        y_axis = []

        if scheme == "NRZI":
            x_axis = self.nrzi()[1]
            y_axis = self.codes["NRZI"]
        
        else:
            raise ValueError("Available schemes: NRZI, HDB3, Manchester, 2B1Q")

        plt.plot(x_axis, y_axis)
        plt.show()
        

# bits = Encoding("01001100011")
bits = Encoding("10110010")
bits.encode()
print("Bits:", bits.get_bits())
print("NRZI:", bits.get_code("NRZI"))
print("2B1Q:", bits.get_code("2Q1Q"))
bits.plot()