import matplotlib.pyplot as plt

class NRZI:

    def __init__ (self, dados):

        valida = True
        for i in dados:
            if (i != '0') and (i != '1'):
                valida = False

        if valida:
            self.dados = dados
        else:
            raise ValueError ("A dados só pode possuir bits 0 ou 1")

        self.dados = dados
        self.mensagem = [1]

    def converte_dados (self):

        aux = []

        for i in self.dados:
            aux.append(int(i))

        self.dados = aux

    def transmitir_mensagem (self):

        self.converte_dados()
        
        timestamp = [0]
        counter = 0
        estados = (1, -1)
        estado = 0

        for i in self.dados: #10110010

            counter += 1
            
            if i == 1:        
                estado = 1 if (estado == 0) else 0
                self.mensagem.append(estados[estado])
                self.mensagem.append(estados[estado])

                timestamp.append(counter)
                timestamp.append(counter)

            elif i == 0:
                self.mensagem.append(estados[estado])
                timestamp.append(counter)

        plt.plot(timestamp, self.mensagem)
        plt.show()
        