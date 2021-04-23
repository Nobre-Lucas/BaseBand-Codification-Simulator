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

    # Gera as coordenadas para plotar o gráfico mais tarde.    
    def gerar_coordenadas(self):
        # Eixo x e y:
        eixo_x = []
        eixo_y = []

        # Controle para dados:
        controle = []

        # Contador irá percorrer a lista:
        counter = 0

        # Contador para contar quantos zeros se passaram até o bit de violação, para evitar repetições do bit de violação em cadeias como "00000"
        zero_counter = 0

        # O pulso irá identificar se o pulso será negativo (False) ou positivo (True).
        pulse_info = True
        pulse_sin = False
        pulse_vio = True

        for i in range(len(self.dados)):
            subcadeia_posterior = self.dados[i+1:i+4]
            subcadeia_anterior = self.dados[i-3:i+1]

            # Tratamentos para 1:
            if self.dados[i] == 1:
                if pulse_info == True:
                    eixo_x.append(counter)
                    eixo_y.append(1)
                    counter += 0.5
                    eixo_x.append(counter)
                    eixo_y.append(1)
                    eixo_x.append(counter)
                    eixo_y.append(0)
                    counter += 0.5
                    eixo_x.append(counter)
                    eixo_y.append(0)
                    pulse_info = not pulse_info
                    
                    zero_counter = 0
                    controle.append("+i")
                else:
                    eixo_x.append(counter)
                    eixo_y.append(-1)
                    counter += 0.5
                    eixo_x.append(counter)
                    eixo_y.append(-1)
                    eixo_x.append(counter)
                    eixo_y.append(0) 
                    counter += 0.5
                    eixo_x.append(counter)
                    eixo_y.append(0)
                    pulse_info = not pulse_info
                    
                    zero_counter = 0
                    controle.append("-i")

            # TRATAMENTO PARA 0.
            elif self.dados[i] == 0:           

                # VERIFICAÇÃO SE ESCREVERÁ UM BIT DE SINALIZAÇÃO
                if sum(subcadeia_posterior) == 0 and len(subcadeia_posterior) >= 3 and zero_counter == 0:
                    if (pulse_info == pulse_vio):
                        if pulse_sin == True:
                            eixo_x.append(counter)
                            eixo_y.append(1)
                            counter += 0.5
                            eixo_x.append(counter)
                            eixo_y.append(1)
                            eixo_x.append(counter)
                            eixo_y.append(0)
                            counter += 0.5
                            eixo_x.append(counter)
                            eixo_y.append(0)
                            pulse_sin = not pulse_sin

                            zero_counter += 1
                            controle.append("+S")
                        elif pulse_sin == False:
                            eixo_x.append(counter)
                            eixo_y.append(-1)
                            counter += 0.5
                            eixo_x.append(counter)
                            eixo_y.append(-1)
                            eixo_x.append(counter)
                            eixo_y.append(0)
                            counter += 0.5
                            eixo_x.append(counter)
                            eixo_y.append(0)
                            pulse_sin = not pulse_sin

                            zero_counter += 1
                            controle.append("-S")
                    

                # VERIFICAÇÃO SE DESENHARÁ UM BIT DE VIOLAÇÃO
                elif zero_counter == 3:
                    if pulse_vio == True:
                        eixo_x.append(counter)
                        eixo_y.append(1)
                        counter += 0.5
                        eixo_x.append(counter)
                        eixo_y.append(1)
                        eixo_x.append(counter)
                        eixo_y.append(0)
                        counter += 0.5
                        eixo_x.append(counter)
                        eixo_y.append(0)
                        pulse_vio = not pulse_vio
                        
                        zero_counter = 0
                        controle.append("+V")
                    elif pulse_vio == False:
                        eixo_x.append(counter)
                        eixo_y.append(-1)
                        counter += 0.5
                        eixo_x.append(counter)
                        eixo_y.append(-1)
                        eixo_x.append(counter)
                        eixo_y.append(0)
                        counter += 0.5
                        eixo_x.append(counter)
                        eixo_y.append(0)
                        pulse_vio = not pulse_vio
                        
                        zero_counter = 0
                        controle.append("-V")   
                else:
                    eixo_x.append(counter)
                    eixo_y.append(0)
                    counter += 1
                    eixo_x.append(counter)
                    eixo_y.append(0)
                    
                    zero_counter += 1
                    controle.append(0)

        print(f"Resultado esperado: ")
        print("[0, '+i', 0, 0, 0, '+v', 0, '-i', '+i', '-s', 0, 0, '-v', '+s', 0, 0, '+v', 0, '-i', 0, 0, 0, '-v']")
        print(f" Bits Inf: 4.")
        print(f" Bits Vio: 4.")
        print(f" Bits Sin: 2.")
        print(f" Zeros   : 13.")
        print(f"Total: {len(self.dados)}")

        print(f"Resultado adquirido: ")
        print(controle)
        print(f"tamanho do controle: {len(controle)}")
        

        plt.plot(eixo_x, eixo_y)
        plt.grid()
        plt.show()
                
codigo1 = HDB3("01000001100000000010000")
codigo1.gerar_coordenadas()