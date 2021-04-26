from encoding import Encoding

import matplotlib.pyplot as plt
import numpy as np

class HDB3(Encoding):
    def __init__(self, bits:str):
        super().__init__(bits)
        self.code = self.encode()
        

    def encode(self) -> tuple:
        consecutive_zero_counter = 0
        counter = 0
        informations_number = 0
        VIOLATION_NUMBER = 3
        timestamp = []
        code = []
        converted_data = []
        converted_data_y = []
        information_polarity = True
        violation_polarity = True

        for i in range(len(self.bits)):
            posterior_sublist = self.bits[i+1:i+4]

            if self.bits[i] == 1:
                converted_data.append(1)
                consecutive_zero_counter = 0
                if information_polarity == True:
                    timestamp.append(counter)
                    code.append(1)
                    counter += 0.5
                    timestamp.append(counter)
                    code.append(1)
                    timestamp.append(counter)
                    code.append(0)
                    counter += 0.5
                    timestamp.append(counter)
                    code.append(0)
                    converted_data_y.append(1)
                elif information_polarity == False:
                    timestamp.append(counter)
                    code.append(-1)
                    counter += 0.5
                    timestamp.append(counter)
                    code.append(-1)
                    timestamp.append(counter)
                    code.append(0)
                    counter += 0.5
                    timestamp.append(counter)
                    code.append(0)
                    converted_data_y.append(-1)
                informations_number += 1
                information_polarity = not information_polarity

            elif self.bits[i] == 0:
                converted_data.append(0)
                if (consecutive_zero_counter == 0) and (sum(posterior_sublist) == 0) and (len(posterior_sublist) == 3) and (informations_number%2 == 1 and informations_number != 1):
                    if (violation_polarity == True):
                        timestamp.append(counter)
                        code.append(1)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(1)
                        timestamp.append(counter)
                        code.append(0)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(0)
                        converted_data_y.append("+s")
                    elif (violation_polarity == False):
                        timestamp.append(counter)
                        code.append(-1)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(-1)
                        timestamp.append(counter)
                        code.append(0)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(0)
                        converted_data_y.append("-s")
                    consecutive_zero_counter += 1
                
                elif (consecutive_zero_counter == VIOLATION_NUMBER):
                    if (violation_polarity == True):
                        timestamp.append(counter)
                        code.append(1)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(1)
                        timestamp.append(counter)
                        code.append(0)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(0)
                        converted_data_y.append("+v")
                    elif (violation_polarity == False):
                        timestamp.append(counter)
                        code.append(-1)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(-1)
                        timestamp.append(counter)
                        code.append(0)
                        counter += 0.5
                        timestamp.append(counter)
                        code.append(0)
                        converted_data_y.append("-v")
                    violation_polarity = not violation_polarity
                    consecutive_zero_counter = 0
                
                elif (consecutive_zero_counter != VIOLATION_NUMBER):
                    timestamp.append(counter)
                    code.append(0)
                    counter += 1
                    timestamp.append(counter)
                    code.append(0)

                    consecutive_zero_counter += 1
                    converted_data_y.append(0)

        return code, timestamp, converted_data
    
    def plot(self):
        
        fig, axs = plt.subplots(1)
        
        x_axis = self.code[1]
        y_axis = self.code[0]
        converted_data = self.code[2]

        plt.xticks(np.arange(len(converted_data)), converted_data)
        bit_code = [str(i) for i in self.bits]
        bit_code.insert(0, '')
        plt.yticks([-1, 0, 1], ['-1', '', '1'])

        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()