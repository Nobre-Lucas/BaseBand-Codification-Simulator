import matplotlib.pyplot as plt


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
        x = [i for i in range(0, len(self.bits))]
        plt.figure(figsize=(20, 5))
        plt.grid()
        plt.axis([-1, len(self.bits), -1.1, 1.1])
        plt.xlabel("Bits ao longo do tempo")
        plt.ylabel("Níveis")
        plt.plot(x, self.codes["AMI"], label="AMI", color='r', drawstyle='steps-post')
        plt.plot(x, self.codes["Pseudoternary"], label="Multilevel", color='b', drawstyle='steps-post')
        plt.legend()
        plt.show()
        

bits = Encoding("01001100011")
bits.encode()
print(bits.get_bits())
print(bits.get_code("AMI"))
print(bits.get_code("Pseudoternary"))
bits.plot()