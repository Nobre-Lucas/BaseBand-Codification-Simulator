import matplotlib.pyplot as plt


class Encoding:

    def __init__(self, word):
        self.word = word
        self.code = []

    def display(self):
        print(self.word)

    def displayCode(self):
        print(self.code)

    def multilevel(self):
        self.code = []

        level = True

        for bit in self.word:
            if bit == "0":
                self.code.append(0)
            else:
                if level is True:
                    self.code.append(1)
                else:
                    self.code.append(-1)
                level = not level

        return self.code

    def plot(self):
        x = [i for i in range(0, len(self.code))]
        y = self.code
        plt.figure(figsize=(20, 5))
        plt.grid()
        plt.axis([-1, len(self.word), -1.1, 1.1])
        plt.xlabel("Bits ao longo do tempo")
        plt.ylabel("Níveis")
        plt.plot(x, y, label="Multilevel", color='red', drawstyle='steps-pre')
        plt.legend()
        plt.show()


bits = Encoding("01001100011")
bits.display()
bits.multilevel()
bits.displayCode()
bits.plot()
