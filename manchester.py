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
            
        
    def convert_data(self):

            aux = []
    
            for i in self.data:
                aux.append(int(i))
    
            self.data = aux
            
    def transmit_message(self):
        self.convert_data()
            
            