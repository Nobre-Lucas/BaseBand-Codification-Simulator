import matplotlib.pyplot as plt
import numpy as np


class Encoding:

    def __init__(self, bits):
        self.bits = bits
        self.codes = {"NRZI": [],
                      "HDB3": [],
                      "Manchester": [],
                      "AMI": [],
                      "Pseudoternary": []}

    def get_bits(self):
        return self.bits

    def get_code(self, scheme: str) -> list:
        return self.codes[scheme]

    def ami(self) -> list:
        code = []

        level = True

        for bit in self.bits:
            if bit == "0":
                code.append(0)
            else:
                if level is True:
                    code.append(1)
                else:
                    code.append(-1)
                level = not level

        return code

    def pseudoternary(self) -> list:
        code = []
        
        level = True
        
        for bit in self.bits:
            if bit == "0":
                if level is True:
                    code.append(1)
                else:
                    code.append(-1)
                level = not level
            else:
                code.append(0)
        
        return code
    
    def encode(self):
        self.codes["AMI"] = self.ami()
        self.codes["Pseudoternary"] = self.pseudoternary()

    def plot(self):
        x = [i for i in range(len(self.bits))]
        
        fig, axs = plt.subplots(3,figsize=(10,10))
        fig.tight_layout(pad=3.0)
        
        major_ticks = np.arange(0, len(self.bits), 1)
        
        for y, ax in zip(self.codes.values(), fig.axes):
            if len(y) > 0:
                ax.set_xticks(major_ticks)
                ax.set_yticks(major_ticks)
                ax.grid(which='both')
                
                ax.plot(x,y,color='red',drawstyle="steps-post")
                ax.set_title("AMI")
        
        plt.show()
        

bits = Encoding("01001100011")
bits.encode()
print(bits.get_bits())
print(bits.get_code("AMI"))
print(bits.get_code("Pseudoternary"))
bits.plot()