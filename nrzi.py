from encoding import Encoding

import matplotlib.pyplot as plt
import numpy as np

class NRZI(Encoding):

    def __init__(self, bits:str):
        super().__init__(bits)
        self.code = self.encode()
        

    def encode(self) -> tuple:
        code = [1, 1]
        timestamp = [0]

        counter = 0
        states = (1, -1)
        state = 0

        for i in self.bits: #10110010

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
    
    
    def plot(self):
        
        fig, axs = plt.subplots(1)

        x_axis = self.code[1]
        y_axis = self.code[0]

        bit_code = [str(i) for i in self.bits]
        bit_code.insert(0, '')
        
        plt.xticks(np.arange(len(x_axis)), bit_code)
        plt.yticks([-1, 0, 1], ['-1', '', '1'])

        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()