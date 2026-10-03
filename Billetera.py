class Billetera:
    def __init__(self,colores, tamaños, textura, marcas):
        self.colores = colores
        self.tamaños = tamaños
        self.textura = textura
        self.marcas = marcas

    def saludar(self):
        print(f"Mi color es {self.colores} y mi tamaño es {self.tamaños}  y mi marca famosa es {self.marcas} ")
         