import matplotlib.pyplot as plt
import numpy as np


class Encoding:

    def __init__(self, bits):
        self.codes = {"Bits": [int(bit) for bit in bits],
                      #   "NRZI": [],
                      # "HDB3": [],
                      # "Manchester": [],
                      "AMI": [],
                      "Pseudoternary": []}

    def get_bits(self):
        return self.codes["Bits"]

    def get_code(self, scheme: str) -> list:
        return self.codes[scheme]

    def ami(self) -> list:
        code = []

        level = True

        for bit in self.codes["Bits"]:
            if bit == 0:
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
        
        for bit in self.codes["Bits"]:
            if bit == 0:
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
        x = [i for i in range(len(self.codes["Bits"]))]
        
        fig, axs = plt.subplots(len(self.codes),figsize=(10,12))
        fig.tight_layout(pad=3.0)
        
        x_ticks = np.arange(0, len(self.codes["Bits"]), 1)
        y_ticks = np.array([-1,0,1])
        
        for t, y, ax in zip(self.codes.keys(), self.codes.values(), axs):
            ax.set_xticks(x_ticks)
            ax.set_yticks(y_ticks)
            ax.grid(which="both")
            ax.set_ylim(-2,2)
            ax.set_title(t)
            ax.plot(x, y, c="red", drawstyle="steps-post")
        
        plt.show()
        

bits = Encoding("01001100011")
bits.encode()
print("Bits:", bits.get_bits())
print("AMIM:", bits.get_code("AMI"))
print("PSTM:", bits.get_code("Pseudoternary"))
bits.plot()