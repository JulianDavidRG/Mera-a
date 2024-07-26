class Animal:
    def __init__(self,name) -> None:
        self.name=name
        self.edad=0
        self.esta_muerto=False
        self.nivel_de_hambre=0##propiedad
        self.tamaño=1 ##propiedad
        pass

    def respira(self):##metodo
        pass    

    def cumple_años(self): ##metodo
        self.edad=self.edad+1
        pass   

    def muere(self):##metodo
        self.esta_muerto=True
        pass    

    def crece(self, cuanto):##metodo
        self.tamaño=self.tamaño+cuanto
        pass    


class Perro(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

        self.longitud_colmillos=1
        pass

    def ladra (self):
        print("woww")
        pass

    def mudar_colmillos(self):
        self.longitud_colmillos=3
        pass
