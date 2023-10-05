class Dispositivo_entrada:

    def __init__(self, tipoentrada, marca) -> None:
        self._tipoentrada = tipoentrada
        self._marca = marca

    def __str__(self) -> str:
        return f'Tipo de Entrada: {self._tipoentrada}, Marca: {self._marca}'
    
    @property
    def tipo_entrada(self):
        return self._tipoentrada
    
    @tipo_entrada.setter
    def tipo_entrada(self, tipoentrada):
        self._tipoentrada = tipoentrada

    @property
    def marca_dispo(self):
        return self._marca
    
    @marca_dispo.setter
    def marca_dispo(self, marca):
        self._marca = marca

if __name__ == "__main__":
    raton1 = Dispositivo_entrada("bluetooth", "lenovo")
    print(raton1)
    print(raton1.marca_dispo)
    print(raton1.tipo_entrada)

    raton2 = Dispositivo_entrada("usb","Razer")
    print(raton2)
    print(raton2.marca_dispo)
    print(raton2.tipo_entrada)
