import matplotlib.pyplot as plt
import numpy as np

class Encoding:

    def __init__(self, bits: str):

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
            raise ValueError ("Available entry: characters 1 or 0")

    def get_bits(self) -> list:
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


    def tboq(self) -> list:
        translate_table = {"00": (+1, -1),
                           "01": (+3, -3),
                           "10": (-1, +1),
                           "11": (-3, +3)}

        o_bits = [0] if (len(self.codes["Bits"]) % 2 != 0) else []
        o_bits += [str(i) for i in self.codes["Bits"]]

        dibits = [[o_bits[i], o_bits[i+1]] for i in range(0, len(o_bits), 2)]

        code = []
        timestamp = [0]

        previous_level = True # T if (previous > 0 or initial) else F
        counter = 0

        for dibit in dibits:

            counter += 1

            if previous_level is True:
                current_level = translate_table["".join(dibit)][0]
            else:
                current_level = translate_table["".join(dibit)][1]

            code.append(current_level)
            code.append(current_level)

            timestamp.append(counter)
            timestamp.append(counter)

            previous_level = True if current_level > 0 else False

        timestamp.pop()

        return code, timestamp


    def encode(self):
        self.codes["NRZI"] = self.nrzi()[0]
        self.codes["2B1Q"] = self.tboq()[0]


    def plot(self, scheme: str):
        
        fig, axs = plt.subplots(1)

        x_axis = []
        y_axis = []

        if scheme == "NRZI":
            x_axis = self.nrzi()[1]
            y_axis = self.codes["NRZI"]

            bit_code = [str(i) for i in self.codes["Bits"]]
            bit_code.insert(0, '')
            plt.yticks([-1, 0, 1], ['-1', '', '1'])

        elif scheme == "2B1Q":
            x_axis = self.tboq()[1]
            y_axis = self.codes["2B1Q"]
            
            plt.ylim(-3.1, 3.1)
            
            
            o_bits = [0] if (len(self.codes["Bits"]) % 2 != 0) else []
            o_bits += [str(i) for i in self.codes["Bits"]]

            bit_code = ["".join([o_bits[i], o_bits[i+1]]) for i in range(0, len(o_bits), 2)]
            bit_code = ['' if i % 2 == 0 else bit_code[i//2] for i in range(len(bit_code)*2)] + ['']
                                    
            plt.xticks(np.arange(len(x_axis))/2, bit_code)
            plt.yticks([-3, -1, 0, 1, 3], ['-3', '-1', '', '1', '3'])
            
        else:
            raise ValueError("Available schemes: NRZI, HDB3, Manchester, 2B1Q")

        
        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()


bits = Encoding("101100100111")
bits.encode()
print("Bits:", bits.get_bits())
print("NRZI:", bits.get_code("NRZI"))
print("2B1Q:", bits.get_code("2B1Q"))

bits.plot("2B1Q")
