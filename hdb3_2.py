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

        self.violations = 0
        self.informations = 0
        self.sinalizations = 0
        self.zeros = 0
        self.final_data = []
        self.x_axis = []
        self.y_axis = []
        

    def generate_wave(self, polarity):

    def generate_coordinates(self):
        zero_counter = 0
        counter = 0

        for i in range(len(self.dados)):
            if self.dados[i] == 1:
                
            elif self.dados[i] == 0:

            else:
                raise ValueError("A dados só podem possuir bits 0 ou 1")
            


    def plot_graph(self):

    