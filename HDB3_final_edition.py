import matplotlib.pyplot as plt

class HDB3:
    # Método construdor
    def __init__(self, dados):
        # Valida se uma string é compativel com o programa.
        valida = True
        for i in dados:
            if (i != '0') and (i != '1'):
                valida = False
        if valida:
            self.dados = dados
        else:
            raise ValueError("A dados só podem possuir bits 0 ou 1")

        # Transforma uma string em uma lista.
        self.dados = [int(bit) for bit in dados]

        self.VIOLATION_NUMBER = 3

        self.counter = 0
        self.violations = 0
        self.informations = 0
        self.sinalizations = 0
        self.zeros = 0
        self.final_data = []
        self.x_axis = []
        self.y_axis = []

    def generate_pulse(self, polarity):
        if (polarity == True):
            self.x_axis.append(self.counter)
            self.y_axis.append(1)
            self.counter += 0.5
            self.x_axis.append(self.counter)
            self.y_axis.append(1)
            self.x_axis.append(self.counter)
            self.y_axis.append(0)
            self.counter += 0.5
            self.x_axis.append(self.counter)
            self.y_axis.append(0)
        else:
            self.x_axis.append(self.counter)
            self.y_axis.append(-1)
            self.counter += 0.5
            self.x_axis.append(self.counter)
            self.y_axis.append(-1)
            self.x_axis.append(self.counter)
            self.y_axis.append(0)
            self.counter += 0.5
            self.x_axis.append(self.counter)
            self.y_axis.append(0)
    
    def plot_graphic(self):
        plt.plot(self.x_axis, self.y_axis)
        plt.grid()
        plt.show()
        
    def generate_coordinates(self):
        consecutive_zero_counter = 0
        information_polarity = True
        violation_polarity = True

        for i in range(len(self.dados)):
            posterior_sublist = self.dados[i+1:i+4]

            # Tratamentos para 1 (uns):
            if self.dados[i] == 1:
                consecutive_zero_counter = 0
                self.generate_pulse(information_polarity)
                if information_polarity == True:
                    self.final_data.append("+i")
                elif information_polarity == False:
                    self.final_data.append("-i")
                self.informations += 1
                information_polarity = not information_polarity

            # Tratamentos para 0 (zeros):
            elif self.dados[i] == 0:
                self.zeros += 1
                # Bit de sinalização
                if (consecutive_zero_counter == 0) and (sum(posterior_sublist) == 0) and (len(posterior_sublist) == 3) and (self.informations%2 == 1 and self.informations != 1):
                    self.generate_pulse(violation_polarity)
                    if (violation_polarity == True):
                        self.final_data.append("+s")
                    elif (violation_polarity == False):
                        self.final_data.append("-s")
                    self.sinalizations += 1
                    consecutive_zero_counter += 1
                

                # Bit de violação
                elif (consecutive_zero_counter == self.VIOLATION_NUMBER):
                    self.generate_pulse(violation_polarity)
                    if (violation_polarity == True):
                        self.final_data.append("+v")
                    elif (violation_polarity == False):
                        self.final_data.append("-v")

                    violation_polarity = not violation_polarity
                    self.violations += 1
                    consecutive_zero_counter = 0
                
                # Zero comum
                elif (consecutive_zero_counter != self.VIOLATION_NUMBER):
                    self.x_axis.append(self.counter)
                    self.y_axis.append(0)
                    self.counter += 1
                    self.x_axis.append(self.counter)
                    self.y_axis.append(0)

                    consecutive_zero_counter += 1
                    self.final_data.append(0)

            else:
                raise ValueError("A dados só podem possuir bits 0 ou 1")
        
        print(f"SINAL FINAL: {self.final_data}")
        print(f"TAMANHO FINAL: {len(self.final_data)}")
        print(f"UNS (i): {self.informations}")
        print(f"ZEROS: {self.zeros}, dos quais...")
        print(f"VIOLAÇÕES (v): {self.violations}")
        print(f"SINALIZAÇÕES (s): {self.sinalizations}")
        print(f"COMUNS (0): {self.zeros - self.violations - self.sinalizations}")
        self.plot_graphic()


codigo1 = HDB3("01000001100000000010000")
codigo1.generate_coordinates()
