import matplotlib.pyplot as plt

class Manchester:
    
    def __init__(self, data):
        
        validation = True
        for i in data:
            if(i != '0') and (i != '1'):
                validation = False
                
        if validation:
            self.data = data
        else:
            raise ValueError ("Os dados só podem possuir bits 0 ou 1")

        self.data =  [int(bit) for bit in data]
        ternary = 1 if self.data[0] == 0 else 0
        self.mensagem = [1 if self.data[0] == 0 else 0]
        self.timestamp = []
    
        
    def convert_data(self):

            aux = []
    
            for i in self.data:
                aux.append(int(i))
    
            self.data = aux
            
    def transmit_message(self):
        self.convert_data()
            
        estados = (1, 0)
        counter = 0
        contador2 = 0
        for i in self.data: #10110010
            
            if i == 1:
                self.mensagem.append(estados[1])
                self.timestamp.append(counter)
                counter += 0.5
                #print(estados[i])
                #print("Esse é o counter após transicionar no bit 1: ", counter)
           

                self.mensagem.append(estados[0])
                self.timestamp.append(counter)

                self.mensagem.append(estados[0])
                self.timestamp.append(counter)
                counter += 0.5
                #print(estados[i])
                #print("Esse é o counter após passar no bit 1: ", counter)

            elif i == 0:

                self.mensagem.append(estados[0])
                self.timestamp.append(counter)  
                counter += 0.5

                #print(estados[i])
                #print("Esse é o counter após transicionar no bit 0: ", counter)

                self.mensagem.append(estados[1])
                self.timestamp.append(counter)

                self.mensagem.append(estados[1])
                self.timestamp.append(counter)
                counter += 0.5

                #print(estados[i])
                #print("Esse é o counter após passar no bit 0: ", counter)
            
            if contador2 < len(self.data)-1:
                if (self.data[contador2+1] == 0 and self.data[contador2] == 0):
                    self.mensagem.append(estados[0])
                    self.timestamp.append(counter)
                    print("teste")

                if (self.data[contador2+1] == 1 and self.data[contador2] == 1):
                    self.mensagem.append(estados[1])
                    self.timestamp.append(counter)
                    print("teste2")
            contador2 += 1

        if(self.data[-1] == 1):
    
            self.mensagem.append(estados[0])
            self.timestamp.append(counter)  

        if(self.data[-1] == 0):
    
            self.mensagem.append(estados[1])
            self.timestamp.append(counter)  

        print(self.mensagem)
        print(self.timestamp)

        self.mensagem.pop()

        plt.plot(self.timestamp, self.mensagem)
        plt.show()


inputbits = Manchester("10011001")
inputbits.transmit_message()
