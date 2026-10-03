class Libro:
    def __init__(self,titulo, autor, cantidadDePaginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidadDePaginas = cantidadDePaginas

    def saludar(self):
        print(f"El libro es {self.titulo}, el autor/autora es {self.autor} y la cantidad de paginas son {self.cantidadDePaginas}")