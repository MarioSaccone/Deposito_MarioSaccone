class Persona:
    def __init__(self, nome, età):
        self.__nome = nome
        self.__età = età

    def get_nome(self):
            return self.__nome
        
    def get_età(self):
            return self.__età

    def presentazione(self):
        return f"{self.get_nome()} ha {self.get_età()} anni"
    
p = Persona("Mario", 20)
print(p.presentazione())