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
                          "AMI": [],
                          "Pseudoternary": []}
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
        self.codes["NRZI"] = self.nrzi()[0]
        self.codes["AMI"] = self.ami()
        self.codes["Pseudoternary"] = self.pseudoternary()

    def plot(self):
        # x = [i for i in range(len(self.codes["Bits"]))]
        
        # fig, axs = plt.subplots(len(self.codes),figsize=(10,12))
        # fig.tight_layout(pad=3.0)
        
        # x_ticks = np.arange(0, len(self.codes["Bits"]), 1)
        # y_ticks = np.array([-1,0,1])
        
        # for t, y, ax in zip(self.codes.keys(), self.codes.values(), axs):
        #     ax.set_xticks(x_ticks)
        #     ax.set_yticks(y_ticks)
        #     ax.grid(which="both")
        #     ax.set_ylim(-2,2)
        #     ax.set_title(t)
        #     ax.plot(x, y, c="red", drawstyle="steps-post")
        
        # plt.show()

        x_axis = []
        y_axis = []

        print("1) NRZI")
        print("2) HDB3")
        print("3) Manchester")
        print("4) 2BIQ")
        
        option = int(input("Qual codificação você gostaria de usar? R:"))

        if option == 1:
            x_axis = self.nrzi()[1]
            y_axis = self.codes["NRZI"]

        elif option == 4:
            x_axis = [i for i in range(len(self.codes["Bits"]))]
            y_axis = self.codes["AMI"]

        plt.plot(x_axis, y_axis)
        plt.show()
        

# bits = Encoding("01001100011")
bits = Encoding("10110010")
bits.encode()
print("Bits:", bits.get_bits())
print("NRZI:", bits.get_code("NRZI"))
print("AMIM:", bits.get_code("AMI"))
print("PSTM:", bits.get_code("Pseudoternary"))
bits.plot()