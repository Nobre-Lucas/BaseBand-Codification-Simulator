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
                          "HDB3": [],
                          "Manchester": [],
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

    def hdb3(self):
        consecutive_zero_counter = 0
        counter = 0
        informations_number = 0
        VIOLATION_NUMBER = 3
        timestamp = []
        code = []
        information_polarity = True
        violation_polarity = True

        for i in range(len(self.codes["Bits"])):
            posterior_sublist = self.codes["Bits"][i+1:i+4]

            if self.codes["Bits"][i] == 1:
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
                informations_number += 1
                information_polarity = not information_polarity

            elif self.codes["Bits"][i] == 0:
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

                    violation_polarity = not violation_polarity
                    consecutive_zero_counter = 0
                
                elif (consecutive_zero_counter != VIOLATION_NUMBER):
                    timestamp.append(counter)
                    code.append(0)
                    counter += 1
                    timestamp.append(counter)
                    code.append(0)

                    consecutive_zero_counter += 1

            else:
                raise ValueError("A dados só podem possuir bits 0 ou 1")

        return code, timestamp


    def manchester(self) -> list:
      code = [1 if self.codes["Bits"][0] == 0 else 0]
      timestamp = []

      counter = 0
      states = (1, 0)
      counter2 = 0

      for i in self.codes["Bits"]: #10110010
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

            
        if counter2 < len(self.codes["Bits"])-1:
          if (self.codes["Bits"][counter2+1] == 0 and self.codes["Bits"][counter2] == 0):
            code.append(states[0])
            timestamp.append(counter)
            print("teste")

          if (self.codes["Bits"][counter2+1] == 1 and self.codes["Bits"][counter2] == 1):
            code.append(states[1])
            timestamp.append(counter)
            print("teste2")
        counter2 += 1
      
      if (self.codes["Bits"][-1] == 1):
        
        code.append(states[0])
        timestamp.append(counter)  

      if (self.codes["Bits"][-1] == 0):
    
        code.append(states[1])
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
        self.codes["HDB3"] = self.hdb3()[0]
        self.codes["2B1Q"] = self.tboq()[0]
        self.codes["Manchester"] = self.manchester()[0]


    def plot(self, scheme: str):
        
        fig, axs = plt.subplots(1)

        x_axis = []
        y_axis = []

        if scheme == "NRZI":
            x_axis = self.nrzi()[1]
            y_axis = self.codes["NRZI"]

            bit_code = [str(i) for i in self.codes["Bits"]]
            bit_code.insert(0, '')
            
            plt.xticks(np.arange(len(x_axis)), bit_code)
            plt.yticks([-1, 0, 1], ['-1', '', '1'])

        elif scheme == "HDB3":
            x_axis = self.hdb3()[1]
            y_axis = self.codes["HDB3"]
           
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

        elif scheme == "Manchester":
            x_axis = self.manchester()[1]
            y_axis = self.codes["Manchester"]

            bit_code = []
            for i in self.codes["Bits"]:
              bit_code.append('')
              bit_code.append(i)

            plt.yticks([0, 1], [ '0', '1'])
            plt.xticks(np.arange(0, len(x_axis), 0.5), bit_code)
            
        else:
            raise ValueError("Available schemes: NRZI, HDB3, Manchester, 2B1Q")

        plt.plot(x_axis, y_axis, 'black', linewidth=2)
        plt.grid()
        plt.show()

bits = Encoding("10110010")
bits.encode()
print("Bits:", bits.get_bits())
print("NRZI:", bits.get_code("NRZI"))
print("Manchester:", bits.get_code("Manchester"))
print("2B1Q:", bits.get_code("2B1Q"))

bits.plot("Manchester")