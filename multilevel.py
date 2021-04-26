from encoding import Encoding

import matplotlib.pyplot as plt
import numpy as np

class Multilevel(Encoding):

    def __init__(self, bits:str):
        super().__init__(bits)
        self.code = self.encode()
        

    def encode(self) -> tuple:
        translate_table = {"00": (+1, -1),
                           "01": (+3, -3),
                           "10": (-1, +1),
                           "11": (-3, +3)}

        o_bits = [0] if (len(self.bits) % 2 != 0) else []
        o_bits += [str(i) for i in self.bits]

        dibits = [[o_bits[i], o_bits[i+1]] for i in range(0, len(o_bits), 2)]

        code = []
        timestamp = [0]

        previous_level = True
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
    
    def plot(self):
        
        fig, axs = plt.subplots(1)

        x_axis = self.code[1]
        y_axis = self.code[0]
        
        plt.ylim(-3.1, 3.1)
        
        o_bits = [0] if (len(self.bits) % 2 != 0) else []
        o_bits += [str(i) for i in self.bits]
        
        bit_code = ["".join([o_bits[i], o_bits[i+1]]) for i in range(0, len(o_bits), 2)]
        bit_code = ['' if i % 2 == 0 else bit_code[i//2] for i in range(len(bit_code)*2)] + ['']
                                
        plt.xticks(np.arange(len(x_axis))/2, bit_code)
        plt.yticks([-3, -1, 0, 1, 3], ['-3', '-1', '', '1', '3'])
        
        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()