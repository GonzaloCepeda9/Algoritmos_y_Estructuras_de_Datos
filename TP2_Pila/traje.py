class Traje:
    def __init__(self, modelo: str, pelicula: str, estado: str):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f'{self.modelo} | {self.pelicula} | {self.estado}'