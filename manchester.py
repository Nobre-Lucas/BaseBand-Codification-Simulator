from encoding import Encoding

import matplotlib.pyplot as plt
import numpy as np

class Manchester(Encoding):

    def __init__(self, bits:str):
        super().__init__(bits)
        self.code = self.encode()
        

    def encode(self) -> tuple:
        code = [1 if self.bits[0] == 0 else 0]
        timestamp = []
        
        counter = 0
        states = (1, 0)
        counter2 = 0
        
        for i in self.bits:
          if i == 1:
            code.append(states[1])
            timestamp.append(counter)
            counter += 0.5
             
            code.append(states[0])
            timestamp.append(counter)
        
            code.append(states[0])
            timestamp.append(counter)
            counter += 0.5
        
          elif i == 0:
            code.append(states[0])
            timestamp.append(counter)  
            counter += 0.5
        
            code.append(states[1])
            timestamp.append(counter)
        
            code.append(states[1])
            timestamp.append(counter)
            counter += 0.5
        
              
          if counter2 < len(self.bits)-1:
            if (self.bits[counter2+1] == 0 and self.bits[counter2] == 0):
              code.append(states[0])
              timestamp.append(counter)
        
            if (self.bits[counter2+1] == 1 and self.bits[counter2] == 1):
              code.append(states[1])
              timestamp.append(counter)
          counter2 += 1
        
        if (self.bits[-1] == 1):
          
          code.append(states[0])
          timestamp.append(counter)  
        
        if (self.bits[-1] == 0):
          
          code.append(states[1])
          timestamp.append(counter)
        
        code.pop() 
        
        return code, timestamp 
    
    def plot(self):
        
        fig, axs = plt.subplots(1)

        x_axis = self.code[1]
        y_axis = self.code[0]

        bit_code = []
        for i in self.bits:
            bit_code.append('')
            bit_code.append(i)

        plt.yticks([0, 1], [ '0', '1'])
        plt.xticks(np.arange(0, len(x_axis), 0.5), bit_code)

        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()